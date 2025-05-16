from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, done BOOLEAN)""")
    conn.commit()
    conn.close()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)

@app.route('/task', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, done) VALUES (?, ?)", (task, False))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task added'}), 201

@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    done = data.get('done', False)
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET done = ? WHERE id = ?", (done, task_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task updated'})

@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
