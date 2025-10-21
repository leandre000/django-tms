# 🧩 Task Management System (TMS)

A lightweight **Task Management System (TMS)** built with **Django** and **Tailwind CSS**.  
It helps teams and individuals create, assign, and track tasks with simplicity and speed.

---

## 🚀 Features
- 🔐 User authentication (login, register, logout)
- 📋 Task CRUD (create, update, delete, view)
- 🗂️ Project-based task grouping
- 🕓 Deadlines & priorities
- 📊 Simple dashboard with task stats
- 🌐 Clean Tailwind-powered responsive UI

---

## 🛠️ Tech Stack
- **Backend:** Django 5+
- **Frontend:** Tailwind CSS
- **Database:** SQLite (default)
- **Auth:** Django built-in authentication

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/tms-django.git
cd tms-django

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (admin)
python manage.py createsuperuser

# 6. Start development server
python manage.py runserver
