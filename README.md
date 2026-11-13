# GuardianEye – AI-Powered In-Cabin Child & Pet Detection System

<p align="center">
  **Intelligent Vehicle Safety Monitoring Using Computer Vision and Edge AI**
</p>

<p align="center">
  ![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
  ![YOLO](https://img.shields.io/badge/AI-YOLO-red)
  ![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B)
  ![OpenCV](https://img.shields.io/badge/Computer%20Vision-OpenCV-green)
  ![Status](https://img.shields.io/badge/Status-Prototype-orange)
</p>

## Live Demo

**Try GuardianEye online:** [Launch GuardianEye](YOUR_STREAMLIT_APP_URL)

*The live demo link will be activated after deployment.*

## Overview

GuardianEye is an AI-powered in-cabin monitoring system designed to improve vehicle safety by detecting people and pets inside vehicles.

Using computer vision and deep learning, the system analyses cabin images, identifies supported occupants and evaluates potential safety risks based on occupancy, parking duration and cabin temperature.

The project combines YOLO-based object detection with a rule-based risk assessment engine to generate alerts when potentially unsafe conditions are identified.

GuardianEye is designed to evolve into a real-time vehicle monitoring solution integrating camera systems, mmWave radar and environmental sensors.

## Problem Statement

Children and pets can accidentally be left inside parked vehicles, exposing them to potentially dangerous cabin temperatures.

GuardianEye aims to address this problem through intelligent occupant detection, occupancy verification and risk assessment.

## Key Features

- **AI-Based Object Detection:** Identifies people, cats and dogs using YOLO.
- **Cabin Image Analysis:** Supports image uploads and camera capture.
- **Occupancy Monitoring:** Counts detected people and pets.
- **Confidence Scoring:** Displays individual object detection confidence.
- **Risk Assessment:** Evaluates occupancy, parking duration and cabin temperature.
- **Intelligent Alerts:** Generates LOW, MEDIUM and HIGH risk notifications.
- **Interactive Dashboard:** Provides an accessible Streamlit interface.

## How It Works

1. **Image Acquisition:** Captures or uploads an image of the vehicle cabin.
2. **Image Processing:** Converts the image into a suitable format.
3. **Object Detection:** YOLO identifies supported objects.
4. **Occupancy Analysis:** Calculates the number of detected people and pets.
5. **Risk Assessment:** Evaluates occupancy and environmental inputs.
6. **Alert Generation:** Displays the corresponding risk level and notification.

## System Architecture

```text
       CAMERA / IMAGE INPUT
                |
                v
       IMAGE PREPROCESSING
                |
                v
       YOLO OBJECT DETECTION
                |
                v
       OCCUPANCY ANALYSIS
                |
                v
       RISK ASSESSMENT ENGINE
                |
                v
          ALERT GENERATION
                |
                v
       STREAMLIT DASHBOARD
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| YOLO (Ultralytics) | Object detection |
| OpenCV | Image processing |
| NumPy | Numerical operations |
| Pillow | Image handling |
| Streamlit | Interactive dashboard |

## Project Structure

```text
GuardianEye/
│
├── app.py              # Main Streamlit application
├── detector.py         # YOLO object detection
├── alerts.py           # Risk assessment and alert logic
├── utils.py            # Utility functions
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── LICENSE             # MIT License
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/harshita0102/GuardianEye.git
```

### 2. Navigate to the project directory

```bash
cd GuardianEye
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python3 -m streamlit run app.py
```

Open the local application at:

`http://localhost:8501`

The pretrained YOLO model is downloaded automatically when first required.

## Risk Assessment

GuardianEye currently uses an explainable, rule-based scoring mechanism.

| Condition | Score Contribution |
|---|---:|
| Person detected | +35 |
| Pet detected | +35 |
| Radar confirmation input | +15 |
| Vehicle parked for at least 5 minutes with detected occupant | +10 |
| Cabin temperature ≥ 30°C | +10 |
| Cabin temperature ≥ 35°C | +25 |

The score is capped at 100.

| Risk Score | Risk Level |
|---|---|
| 0–29 | LOW |
| 30–59 | MEDIUM |
| 60–100 | HIGH |

These thresholds are prototype rules and are not validated automotive safety thresholds.

## Future Enhancements

- [ ] Real-time webcam-based occupant detection.
- [ ] Dedicated child-specific detection and classification.
- [ ] Improved pet detection.
- [ ] mmWave radar integration.
- [ ] Live cabin temperature monitoring.
- [ ] Camera and radar sensor fusion.
- [ ] Real-time emergency notifications.
- [ ] Buzzer and alarm integration.
- [ ] Raspberry Pi-based edge deployment.
- [ ] Model evaluation and performance optimisation.
- [ ] Cloud-hosted monitoring dashboard.

## Current Limitations

- The current YOLO model detects people, cats and dogs but cannot determine whether a detected person is a child.
- Radar and temperature readings are currently manual prototype inputs.
- Risk assessment uses demonstration rules rather than a validated safety model.
- The application currently processes uploaded or captured images rather than continuously monitoring a vehicle.
- Detection performance depends on lighting, image quality, occlusion and camera positioning.

**Safety Disclaimer:** GuardianEye is an experimental prototype and is not a certified vehicle safety system. It must not be used as the sole means of protecting children or pets.

## Developer

**Harshita Agarwal**

B.Tech – Computer Science & Engineering  
Specialization: IoT & Intelligent Systems

GitHub: [@harshita0102](https://github.com/harshita0102)

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

<p align="center">
  **GuardianEye – Making Every Journey Safer Through Intelligent Technology.**
</p>