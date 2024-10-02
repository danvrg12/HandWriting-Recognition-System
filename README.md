# PDF to Image Converter with OCR for Kannada Handwritten Text

This project was developed as part of a hackathon for **Freethought Labs (OPC) Pvt Ltd** in collaboration with the **Department of Computer Science, Christ (Deemed to be University)**. The goal is to build a system that converts PDF files containing handwritten Kannada text into images and performs Optical Character Recognition (OCR) to extract text.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [OCR Results](#ocr-results)
- [Known Issues](#known-issues)
- [Future Work](#future-work)
- [License](#license)

## Overview
This Streamlit-based web application allows users to upload PDF files and convert each page to an image. The system uses `pytesseract` to perform Optical Character Recognition (OCR) on each image, specifically handling Kannada text.

### Objectives
- Convert PDFs with handwritten Kannada text to images.
- Extract Kannada text using OCR from each page.
- Provide a user-friendly interface to view images and extracted text.

## Features
- **PDF Upload**: Users can upload multi-page PDF files.
- **Image Conversion**: Each page of the PDF is converted to a high-resolution image.
- **OCR Extraction**: `pytesseract` is used to extract Kannada text from the images.
- **Real-Time Display**: Users can view the images and extracted text directly in the browser.
- **Error Handling**: Gracefully handles errors during file upload, PDF conversion, and OCR extraction.

## Setup Instructions

### Prerequisites
- Python 3.x
- Tesseract OCR (Make sure Tesseract is installed on your system)
    - Download Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
    - Ensure that `pytesseract.pytesseract.tesseract_cmd` is correctly set to the Tesseract executable path in the script.
- Streamlit
- PIL (Python Imaging Library)
- pdf2image

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/pdf-kan-ocr.git
   cd pdf-kan-ocr
2. Install the required dependencies:
 
    `pip install -r requirements.txt` 

### Install Tesseract OCR
- For Windows, download the installer from [here](https://github.com/tesseract-ocr/tesseract/releases).
- Set the path to `tesseract.exe` in your script, e.g., `r'C:\path\to\tesseract.exe'`.

### Configuration
Ensure `pytesseract.pytesseract.tesseract_cmd` is set to your Tesseract installation path in the script:

`pytesseract.pytesseract.tesseract_cmd = r'C:\path\to\tesseract.exe'`

### Run the App
To start the application, use Streamlit:

` streamlit run app.py`

### Usage
  - Upload a PDF file containing handwritten Kannada text.
  - The system will automatically convert each page to an image.
  - Extracted text will be displayed alongside the images in real-time.
  - Review the extracted Kannada text in the text areas provided for each page.

### OCR Results
  - The current system uses the pytesseract library with the Kannada language model (lang='kan'). While it works well for some text, you may notice:

    - Noise Handling: The system does not currently pre-process noisy PDFs, so you may get poor OCR results for heavily corrupted data.
    - Multi-Column Handling: Bonus points can be earned by improving this feature in future work.

### Future Work : 
  
  - Implement noise reduction techniques to improve OCR accuracy for noisy handwritten text.
  - Improve the handling of multi-column PDF layouts.
  - Explore alternative OCR engines or fine-tune the Kannada OCR model for better accuracy.
    
### License :
This project is licensed under the GPLv3 License.
