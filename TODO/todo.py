from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список задач
tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks, enumerate=enumerate)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    description = request.form["description"]
    tasks.append({"title": title, "description": description, "completed": False})
    return redirect(url_for("index"))

@app.route("/complete/<int:task_index>")
def complete(task_index):
    tasks[task_index]["completed"] = True
    return redirect(url_for("index"))

@app.route("/delete/<int:task_index>")
def delete(task_index):
    tasks.pop(task_index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=8000)
