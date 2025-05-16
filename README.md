# Simple To-Do API with Python & Flask

This is a basic CRUD REST API that lets users manage to-do tasks. It’s built using **Python (Flask)** and uses **SQLite** for storage.

## Features
- Add new tasks  
- Get all tasks  
- Update task status (done/not done)  
- Delete tasks  

## How to Run
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the server
python app.py

# 3. API is live at
http://localhost:5000/tasks

Tech Stack
Python
Flask
SQLite (local DB)
REST API (CRUD)

Sample API Calls
# Add a task
curl -X POST http://localhost:5000/task -H "Content-Type: application/json" -d '{"task": "Buy groceries"}'

# Get all tasks
curl http://localhost:5000/tasks

# Update task as done
curl -X PUT http://localhost:5000/task/1 -H "Content-Type: application/json" -d '{"done": true}'

# Delete a task
curl -X DELETE http://localhost:5000/task/1
