import json
import os
from flask import Flask, jsonify, request, send_from_directory, render_template

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE, "data")
STATIC_DIR = os.path.join(BASE, "static")
CONTENT_FILE = os.path.join(DATA_DIR, "content.json")
PROGRESS_FILE = os.path.join("/tmp" if os.environ.get("VERCEL") else DATA_DIR, "progress.json")

app = Flask(__name__, template_folder="templates", static_folder="static")


def load_content():
    with open(CONTENT_FILE, encoding="utf-8") as f:
        return json.load(f)


def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return _default_progress()
    with open(PROGRESS_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_progress(p):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(p, f, indent=2, ensure_ascii=False)


def _default_progress():
    content = load_content()
    chapters = {}
    for ch in content["chapters"]:
        cid = ch["chapter_id"]
        units = {}
        for u in ch["units"]:
            units[u["unit_id"]] = "not_started"
        chapters[cid] = {
            "completed": False,
            "unlocked": ch.get("unlocked", False),
            "accuracy": None,
            "coming_soon": ch.get("coming_soon", False),
            "units": units,
        }
    return {
        "current_chapter": "ch01",
        "current_unit": "ch01_concept_intro",
        "current_item": 0,
        "chapters": chapters,
        "questions": {},
    }


# ─── Routes ──────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/path")
def api_path():
    content = load_content()
    progress = load_progress()
    result = []
    for ch in content["chapters"]:
        cid = ch["chapter_id"]
        cp = progress["chapters"].get(cid, {})
        units_done = sum(1 for v in cp.get("units", {}).values() if v == "completed")
        units_total = len([u for u in ch["units"] if u["unit_type"] != "review"])
        pct = round(units_done / units_total * 100) if units_total else 0
        result.append({
            "chapter_id": cid,
            "title": ch["title"],
            "description": ch["description"],
            "priority": ch.get("priority", "medium"),
            "unlocked": cp.get("unlocked", False),
            "completed": cp.get("completed", False),
            "coming_soon": ch.get("coming_soon", False),
            "accuracy": cp.get("accuracy"),
            "progress_pct": pct,
        })
    return jsonify({"chapters": result, "current_chapter": progress.get("current_chapter")})


@app.route("/api/chapter/<chapter_id>")
def api_chapter(chapter_id):
    content = load_content()
    progress = load_progress()
    chapter = next((c for c in content["chapters"] if c["chapter_id"] == chapter_id), None)
    if not chapter:
        return jsonify({"error": "Not found"}), 404
    cp = progress["chapters"].get(chapter_id, {})
    if not cp.get("unlocked") and not chapter.get("coming_soon"):
        return jsonify({"error": "Locked"}), 403
    units = []
    for u in chapter["units"]:
        uid = u["unit_id"]
        units.append({
            "unit_id": uid,
            "unit_type": u["unit_type"],
            "title": u["title"],
            "estimated_minutes": u.get("estimated_minutes", 5),
            "status": cp.get("units", {}).get(uid, "not_started"),
            "item_count": len(u["items"]),
        })
    return jsonify({"chapter": chapter, "units": units, "chapter_progress": cp})


@app.route("/api/unit/<unit_id>")
def api_unit(unit_id):
    content = load_content()
    progress = load_progress()
    for ch in content["chapters"]:
        for u in ch["units"]:
            if u["unit_id"] == unit_id:
                items = _enrich_items(u["items"], progress)
                return jsonify({
                    "unit_id": unit_id,
                    "unit_type": u["unit_type"],
                    "title": u["title"],
                    "chapter_id": ch["chapter_id"],
                    "items": items,
                    "current_item": progress.get("current_item", 0)
                        if progress.get("current_unit") == unit_id else 0,
                })
    return jsonify({"error": "Not found"}), 404


def _enrich_items(items, progress):
    enriched = []
    for item in items:
        if item.get("type") == "concept_card":
            enriched.append(item)
        else:
            qid = item.get("id")
            q_prog = progress.get("questions", {}).get(qid, {})
            e = dict(item)
            e["times_seen"] = q_prog.get("times_seen", 0)
            e["times_correct"] = q_prog.get("times_correct", 0)
            e["last_result"] = q_prog.get("last_result")
            e["hint_used"] = q_prog.get("hint_used", False)
            enriched.append(e)
    return enriched


@app.route("/api/answer", methods=["POST"])
def api_answer():
    body = request.get_json()
    question_id = body.get("question_id")
    correct = body.get("correct", False)
    hint_used = body.get("hint_used", False)
    unit_id = body.get("unit_id")
    item_index = body.get("item_index", 0)

    progress = load_progress()
    if "questions" not in progress:
        progress["questions"] = {}
    q = progress["questions"].setdefault(question_id, {
        "times_seen": 0, "times_correct": 0, "last_result": None, "hint_used": False
    })
    q["times_seen"] += 1
    if correct and not hint_used:
        q["times_correct"] += 1
    q["last_result"] = "correct" if correct else "wrong"
    q["hint_used"] = hint_used

    progress["current_unit"] = unit_id
    progress["current_item"] = item_index + 1
    save_progress(progress)
    return jsonify({"ok": True})


@app.route("/api/unit/complete", methods=["POST"])
def api_unit_complete():
    body = request.get_json()
    unit_id = body.get("unit_id")
    chapter_id = body.get("chapter_id")

    progress = load_progress()
    cp = progress["chapters"].setdefault(chapter_id, {"completed": False, "unlocked": True, "accuracy": None, "units": {}})
    cp["units"][unit_id] = "completed"
    progress["current_unit"] = unit_id
    progress["current_item"] = 0
    save_progress(progress)
    return jsonify({"ok": True})


@app.route("/api/chapter/complete", methods=["POST"])
def api_chapter_complete():
    body = request.get_json()
    chapter_id = body.get("chapter_id")
    accuracy = body.get("accuracy")

    content = load_content()
    progress = load_progress()
    cp = progress["chapters"].setdefault(chapter_id, {})
    cp["completed"] = True
    cp["accuracy"] = accuracy

    # Unlock next chapter
    chapter_ids = [c["chapter_id"] for c in content["chapters"]]
    try:
        idx = chapter_ids.index(chapter_id)
        if idx + 1 < len(chapter_ids):
            next_id = chapter_ids[idx + 1]
            next_ch = content["chapters"][idx + 1]
            if not next_ch.get("coming_soon"):
                progress["chapters"].setdefault(next_id, {})["unlocked"] = True
                progress["current_chapter"] = next_id
    except ValueError:
        pass

    save_progress(progress)
    # HOOK: Agent7 – weak spot analysis after chapter complete
    return jsonify({"ok": True, "next_chapter": progress.get("current_chapter")})


@app.route("/api/progress")
def api_progress():
    progress = load_progress()
    content = load_content()
    total_q = sum(
        1 for ch in content["chapters"]
        for u in ch["units"]
        for item in u["items"]
        if item.get("type") != "concept_card"
    )
    answered = len(progress.get("questions", {}))
    correct = sum(1 for q in progress.get("questions", {}).values() if q.get("last_result") == "correct")
    chapters_done = sum(1 for cp in progress["chapters"].values() if cp.get("completed"))
    return jsonify({
        "total_questions": total_q,
        "answered": answered,
        "correct": correct,
        "accuracy": round(correct / answered * 100) if answered else 0,
        "chapters_completed": chapters_done,
        "chapters_total": len([c for c in content["chapters"] if not c.get("coming_soon")]),
        # HOOK: Agent8 – difficulty adaptation data here
    })


@app.route("/api/review/<chapter_id>")
def api_review(chapter_id):
    content = load_content()
    progress = load_progress()
    wrong_ids = [
        qid for qid, q in progress.get("questions", {}).items()
        if q.get("last_result") == "wrong" and qid.startswith(chapter_id)
    ]
    if not wrong_ids:
        return jsonify({"items": [], "message": "Keine Fehler – Kapitel fehlerfrei!"})
    items = []
    for ch in content["chapters"]:
        if ch["chapter_id"] == chapter_id:
            for u in ch["units"]:
                for item in u["items"]:
                    if item.get("id") in wrong_ids:
                        items.append(item)
    return jsonify({"items": items})


@app.route("/api/visual/<name>")
def api_visual(name):
    return send_from_directory(os.path.join(STATIC_DIR, "img"), name)


# HOOK: Agent7 – GET /api/weak_spots → topics with >40% error rate
@app.route("/api/weak_spots")
def api_weak_spots():
    return jsonify({"hook": "Agent7 – not yet implemented"})


# HOOK: Agent8 – GET /api/performance_trend
@app.route("/api/performance_trend")
def api_performance_trend():
    return jsonify({"hook": "Agent8 – not yet implemented"})


# HOOK: Agent9 – POST /api/generate_questions
@app.route("/api/generate_questions", methods=["POST"])
def api_generate_questions():
    return jsonify({"hook": "Agent9 – not yet implemented"})


# HOOK: Agent10 – POST /api/exam/generate
@app.route("/api/exam/generate", methods=["POST"])
def api_exam_generate():
    return jsonify({"hook": "Agent10 – not yet implemented"})


# HOOK: Agent10 – POST /api/exam/evaluate
@app.route("/api/exam/evaluate", methods=["POST"])
def api_exam_evaluate():
    return jsonify({"hook": "Agent10 – not yet implemented"})


if __name__ == "__main__":
    from r_simulator import generate_all
    generate_all()
    app.run(debug=True, port=5000)
