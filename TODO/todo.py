from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список задач
tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    description = request.form["description"]
    tasks.append({"title": title, "description": description, "completed": False})
    return redirect(url_for("index"))

@app.route("/complete/<int:index>")
def complete(index):
    tasks[index]["completed"] = True
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    tasks.pop(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
