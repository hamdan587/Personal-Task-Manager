import json
from datetime import datetime

# Define the tasks file path
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from the JSON file."""
    try:
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)
            return tasks if tasks else []  # Return an empty list if tasks.json is empty
    except (FileNotFoundError, json.JSONDecodeError):
        # Create an empty JSON file if it doesn’t exist or is invalid
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(title, due_date, priority, description=""):
    """Add a new task to the task list."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "due_date": due_date,
        "priority": priority,
        "description": description,
        "completed": False,
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{title}" added successfully.')

def mark_completed(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            print(f'Task {task_id} marked as completed.')
            return
    print(f'Task {task_id} not found.')

def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task {task_id} deleted successfully.')

def update_task(task_id, title=None, due_date=None, priority=None, description=None):
    """Update details of an existing task."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            if title: task['title'] = title
            if due_date: task['due_date'] = due_date
            if priority: task['priority'] = priority
            if description: task['description'] = description
            save_tasks(tasks)
            print(f'Task {task_id} updated successfully.')
            return
    print(f'Task {task_id} not found.')
