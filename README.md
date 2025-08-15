### 🗂️ Project: Todo — A Minimalistic & Rewarding To-Do List App

Welcome to Todo List, a lightweight and beautiful task management web application built with Flask and styled using Bootstrap. Designed to be minimal yet rewarding, MyTodo not only helps you keep track of your daily tasks but also celebrates your productivity with a fun Mario animation when all your tasks are complete. 🎉

Whether you're a student organizing your studies, a developer managing your side projects, or just someone looking to keep life in order, MyTodo is a clean, no-login-needed, local task tracker that runs right from your browser.

---

## 🌐 Live Demo

🚀 Try the app here: [https://todo-list-8gob.onrender.com](https://todo-list-8gob.onrender.com)

[![Live on Render](https://img.shields.io/badge/Live-Demo-green?style=flat&logo=render)](https://todo-list-8gob.onrender.com)


---

## ✨ Features

✅ Add New Tasks – Quickly add to-dos with a simple form.

🔁 Toggle Completion – Mark tasks as done or undone with a checkbox.

🗑️ Delete Tasks – Clean your list by deleting tasks.

🎉 All Tasks Done? You Win! – Celebrate with a Mario animation once all tasks are complete.

💻 Responsive UI – Built with Bootstrap to look good on both desktop and mobile.

⚡ Fast and Lightweight – No databases, no external services, no bloat.

---

## 🚀 Why I Built This

This app was born out of the desire to:

Build a complete web app from scratch using Flask

Learn about routing, form handling, and templating with Jinja2

Create a satisfying user experience that adds a fun twist to productivity

Unlike most to-do list apps that sync to the cloud, this project focuses on local-only simplicity — ideal for beginners or quick personal use.

---

## 🔧 Technologies Used

Python 3 – Backend logic

Flask – Web framework

HTML5 + Jinja2 – Template rendering

Bootstrap 5 – Layout, responsiveness, and form components

Font Awesome – Icons for delete and check functionality

CSS3 – Custom styling

---

## 🏗️ How It Works

Your task list is stored in a simple Python list (todo_list[]) in memory. Each task is a dictionary:

{"task": "Buy groceries", "done": False}


When a user submits a new task, it’s added to the list.

Checking a task toggles its 'done' state.

Deleting removes the task from the list.

All changes are reflected instantly and only for the current session.

⚠️ Note: The data is not saved permanently. It disappears when the server restarts.

---

## ⚙️ Deployment

This project is deployed using [Render](https://render.com). To deploy your own version:

1. Fork or clone the repository.
2. Push it to your own GitHub repo.
3. Create a new **Web Service** on Render.
4. Use this build and start command:

   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn main:app`

---

## 🙋‍♀️ Contributing

Contributions are welcome! Feel free to submit issues or pull requests. Whether it’s bug fixes, improvements, or new features — all are appreciated.
