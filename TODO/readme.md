**Flask ToDo App**

This is a simple Flask application that allows users to create and manage a list of tasks.

**Requirements**

Python 3.6 or newer
Flask
Installation
Clone this repository
Install dependencies: pip install flask


**Run the app: **

python app.py
Open http://localhost:8000/ in your web browser

**Usage**

GET / - Displays a list of tasks.
POST /add - Adds a new task to the list.
GET /complete/<int:task_index> - Marks a task as completed.
GET /delete/<int:task_index> - Deletes a task from the list.

**Contributing**

Contributions are welcome! Please open an issue or submit a pull request if you would like to make changes to this app.

**License**

This app is licensed under the MIT License. See the LICENSE file for more information
