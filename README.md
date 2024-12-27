# CS50 AI Nepal Attendance System

Welcome to the **CS50 AI Nepal Attendance System**, an initiative by the CS50xNepal team to streamline participant tracking and engagement in our educational programs. This platform is a Nepali adaptation of Harvard University's CS50 Artificial Intelligence course, tailored to bring world-class AI education to Nepal.

---

## 🌟 Features
- Participant attendance tracking
- User-friendly interface
- Secure authentication
- Scalable and efficient design
- Built using the Django framework

---

## 🛠️ Tech Stack
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript (optional enhancements)
- **Database**: SQLite (default) or any supported by Django
- **Version Control**: Git

---

## 🚀 Steps to Run the Project

### 1. Clone the Repository
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/yourusername/cs50-ai-nepal-attendance.git
cd cs50-ai-nepal-attendance
```

---

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

---

### 3. Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables (Optional)
If your project uses environment variables for sensitive data (like database credentials), create a `.env` file in the root directory and configure it accordingly:
```plaintext
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `DB_SSLMODE`
```

---

### 5. Apply Database Migrations
Set up the database by running migrations:
```bash
python manage.py migrate
```

---

### 6. Create a Superuser (Optional)
To access the Django admin panel, create a superuser:
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

---

### 7. Collect Static Files (Optional for Production)
If you plan to deploy the application, collect the static files:
```bash
python manage.py collectstatic
```

---

### 8. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

---

### 9. Access the Application
Open your web browser and navigate to:
- **Homepage**: `http://127.0.0.1:8000`
- **Admin Panel**: `http://127.0.0.1:8000/admin`

---

## 📂 Project Structure
```plaintext
cs50-ai-nepal-attendance/
├── attendance/          # Core attendance app
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
├── db.sqlite3           # Default SQLite database
└── venv/                # Virtual environment (optional, not committed)
```

---

## 🤝 Contributing
We welcome contributions to improve this platform!  
To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## ✨ Acknowledgments
Special thanks to:
- **Harvard University** for the [CS50 AI course](https://cs50.harvard.edu/ai/2020/)
- **CS50xNepal** for their dedication to bringing AI education to Nepal
