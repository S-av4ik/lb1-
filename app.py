"""Task Tracker API (демонстраційний застосунок для лабораторної)."""
from flask import Flask, jsonify, request, abort

__version__ = "1.0.1"

app = Flask(__name__)
TASKS = {}
_next_id = 1


@app.get("/health")
def health():
    return jsonify(status="ok", version=__version__)


@app.post("/tasks")
def create_task():
    global _next_id
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        abort(400, description="title is required")
    task = {"id": _next_id, "title": title, "done": False}
    TASKS[_next_id] = task
    _next_id += 1
    return jsonify(task), 201


@app.get("/tasks")
def list_tasks():
    return jsonify(list(TASKS.values()))


@app.get("/tasks/<int:task_id>")
def get_task(task_id):
    task = TASKS.get(task_id) or abort(404)
    return jsonify(task)


@app.put("/tasks/<int:task_id>")
def update_task(task_id):
    task = TASKS.get(task_id) or abort(404)
    data = request.get_json(silent=True) or {}
    if "title" in data:
        task["title"] = str(data["title"]).strip()
    if "done" in data:
        task["done"] = bool(data["done"])
    return jsonify(task)


@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    TASKS.pop(task_id, None) or abort(404)
    return "", 204
