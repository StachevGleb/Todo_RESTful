from flask import jsonify, request
from backend import app, db
from backend.models import Task


@app.route('/health')
def health():
    return "ok"


# The GET and POST route handler.
@app.route("/tasks", methods=['GET', 'POST'])
def all_tasks():
    tasks = Task.query.all()
    task_list = []
    for task in tasks:
        task_data = {
            'task_id': task.task_id,
            'title': task.title,
            'essence': task.essence,
            'status': task.status
        }
        task_list.append(task_data)
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.json
        new_task = Task(title=post_data['title'], essence=post_data['essence'], status=post_data['status'])
        db.session.add(new_task)
        db.session.commit()
        response_object['message'] = 'Task Added!'
    else:
        response_object['tasks'] = task_list
    return jsonify(response_object)


# The PUT and DELETE route handler.
@app.route("/tasks/<int:task_id>", methods=['POST', 'DELETE', 'GET'])
def single_task(task_id):
    task = Task.query.get_or_404(task_id)
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.json
        task.title = post_data['title']
        task.essence = post_data['essence']
        task.status = post_data['status']
        db.session.commit()
        response_object['message'] = 'Task Updated!'
    if request.method == "DELETE":
        remove_task(task_id)
        response_object['message'] = 'Task removed!'
    return jsonify(response_object)


# Removing the task to update
def remove_task(task_id):
    task_to_remove = Task.query.get(task_id)
    if task_to_remove:
        db.session.delete(task_to_remove)
        db.session.commit()
        return True
    else:
        print("Task not found with ID:", task_id)
        return False


@app.route('/', methods=['GET'])
def greetings():
    return "Hello, JUPIplus RESTful Todo !"


@app.route('/test', methods=['GET'])
def test():
    return "JUPIplus"
