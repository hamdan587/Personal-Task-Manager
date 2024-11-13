
# 🌟 Personal Task Manager 🌟

A sleek and efficient **Flask** web application for managing your tasks effortlessly! This intuitive tool is perfect for those looking to stay organized and get things done.

---

## 📋 Features

- 📝 **Add, Edit, Complete, and Delete Tasks**: Manage all your tasks with essential CRUD operations.
- 🎯 **Priority Levels**: Set priority levels to categorize tasks effectively.
- 🌐 **Clean and Simple UI**: A responsive interface for easy navigation and task viewing.
- 💾 **Persistent Data**: Uses a JSON file for storage (MongoDB support coming soon!).

---

## 🚀 Getting Started

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/yourusername/Personal-Task-Manager.git
cd Personal-Task-Manager
```

2️⃣ **Set up the virtual environment and install dependencies:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`
pip install -r requirements.txt
```

3️⃣ **Run the application:**
```bash
python app.py
```

4️⃣ **Access the app in your browser:**
   - Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛠️ Usage

- **Home**: View all tasks with options to edit, complete, or delete.
- **Add New Task**: Create a new task with title, description, due date, and priority level.
- **Manage Tasks**: Mark tasks as completed to track progress.

---

## 📂 JSON Data Storage

All tasks are stored in a `tasks.json` file within the project. This file serves as the primary data source until future MongoDB integration.

---

## 🐳 Docker Setup

Run the application in a Docker container:

1. **Build the Docker image:**
   ```bash
   docker build -t personal-task-manager .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 5000:5000 personal-task-manager
   ```

---

## ✅ Testing

Unit tests ensure the core functionality of the app. Run tests using `pytest`:

```bash
pytest tests/test_task_manager.py
```

---

## 🔄 GitHub Actions for Continuous Integration

This repository includes a GitHub Actions workflow for automated testing on every push and pull request to the `main` branch. 

---

Your Productivity Partner! — Track, manage, and accomplish your tasks seamlessly with Personal Task Manager!
