# 🎓 Online Exam Cheat Detection System

An AI-powered proctoring tool that detects and logs cheating behavior during online exams using real-time webcam monitoring, gaze detection, and tab switch tracking.

![Logo](static/SNPS_Logo.png)

---

## 📌 Features

* ✅ Real-time webcam monitoring using MediaPipe
* ✅ Automatic face presence detection
* ✅ Eye gaze detection (left/right movement)
* ✅ Auto-flag if student looks left/right 5 or more times
* ✅ Tab switch detection (focus lost tracking)
* ✅ Auto-submission when exam time ends
* ✅ Full-screen enforced exam mode
* ✅ Live invigilator dashboard (powered by Socket.IO)
* ✅ Cheat activity logs downloadable in `.csv` format
* ✅ Custom university branding and modern responsive UI

---

## 🔧 Technologies Used

* **Python 3.9+**
* **Flask** – Web framework
* **OpenCV** – Webcam video capture
* **MediaPipe** – Face mesh and eye tracking
* **Socket.IO** – Real-time invigilation alerts
* **HTML5, CSS3, JavaScript**
* **Bootstrap** – Responsive UI framework

---

## 📂 Project Structure

```bash
📁 Cheat Detection System
 ┣ 📁 templates
 ┃ ┣ 📄 index.html
 ┃ ┗ 📄 invigilator.html
 ┣ 📁 static
 ┃ ┗ 📄 SNPS_Logo.png
 ┣ 📄 app.py
 ┣ 📄 cheat_logs.txt
 ┗ 📄 requirements.txt
```

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/May-nk/Online-Cheat-Detector-main.git
cd Online-Cheat-Detector-main/Cheat Detection System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

* **Student View** → [http://localhost:5000/](http://localhost:5000/)
* **Invigilator Dashboard** → [http://localhost:5000/invigilator](http://localhost:5000/invigilator)

---

## 📝 Report & Logging

* All cheat events are saved in `cheat_logs.txt`
* Download the full cheat report in `.csv` format from the UI using the **Download Report** button

---

## 💡 Future Improvements

* Support for multiple student webcams
* Face recognition for authentication
* Remote exam scheduling panel
* Invigilator-student chat communication system
* Stronger fullscreen enforcement via browser extension

---

## 👨‍💻 Author

**Mayank**
B.Tech CSE @ Sapthagiri NPS University
GitHub: [@May-nk](https://github.com/May-nk)
Email: [your-email@example.com](mailto:rajwork006@gmail.com)

---

## 📜 License

This project is intended for educational and demo purposes only. For real-world deployment, ensure compliance with relevant privacy and data protection regulations (e.g., GDPR, HIPAA).
