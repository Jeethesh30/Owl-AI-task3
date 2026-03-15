# 📝 Daily Tasks – Full Stack Task Manager

A modern **Task Management Web Application** built using **Python (Flask), JavaScript, HTML, CSS, and SQLite**.
It allows users to create, manage, search, and track tasks with priority levels and completion status.

The project focuses on building a **clean UI with interactive animations and a functional backend API**.

---

# 🚀 Features

### ✔ Task Management

* Add new tasks
* Delete tasks
* Mark tasks as **Completed / Pending**
* Tasks automatically update in the database

### 🔎 Search & Sorting

* Search tasks by title or notes
* Sort tasks by:

  * Order Added
  * Title
  * Priority

### ⚡ Priority Levels

Each task can be assigned a priority:

* **HIGH**
* **MEDIUM**
* **LOW**

### 📅 Due Dates

Tasks support due dates and automatically highlight **overdue tasks**.

### 🎨 Modern UI

* Centered card layout
* Animated gradient background
* Hover animations
* Smooth task appearance animation

### 💾 Persistent Storage

All tasks are stored in an **SQLite database** so data remains saved after restarting the application.

---

# 🛠 Tech Stack

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Backend logic              |
| Flask      | Web framework              |
| SQLite     | Database                   |
| HTML       | Structure                  |
| CSS        | Styling & animations       |
| JavaScript | Frontend logic & API calls |

---

# 📂 Project Structure

```
OWLAITASK3/
│
├── app.py
├── tasks.db
├── README.md
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
│
└── task_manager.py
```

---

# ⚙ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install flask
```

---

# ▶ Running the Application

Run the Flask server:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

# 📸 Application Preview

Main features include:

* Adding tasks
* Completing tasks
* Priority sorting
* Search functionality
* Interactive UI

---

# 🎯 Future Improvements

Possible enhancements for the project:

* Edit existing tasks
* Drag and drop task ordering
* Task progress dashboard
* User authentication
* Dark mode theme

---

# 👨‍💻 Author

Developed by **Jeethesh**
Full Stack / Python Developer Project

---

# ⭐ License

This project is for **educational and portfolio purposes**.
