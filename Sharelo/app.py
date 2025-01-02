import streamlit as st
import qrcode
from PIL import Image
import io
import random
import string

# Simulating a backend content storage system (replace with real backend)
content_store = {}

def generate_unique_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Set page title and layout
st.set_page_config(page_title="Notepad with QR Code Generator", layout="wide")

# Title and description
st.title("Sharelo")
st.write("A simple text editor with the ability to generate QR codes for your content.")

# Text area (mimics the Notepad functionality)
text_area = st.text_area("Write your content here:", height=450)

# Buttons for functionalities
col1, col2, col3, col4 = st.columns(4)

with col1:
    save_button = st.button("Save Content")

with col2:
    load_button = st.file_uploader("Load Content", type=["txt"])

with col3:
    clear_button = st.button("Clear Content")

with col4:
    generate_qr_button = st.button("Generate QR Code")

# Save content to a file
if save_button and text_area:
    with open("notepad_content.txt", "w") as file:
        file.write(text_area)
    st.success("Content saved as 'notepad_content.txt'!")

# Load content from a file
if load_button:
    file_content = load_button.read().decode("utf-8")
    st.text_area("Write your content here:", value=file_content, height=300, key="loaded_text")

# Clear the text area
if clear_button:
    st.experimental_rerun()

# Generate QR Code for the text content
if generate_qr_button and text_area:
    # Generate a unique ID for the content
    unique_id = generate_unique_id()
    content_store[unique_id] = text_area  # Simulating backend storage

    # Generate a hosted URL for the content
    hosted_url = f"https://example.com/view?content_id={unique_id}"

    # Create QR code for the URL
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(hosted_url)
    qr.make(fit=True)

    # Create QR code image
    qr_img = qr.make_image(fill="black", back_color="white")
    buf = io.BytesIO()
    qr_img.save(buf)
    buf.seek(0)

    # Display the QR code
    st.image(buf, caption="Your QR Code (Scan to View Content)", width=200)
    st.markdown(f"[View your content here]({hosted_url})")

    # Provide download option for the QR code
    st.download_button(
        label="Download QR Code",
        data=buf,
        file_name="generated_qr_code.png",
        mime="image/png"
    )

# Note: Replace `https://example.com/view?content_id=` with your own hosting URL.
