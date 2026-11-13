import streamlit as st
import time
from PIL import Image
from detector import detect_occupants
from alerts import assess_risk, build_alert
from utils import image_to_bytes

st.set_page_config(page_title="GuardianEye", page_icon="🚗", layout="wide")
st.title("🚗 GuardianEye")
st.caption("Edge AI In-Cabin Occupant & Pet Detection — prototype dashboard")

with st.sidebar:
    st.header("Vehicle inputs")
    radar_present = st.toggle("Radar confirms occupancy (prototype input)", value=False)
    vehicle_parked = st.toggle("Vehicle is parked", value=True)
    parked_minutes = st.number_input("Time parked (minutes)", min_value=0, value=10, step=1)
    cabin_temp = st.number_input("Cabin temperature (°C)", min_value=-10.0, max_value=80.0, value=28.0, step=0.5)
    st.caption("Radar and temperature are manual prototype inputs. Connect hardware for live readings.")

uploaded = st.file_uploader("Upload an in-cabin image", type=["jpg", "jpeg", "png"])
camera_image = st.camera_input("Or capture an image using your camera")

image_file = uploaded if uploaded is not None else camera_image

if image_file:
    image = Image.open(image_file).convert("RGB")
    left, right = st.columns([1, 1])
    with left:
        st.subheader("Cabin image")
        st.image(image, use_container_width=True)

    with st.spinner("Analysing image with YOLO..."):
        detections, annotated = detect_occupants(image)

    people = sum(1 for d in detections if d["label"] == "person")
    pets = sum(1 for d in detections if d["label"] in ("cat", "dog"))
    risk = assess_risk(
        people=people,
        pets=pets,
        radar_present=radar_present,
        vehicle_parked=vehicle_parked,
        parked_minutes=parked_minutes,
        cabin_temp=cabin_temp
    )
    alert = build_alert(risk)

    with right:
        st.subheader("Detection output")
        st.image(annotated, caption="YOLO detections", use_container_width=True)
        st.metric("People detected", people)
        st.metric("Pets detected", pets)
        st.metric("Detection count", len(detections))
        if detections:
            st.dataframe(
                [{"Object": d["label"], "Confidence": f'{d["confidence"]:.1%}'} for d in detections],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("No supported objects detected.")

    st.divider()
    st.subheader("Risk assessment")
    c1, c2, c3 = st.columns(3)
    c1.metric("Risk level", risk["level"])
    c2.metric("Risk score", f'{risk["score"]}/100')
    c3.metric("Cabin temperature", f'{cabin_temp:.1f} °C')
    st.progress(risk["score"] / 100)
    if alert["level"] == "HIGH":
        st.error(alert["message"])
    elif alert["level"] == "MEDIUM":
        st.warning(alert["message"])
    else:
        st.success(alert["message"])

    st.caption("Prototype only: this dashboard is not a certified vehicle safety system. Never rely on it as the sole means of protecting an occupant.")
else:
    st.info("Upload or capture an image to begin detection.")
    st.markdown("""
    **How to test**
    1. Install the requirements.
    2. Run `streamlit run app.py`.
    3. Upload a cabin image containing a person, cat or dog.
    4. Change the radar, parked-time and temperature inputs to test alert levels.
    """)
