from flask import Flask, render_template, request, redirect, url_for

# CREATE THE APP
app = Flask(__name__)


# Empty Todo
todo_list = []


@app.route('/')
def index():
    return render_template("index.html", todo_list=todo_list)


@app.route('/add', methods=["POST"])
def add():
    todo = request.form['todo']
    todo_list.append({"task": todo, "done": False})
    return redirect(url_for("index"))


@app.route('/check/<int:index>', methods=["POST"])
def check(index):
    todo_list[index]['done'] = not todo_list[index]['done']
    return redirect(url_for("index"))


@app.route('/delete/<int:index>')
def delete(index):
    del todo_list[index]
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
