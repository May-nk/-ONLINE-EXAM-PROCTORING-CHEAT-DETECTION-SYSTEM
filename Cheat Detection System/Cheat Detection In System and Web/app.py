import os
import csv
import time
import cv2
import platform
import threading
import mediapipe as mp
from flask import Flask, render_template, jsonify, Response, request, send_file

app = Flask(__name__)

# ✅ Logging Setup
LOG_FILE = "cheat_logs.txt"
event_log = []


# ✅ Eye direction counters
LEFT_COUNT = 0
RIGHT_COUNT = 0
CHEAT_FLAGGED = False

# ✅ Simulated Student Data (For Invigilator Panel Demo)
student_sessions = [
    {
        "name": "Student A",
        "id": "stu001",
        "video_url": "/video_feed",  # Reusing the same camera feed
        "alerts": ["Face Missing", "Tab Switch"]
    },
    {
        "name": "Student B",
        "id": "stu002",
        "video_url": "/video_feed",
        "alerts": ["Looking Away"]
    },
    {
        "name": "Student C",
        "id": "stu003",
        "video_url": "/video_feed",
        "alerts": []
    }
]

def log_event(event_type, message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [{event_type}] {message}"
    event_log.append(entry)
    if len(event_log) > 100:
        event_log.pop(0)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")  # ✅ Correct newline for Windows



# ✅ MediaPipe Setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)

# ✅ Webcam Frame Generator

# ✅ Webcam Frame Generator (with cooldown logic)
def generate_frames():
    global LEFT_COUNT, RIGHT_COUNT, CHEAT_FLAGGED

    cap = cv2.VideoCapture(0)
    prev_direction = None
    cooldown_frames = 0

    try:
        while True:
            success, frame = cap.read()
            if not success:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(frame_rgb)

            if not results.multi_face_landmarks:
                log_event("Face Missing", "Face not detected in the frame.")
                prev_direction = None
                cooldown_frames = 0
            else:
                for face_landmarks in results.multi_face_landmarks:
                    left_eye_x = face_landmarks.landmark[33].x
                    right_eye_x = face_landmarks.landmark[263].x
                    nose_x = face_landmarks.landmark[1].x

                    direction = None
                    if left_eye_x < nose_x - 0.03:
                        direction = "LEFT"
                    elif right_eye_x > nose_x + 0.03:
                        direction = "RIGHT"

                    if cooldown_frames == 0 and direction and direction != prev_direction:
                        if direction == "LEFT":
                            LEFT_COUNT += 1
                            log_event("Quick eye glance: LEFT", f"Left Count = {LEFT_COUNT}")
                        elif direction == "RIGHT":
                            RIGHT_COUNT += 1
                            log_event("Quick eye glance: RIGHT", f"Right Count = {RIGHT_COUNT}")

                        prev_direction = direction
                        cooldown_frames = 15  # Wait 15 frames before next valid count

                    if cooldown_frames > 0:
                        cooldown_frames -= 1

                    if LEFT_COUNT + RIGHT_COUNT >= 5 and not CHEAT_FLAGGED:
                        CHEAT_FLAGGED = True
                        log_event("DEBUG", "Frame processed")


            # Frame encoding
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    finally:
        cap.release()

# 🌐 Flask Routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/status')
def get_status():
    return jsonify({"status": "Running", "alerts": event_log[-5:]})

@app.route('/log_tab_switch', methods=['POST'])
def log_tab_switch():
    log_event("Tab Switch", "User switched window or lost browser focus.")
    return '', 204

@app.route('/timer_expired')
def timer_expired():
    log_event("Timer Ended", "Exam duration completed.")
    return jsonify({"message": "Timer expired logged."})

@app.route('/invigilator')
def invigilator_dashboard():
    return render_template('invigilator.html', students=student_sessions)

# ✅ Report Download (CSV) — Windows-safe
@app.route('/download_report')
def download_report():
    csv_file = "cheat_report.csv"

    with open(LOG_FILE, "r") as log_file, open(csv_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Event Type", "Description"])
        for line in log_file:
            try:
                if "] [" in line:
                    parts = line.strip().split("] [")
                    timestamp = parts[0].replace("[", "")
                    event_type, message = parts[1].split("] ")
                    writer.writerow([timestamp, event_type.strip(), message.strip()])
                else:
                    writer.writerow([line.strip()])
            except:
                pass

    response = send_file(csv_file, as_attachment=True)

    def delayed_delete(path):
        def delete():
            time.sleep(2)
            try:
                os.remove(path)
            except Exception as e:
                print(f"Failed to delete file: {e}")
        threading.Thread(target=delete).start()

    delayed_delete(csv_file)
    return response

# 🚀 Run the app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
