import streamlit as st
import qrcode
from PIL import Image
import io

# Set page title and layout
st.set_page_config(page_title="Simple QR Code Generator", layout="wide")

# Title and description
st.title("Sharelo - Simple QR Code Generator")
st.write("Enter your content below, and generate a QR code that can be scanned easily.")

# Text area for content input
text_area = st.text_area("Write your content here:", height=200)

# Button to generate QR code
generate_qr_button = st.button("Generate QR Code")

# Generate and display QR Code
if generate_qr_button and text_area:
    # Create a QR code with better scan-ability
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=12,  # Larger boxes make the QR code more scan-able
        border=6  # Increased border for better clarity
    )
    qr.add_data(text_area)
    qr.make(fit=True)

    # Create QR code image
    qr_img = qr.make_image(fill="black", back_color="white")
    
    # Save image to buffer
    buf = io.BytesIO()
    qr_img.save(buf)
    buf.seek(0)

    # Display QR code
    st.image(buf, caption="Your Easy-to-Scan QR Code", width=300)

    # Provide download option for the QR code
    st.download_button(
        label="Download QR Code",
        data=buf,
        file_name="generated_qr_code.png",
        mime="image/png"
    )
