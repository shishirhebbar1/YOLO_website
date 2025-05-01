import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO

# --- Page Config & Theme Settings ---
st.set_page_config(
    page_title="YOLO Object Detection",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Advanced UI ---
st.markdown("""
    <style>
    html, body, .stApp {
        /* soft indigo gradient */
        background: linear-gradient(135deg, #4B2E83 0%, #6C63FF 100%) !important;
        color: #FFF;
    }
    /* Main title styling */
    .main-title {
        color: #FFF;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.25rem;
    }
    /* Subtitle styling */
    .sub-title {
        color: #E0D7FF;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    /* Sidebar container override – now colored */
    section[data-testid="stSidebar"] {
        background: rgba(75, 46, 131, 0.85) !important;
        padding: 1rem;
        border-radius: 0.75rem;
    }
    /* Upload box placeholder */
    .upload-box {
        border: 2px dashed #E0D7FF;
        padding: 2rem;
        border-radius: 0.75rem;
        text-align: center;
        color: #333;
        font-size: 1rem;
        background-color: #FFFFFFDD;
        backdrop-filter: blur(4px);
    }
    </style>
""", unsafe_allow_html=True)


# Page Header (note the class names now match your CSS)
st.markdown('<div class="main-title">YOLO Object Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Select a YOLO model, upload an image, and visualize detections.</div>', unsafe_allow_html=True)

# Sidebar for model selection and upload
with st.sidebar:
    st.header("Settings")
    model_choice = st.radio(
        "Choose YOLO model:",
        ("YOLO on Pascal Dataset", "YOLO on Hardhat Dataset", "YOLO on Food Dataset"),
        index=1
    )
    weight_map = {
        "YOLO on Pascal Dataset": "yolo-pascal.pt",
        "YOLO on Hardhat Dataset": "yolo-hardhat.pt",
        "YOLO on Food Dataset":    "yolo-food.pt",
    }
    weight_path = weight_map[model_choice]

    uploaded_file = st.file_uploader(
        "Upload an image", type=["png", "jpg", "jpeg"],
        help="Upload a clear image for object detection"
    )

# Main content: Display loader and results
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    img_array = np.array(image)

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Input Image")
        st.image(image, use_column_width=True, caption="Original Image")

    with st.spinner(f"Loading model {model_choice}..."):
        model = YOLO(weight_path)

    with st.spinner("Detecting objects..."):
        results   = model(img_array)
        annotated = results[0].plot()

    with col2:
        st.subheader("Detected Objects")
        st.image(annotated, use_column_width=True, caption="Detections")

        # Object counts
        names, classes = results[0].names, results[0].boxes.cls.cpu().numpy()
        unique, counts = np.unique(classes, return_counts=True)
        count_dict = { names[int(u)]: int(c) for u, c in zip(unique, counts) }
        if count_dict:
            st.markdown("**Object Counts:**")
            for obj, cnt in count_dict.items():
                st.markdown(f"- {obj}: {cnt}")
        else:
            st.info("No objects detected.")
else:
    st.markdown(
        '<div class="upload-box">'
        'Choose a YOLO model in the sidebar, then upload an image to begin.'
        '</div>',
        unsafe_allow_html=True
    )
