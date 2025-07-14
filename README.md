Django Task Manager
A simple yet functional Task Manager web application built using the Django framework. This project allows users to create, view, update, and delete tasks with a user-friendly interface.

🚀 Features
Add new tasks with a title, description, and completion status

View all tasks on the homepage

Update task details

Delete tasks

Django admin panel integration

Clean UI using basic HTML templates

💻 Tech Stack
Backend: Python, Django

Frontend: HTML, CSS (optional for styling)

Database: SQLite

Tools: VS Code, Git, GitHub

📁 Project Structure
taskmanager_project/
├── taskmanager/
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── tasks/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── templates/
│ │ └── tasks/
│ │ └── task_list.html
│ └── ...
├── db.sqlite3
├── manage.py
└── venv/

🛠️ How to Run
Clone the repository

Create a virtual environment and activate it

Install Django using pip install django

Apply migrations using python manage.py makemigrations and python manage.py migrate

Run the development server using python manage.py runserver

🔐 Admin Access (Optional)
Create a superuser using python manage.py createsuperuser
Access the admin panel at: http://127.0.0.1:8000/admin

✅ Future Improvements
User login and authentication

Add due dates and priority tags

Improve UI using Bootstrap or Tailwind CSS

Deploy to cloud using Render or Vercel

📌 Author
Rachana AH
Built with love and learning ❤️
GitHub: https://github.com/Racchanah
