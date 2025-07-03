# 📚 ONLINE EXAM PROCTORING & CHEAT DETECTION SYSTEM

An AI-powered proctoring tool designed for online examinations. It detects cheating behavior through real-time webcam monitoring, gaze tracking, tab switch alerts, and provides an invigilator dashboard for live monitoring.

![University Logo](/Cheat Detection In System and Web/static/SNPSU_logo2.png)

---

## ✅ Features

* Real-time webcam monitoring using MediaPipe
* Automatic face detection and absence logging
* Eye gaze detection (left/right tracking)
* Cheat flagging on multiple suspicious glances
* Tab switch detection (browser focus loss)
* Auto-submit when the exam timer ends
* Full-screen enforced exam interface
* Invigilator dashboard to monitor multiple students
* Cheat log viewer and CSV report generator
* Modern responsive UI with university branding
* **Multi-device support** – Run on two systems (student and invigilator) using the same IP address on the local network

---

## ⚒️ Technologies Used

* **Python 3.9+**
* **Flask** – Web framework
* **OpenCV** – Real-time video processing
* **MediaPipe** – Face and eye mesh detection
* **Socket.IO** – Real-time invigilation alerts
* **HTML5, CSS3, JavaScript**
* **Bootstrap** – Responsive design

---

## 📁 Project Structure

```
📁 Cheat Detection System
 ├ 📁 templates
 ┃ ├ 📄 index.html           # Student exam page
 ┃ └ 📄 invigilator.html     # Invigilator dashboard
 ├ 📁 static
 ┃ └ 📄 SNPSU_logo2.png      # University logo
 ├ 📄 app.py                 # Main Flask application
 ├ 📄 cheat_logs.txt         # Log file for cheat events
 └ 📄 requirements.txt       # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/May-nk/-ONLINE-EXAM-PROCTORING-CHEAT-DETECTION-SYSTEM.git
cd ONLINE-EXAM-PROCTORING-CHEAT-DETECTION-SYSTEM
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

### 4. Access in Browser

* **Student Interface** → [http://localhost:5000/](http://localhost:5000/)
* **Invigilator Panel** → [http://localhost:5000/invigilator](http://localhost:5000/invigilator)

### 🌐 Access from Another Device on Same Network

You can run the app on one system and access it from another using the local IP address:

* Replace `localhost` with your system's local IP (e.g., `192.168.1.10:5000`)
* Make sure both devices are on the same Wi-Fi/network

---

## 📋 Logs & Reports

* All cheating events are saved in `cheat_logs.txt`
* Use the **Download Report** button to export a `.csv` file
* Events include tab switching, missing face detection, and eye glances

---

## 🔒 Notes on Privacy

This tool is built for educational and demonstration purposes. Deployment in real-world settings requires:

* Informed consent from users
* Compliance with data protection regulations (e.g., GDPR, HIPAA)

---

## 💡 Future Enhancements

* Multi-student real webcam feeds
* Face recognition authentication
* Exam scheduler and tokenized access
* Chat module for student-invigilator communication
* Browser extension to enhance fullscreen enforcement

---

## 👨‍💼 Author

**Mayank**
B.Tech CSE @ Sapthagiri NPS University
GitHub: [@May-nk](https://github.com/May-nk)
Email: [your-email@example.com](mailto:rajwork006@gmail.com)

---

## 📜 License

This project is licensed for demo/educational use only.
