
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

TARGET_CLASSES = {"person", "cat", "dog"}

@st.cache_resource
def get_model():
    # Load the model once and reuse it across Streamlit reruns.
    return YOLO("yolov8n.pt")

def detect_occupants(pil_image, confidence_threshold=0.35):
    model = get_model()

    results = model.predict(
        source=np.array(pil_image.convert("RGB")),
        conf=confidence_threshold,
        verbose=False
    )

    result = results[0]
    detections = []

    for box in result.boxes:
        class_id = int(box.cls[0].item())
        label = model.names[class_id]

        if label not in TARGET_CLASSES:
            continue

        detections.append({
            "label": label,
            "confidence": float(box.conf[0].item()),
            "box": [int(v) for v in box.xyxy[0].tolist()]
        })

    annotated = cv2.cvtColor(
        result.plot(),
        cv2.COLOR_BGR2RGB
    )

    return detections, annotated
