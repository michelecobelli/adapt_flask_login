# 🧠 ADAPT.ai — User-Personalized Project Platform (Flask + Figma Integration)

ADAPT.ai is a full-stack web application designed to give each user their own personalized dashboard where they can log in, register, and write a custom description of their design project.

The visual interface is based on a Figma-designed static prototype, which has been carefully transformed into a fully dynamic Flask application without compromising layout or styling.

---

## 🚀 Features

- 🔐 **User Authentication** (Sign up, login, logout)
- 📄 **Per-User Project Description** stored in the database
- 🎨 **Fully Styled Pages from Figma** with automatic screen resizing
- 🧠 **Session-based Personalization** (Shows each user’s first name)
- 🔁 **Logout System** that clears session and returns to landing page

---

## 📁 Folder Structure

```
adapt_flask_project/
├── app.py
├── config.py
├── /models/
│   └── user.py
├── /templates/
│   ├── user_landing.html
│   ├── sign_up.html
│   ├── log_in.html
│   └── main_page_user.html
├── /static/
│   └── /css/
│       ├── user_landing.css
│       ├── sign_up.css
│       ├── log_in.css
│       └── main_page_user.css
├── app.db (generated after first run)
├── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/adapt-ai.git
cd adapt-ai
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

The app will run at:

```
http://127.0.0.1:5000/
```

---

## 📌 Usage Flow

- Visit `/` to access the landing page
- Click **Start Using Adapt** → go to **Sign Up**
- Click **Get Started** → go to **Login**
- After login/signup, you're taken to `/dashboard`
- Write and save a **project description** — it will be saved per user
- Click **EXIT** to log out and return to home

---

## 🛠 Tech Stack

- Python 3 + Flask
- Flask-SQLAlchemy
- HTML/CSS (from Figma)
- Jinja Templating
- SQLite (local DB)

---

## ✅ Status

This project is fully functional and ready to expand. Possible future upgrades include:
- Flash messages for feedback
- Support for multiple projects per user
- Flask-Migrate for schema updates
- User profile editing

---

## 📄 License

MIT License — free to use and adapt.

---

## 👤 Created By

**Your Name / Team**  
📫 Reach out via GitHub or email
