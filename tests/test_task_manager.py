import pytest
import json
from app import app, load_tasks, add_task, update_task, mark_completed, delete_task

@pytest.fixture
def client():
    """Create a test client."""
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

@pytest.fixture
def setup():
    """Setup tasks for testing."""
    tasks = load_tasks()
    tasks.clear() 
    add_task('Test Task 1', '2024-12-31', 'High')
    add_task('Test Task 2', '2024-12-25', 'Medium')
    add_task('Test Task 3', '2024-12-10', 'Low')
    yield tasks 

# Test 1: Check if the home page (index) loads correctly
def test_index(client, setup):
    """Test the index route to view all tasks."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Task Manager' in response.data
    assert b'Test Task 1' in response.data
    assert b'Test Task 2' in response.data
    assert b'Test Task 3' in response.data

# Test 2: Add a new task
def test_add_task(client):
    """Test the add task route."""
    response = client.post('/add', data={
        'title': 'New Task',
        'due_date': '2024-12-15',
        'priority': 'Low',
        'description': 'This is a new task.'
    })
    assert response.status_code == 302 
    response = client.get('/')
    assert b'New Task' in response.data

# Test 3: Update an existing task
def test_update_task(client, setup):
    """Test updating a task."""
    response = client.post('/update/1', data={
        'title': 'Updated Test Task',
        'due_date': '2024-12-15',
        'priority': 'Medium',
        'description': 'Updated description.'
    })
    assert response.status_code == 302 
    response = client.get('/')
    assert b'Updated Test Task' in response.data
    assert b'Updated description.' in response.data

# Test 4: Mark a task as completed
def test_complete_task(client, setup):
    """Test completing a task."""
    response = client.get('/complete/1')
    assert response.status_code == 302 
    response = client.get('/')
    assert b'Completed' in response.data 

# Test 6: Task is not found when updating a non-existent task
def test_update_non_existent_task(client):
    """Test updating a non-existent task."""
    response = client.post('/update/999', data={
        'title': 'Non-existent Task',
        'due_date': '2024-12-30',
        'priority': 'High',
        'description': 'This task does not exist.'
    })
    assert response.status_code == 302  
    response = client.get('/')
    assert b'Non-existent Task' not in response.data 


# Test 8: Task completion works correctly
def test_task_completion(client, setup):
    """Test marking a task as completed."""
    response = client.get('/complete/3')
    assert response.status_code == 302 
    response = client.get('/')
    assert b'Completed' in response.data 

# Test 9: Checking task update route (GET request)
def test_update_task_get(client, setup):
    """Test the GET method for task update."""
    response = client.get('/update/1')
    assert response.status_code == 200 
    assert b'Update Task' in response.data  

# Test 10: Trying to delete a non-existent task
def test_delete_non_existent_task(client):
    """Test deleting a non-existent task."""
    response = client.get('/delete/999')
    assert response.status_code == 302  
    response = client.get('/')
    assert b'999' not in response.data 
