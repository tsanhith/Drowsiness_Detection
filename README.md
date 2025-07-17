<<<<<<< HEAD
Drowsiness Detection for Online Tutor Platform
This repository contains a project aimed at enhancing online tutoring platforms by implementing a drowsiness detection system. The system leverages the GoogleNet/Inception V3 model for image classification to monitor and detect drowsiness in real-time, ensuring a more engaging and effective learning experience.

Features
High Accuracy: The model achieves a training accuracy of 99.66% and a testing accuracy of 99.7%, ensuring reliable detection of drowsiness.
Real-Time Monitoring: Continuously monitors the user's facial expressions to detect signs of drowsiness during online tutoring sessions.
User-Friendly Interface: Easy-to-integrate system that can be seamlessly incorporated into existing online tutoring platforms.
Model Details
Architecture: GoogleNet/Inception V3, known for its efficiency and accuracy in image classification tasks.
Training Data: Extensive dataset of facial images labeled for drowsiness and alertness, ensuring robust model training.
Implementation: Implemented in Python with TensorFlow/Keras, enabling easy modification and extension.
=======
# Drowsiness Detection 🚗😴

Detect driver drowsiness in real-time using computer vision and machine learning.

---

## 🚀 Overview

This project monitors the driver’s eyes and alerts when signs of drowsiness are detected.  
It uses OpenCV and dlib for face and eye detection, alongside a simple alert mechanism.

---

## 🛠️ Features

- Real-time video feed analysis
- Eye aspect ratio calculation for blink/drowsiness detection
- Audible alarm on drowsiness
- Easy-to-use interface

---

## 📦 Setup

**Requirements:**  
- Python 3.7+
- OpenCV
- dlib
- imutils
- numpy
- scipy

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the application:**
```bash
python drowsiness_detector.py
```

---

## ✨ How It Works

- The system captures video from your webcam.
- Detects facial landmarks and calculates the Eye Aspect Ratio (EAR).
- If EAR falls below a threshold for a set time, triggers an alarm.

---

## 🧠 Algorithm

The project uses the Eye Aspect Ratio (EAR) algorithm to monitor eye closure:

```
EAR = (||p2 - p6|| + ||p3 - p5||) / (2 * ||p1 - p4||)
```
If EAR drops below a threshold, the driver is likely drowsy.

---

## ⚡ Customization

- Adjust EAR threshold and alarm duration in `drowsiness_detector.py`
- Replace or improve the alert sound
- Integrate with car systems or mobile devices

---

## 📚 References

- [OpenCV](https://opencv.org/)
- [dlib](http://dlib.net/)
- [Eye Aspect Ratio Paper](https://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf)

---

## 📄 License

MIT

---

*Made with ❤️ by tsanhith*
>>>>>>> 4e3563b03635434dc7760aed0af27608d6d77ee1
