from flask import Flask, request, jsonify, send_from_directory
import sqlite3

app = Flask(__name__, static_folder="frontend", static_url_path="/static")


def get_db():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    return send_from_directory("frontend", "index.html")


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("frontend", filename)


@app.route("/api/tasks")
def get_tasks():

    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks ORDER BY id").fetchall()
    conn.close()

    return jsonify([dict(t) for t in tasks])


@app.route("/api/tasks", methods=["POST"])
def add_task():

    data = request.json

    conn = get_db()

    conn.execute(
        "INSERT INTO tasks(title,due_date,note,priority,completed) VALUES (?,?,?,?,0)",
        (data["title"], data["due_date"], data["note"], data["priority"])
    )

    conn.commit()
    conn.close()

    return jsonify({"success": True})


@app.route("/api/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):

    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"success": True})


@app.route("/api/tasks/<int:id>/toggle", methods=["POST"])
def toggle_task(id):

    conn = get_db()

    task = conn.execute(
        "SELECT completed FROM tasks WHERE id=?", (id,)
    ).fetchone()

    new_status = 0 if task["completed"] else 1

    conn.execute(
        "UPDATE tasks SET completed=? WHERE id=?",
        (new_status, id)
    )

    conn.commit()
    conn.close()

    return jsonify({"success": True})


@app.route("/api/search")
def search():

    q = request.args.get("q", "")

    conn = get_db()

    tasks = conn.execute(
        "SELECT * FROM tasks WHERE title LIKE ? OR note LIKE ?",
        ('%' + q + '%', '%' + q + '%')
    ).fetchall()

    conn.close()

    return jsonify([dict(t) for t in tasks])


@app.route("/api/sort", methods=["POST"])
def sort_tasks():

    by = request.json["by"]

    conn = get_db()

    if by == "title":

        tasks = conn.execute(
            "SELECT * FROM tasks ORDER BY title"
        ).fetchall()

    elif by == "priority":

        tasks = conn.execute("""
        SELECT * FROM tasks
        ORDER BY
        CASE priority
            WHEN 'HIGH' THEN 1
            WHEN 'MEDIUM' THEN 2
            WHEN 'LOW' THEN 3
        END
        """).fetchall()

    else:

        tasks = conn.execute(
            "SELECT * FROM tasks ORDER BY id"
        ).fetchall()

    conn.close()

    return jsonify([dict(t) for t in tasks])


if __name__ == "__main__":

    conn = sqlite3.connect("tasks.db")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        due_date TEXT,
        note TEXT,
        priority TEXT,
        completed INTEGER
    )
    """)

    conn.commit()
    conn.close()

    app.run(debug=True)