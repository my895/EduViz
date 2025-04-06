## 🧠 **EduVision** — Smart Classroom Automation Suite

### ⚡ Real-Time Attendance · Smart Alerts · Intelligent Resource Management

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_App-000000?style=flat&logo=flask)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=flat&logo=postgresql)](https://www.postgresql.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?style=flat&logo=opencv)](https://opencv.org/)

---

### 🔍 Description

**EduVision** is a Flask-based smart classroom system that leverages **computer vision** and **automated alerting** to digitize and streamline classroom workflows.

Designed for educational institutions, it offers:
- **Real-time face recognition** for attendance tracking.
- **Instant emergency alert dispatch** (e.g., SMS/Email).
- **Backend resource and session management** via PostgreSQL.

---

### 💡 Core Features

- 🧑‍💼 **Face-based Attendance**  
  Fast, secure, and hands-free student authentication using OpenCV.

- 🚨 **Emergency Notification System**  
  Trigger alerts via web dashboard for fire drills, intrusions, or system malfunctions.

- 📊 **Smart Admin Dashboard**  
  Tracks attendance logs, classroom activity, and alerts in real-time.

- 🌐 **Responsive Web UI**  
  Clean frontend built using HTML, CSS, and JavaScript.

---

### ⚙️ Tech Stack

| Layer       | Tech Used |
|-------------|-----------|
| **Backend** | Python · Flask |
| **Frontend** | HTML · CSS · JavaScript |
| **Database** | PostgreSQL |
| **CV Engine** | OpenCV · dlib |
| **Comms** | Flask-Mail · SMTP |
| **Security** | Role-based access + input validation |

---

### 🚀 Getting Started

```bash
# Clone repository
git clone https://github.com/xprilion/SmartClassroom.git
cd SmartClassroom

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Flask App
export FLASK_APP=app.py
flask run
```

✅ PostgreSQL should be up and running. Configure your DB URI inside `config.py`.

---

### 🧠 Face Recognition Setup

1. Place face images of students in a designated folder (e.g., `faces/`).
2. Each image must be named after the student (e.g., `john_doe.jpg`).
3. System detects, encodes, and maps to student entries on first run.

---

### 🛰️ Future Scope

- ✨ Integration with **IoT devices** for auto door-lock systems.
- 📱 Companion **Mobile App** for real-time attendance view.
- 🔐 JWT-based **Auth API** for secure third-party extensions.


---

### 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
