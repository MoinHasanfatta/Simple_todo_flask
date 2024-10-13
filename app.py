from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for all domains and routes

# Simple list to store tasks
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)  # Return all tasks as JSON

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')  # Get task from JSON body
    if task:
        tasks.append(task)  # Add task to list
        return jsonify({'message': 'Task added'}), 200
    return jsonify({'message': 'No task provided'}), 400  # Handle empty task

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):  # Check if task ID is valid
        tasks.pop(task_id)  # Remove task from list
        return jsonify({'message': 'Task deleted'}), 200
    return jsonify({'message': 'Task not found'}), 404  # Handle invalid task ID

if __name__ == '__main__':
    app.run(debug=True)
