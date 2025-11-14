
from flask import Flask, render_template, request, redirect
import redis

app = Flask(__name__)

@app.route("/")
def get_all_todo():
    r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
    t = r.keys('todo:*')
    todo = []
    for key in t:
        if r.type(key) == 'hash':
            kk = r.hgetall(key)
            todo.append(kk)
    return render_template("todos.html", todo=todo)

@app.route("/add", methods=['GET', 'POST'])
def add_todo():
    if request.method == 'POST':
        r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        done = "false"
        id = r.incr("todo:id")
        r.hset(f"todo:{id}", mapping={
            "id":id,
            "title":title,
            "description":description,
            "date":date,
            "done":done,
        })
        return redirect("/")
    else:
        return render_template("create_todo.html")
    
@app.route("/delete/<int:id>", methods=['GET'])
def delete_todo(id):
    r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
    r.delete(f'todo:{id}')
    return redirect("/")

@app.route("/done/<int:id>", methods=['GET'])
def done_todo(id):
    r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
    r.hset(f"todo:{id}", mapping={
        "done":"true",
    })
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)