# 🎓 AI-Based Attendance System using Face Recognition

## 📌 Project Overview

This project is an AI-based attendance system that uses face recognition to automatically mark attendance. It reduces manual work and improves accuracy using computer vision.

---

## 🚀 Features

* Face Registration (Capture Images)
* Face Training using LBPH Algorithm
* Automatic Attendance using Webcam
* Subject-wise Attendance Tracking
* Monthly Attendance Reports
* Overall Attendance Percentage
* Dashboard with Filters (Search by Name/ID)
* Graphical Representation (Pie Charts)
* User-friendly GUI Interface

---

## 🛠️ Technologies Used

### 🎨 Frontend

* Python Tkinter (GUI)
* React + TypeScript (.tsx files for UI components)

### ⚙️ Backend

* Python
* OpenCV (Face Detection)
* dlib & face-recognition (Face Recognition)
* Pandas (Data Processing)
* CSV Files (Data Storage)

---

## 🤖 Working Flow

1. Register student (capture face images)
2. Images stored in dataset folder
3. Train model using LBPH algorithm
4. Model saved as `Trainner.yml`
5. Webcam detects face
6. Face matched with trained data
7. Attendance marked automatically
8. Data stored in CSV files
9. Dashboard shows reports (overall, monthly, subject-wise)

---

## 🧠 Algorithms Used

* Haar Cascade Classifier → Face Detection
* LBPH (Local Binary Patterns Histogram) → Face Recognition

---

## 📊 Why This System?

* Saves time (no manual attendance)
* Prevents proxy attendance
* Accurate and fast
* Easy report generation
* Useful for colleges & offices

---

## ⚠️ Note

This project cannot be deployed on platforms like Vercel because it requires webcam access. It should be run locally.

---

## 👩‍💻 Team Members

* Janvi – Model Training & Backend Logic
* Nandini – Frontend UI
* Sudhesna – Data Handling & Integration

