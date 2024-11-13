from flask import Flask, render_template, request, redirect, url_for
from task_manager import load_tasks, add_task, update_task, mark_completed, delete_task

app = Flask(__name__)

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        due_date = request.form['due_date']
        priority = request.form['priority']
        description = request.form['description']
        add_task(title, due_date, priority, description)
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update(task_id):
    task = next((t for t in load_tasks() if t['id'] == task_id), None)
    if not task:
        return redirect(url_for('index'))
    if request.method == 'POST':
        title = request.form['title']
        due_date = request.form['due_date']
        priority = request.form['priority']
        description = request.form['description']
        update_task(task_id, title, due_date, priority, description)
        return redirect(url_for('index'))
    return render_template('update_task.html', task=task)

@app.route('/complete/<int:task_id>')
def complete(task_id):
    mark_completed(task_id)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
