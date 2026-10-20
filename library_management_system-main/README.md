# 📚 Library Management System

A simple and modern **Library Management System** built with Django.

Designed as a learning project to practice Django fundamentals, authentication, models, relationships, forms, CRUD operations, and template inheritance.

---

## ✨ Features

* 🔐 User Registration & Login
* 📚 Browse Books
* ✍️ Manage Authors
* 🏷️ Manage Categories
* ➕ Add Books
* ✏️ Update Books
* 🗑️ Delete Books
* 📖 Borrow Books
* 🔄 Return Books
* 🖼️ Book Cover Images
* 👤 User Accounts
* 📱 Responsive Design

---

## 🛠️ Built With

* 🐍 Python
* 🌿 Django
* 🎨 HTML & CSS
* 🅱️ Bootstrap
* 🗄️ SQLite
* 🖼️ Pillow

---

## 📂 Project Structure

```text
Library_Management_System/
│
├── config/
│   └── Project configuration
│
├── main/
│   └── Home, About & Contact
│
├── accounts/
│   └── Registration, Login & Logout
│
├── library/
│   └── Books, Authors, Categories & Borrow Records
│
├── templates/
│   ├── base.html
│   ├── nav.html
│   ├── foot.html
│   └── ...
│
├── manage.py
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Go to the project directory

```bash
cd Library_Management_System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

## 🧩 Main Models

The project currently includes:

```text
👤 User
   │
   └── Borrow Records
          │
          └── 📚 Book
                ├── ✍️ Author
                └── 🏷️ Category
```

---

## 🌱 Learning Goals

This project is being developed to strengthen practical Django skills, including:

* Django project & app structure
* Custom User Model
* Authentication
* Model Relationships
* Model Forms
* CRUD Operations
* File Uploads
* Template Inheritance
* URL Routing
* Authentication Protection
* Database Management

---

## 💜 Project Status

🚧 **Currently in development**

More features and improvements will be added as the project grows.

---

## 👩‍💻 Author

Made with 💜 and lots of ☕ while learning Django.

**Radia Mahbub**

---

### ⭐ If you like this project

Feel free to explore the code, learn from it, and build something of your own!

> **Learn → Build → Break → Fix → Repeat.** 🐍✨
