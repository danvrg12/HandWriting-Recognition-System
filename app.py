import streamlit as st
from pdf2image import convert_from_path
import os
import tempfile
import pytesseract
from PIL import Image

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Dania\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Streamlit app header
st.title("PDF to Image Converter with OCR")

# Let the user upload a PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded PDF to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        temp_pdf_path = temp_pdf.name  # Get the path of the temp file

    st.success("PDF uploaded successfully!")

    # Convert PDF to images
    st.write("Converting PDF to images...")
    try:
        pages = convert_from_path(temp_pdf_path, 300)

        # Create a directory to store the images
        output_dir = "output_images"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save and display the images
        for i, page in enumerate(pages):
            image_path = f"{output_dir}/page_{i + 1}.png"
            page.save(image_path, 'PNG')
            st.image(image_path, caption=f'Page {i + 1}', use_column_width=True)

            # Perform OCR on the saved image
            st.write(f"Extracting text from Page {i + 1} using OCR...")
            try:
                kan_text = pytesseract.image_to_string(Image.open(image_path), lang='kan')
                st.text_area(f"Extracted Text from Page {i + 1}:", value=kan_text, height=300)
            except Exception as ocr_error:
                st.error(f"An error occurred during OCR extraction: {ocr_error}")

        st.success(f"Conversion complete! {len(pages)} pages converted.")
    except Exception as e:
        st.error(f"An error occurred during conversion: {e}")
