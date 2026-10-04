# Image and Text Recognition

A Python-based image and text recognition project developed as part of my Decode Labs internship.

## Features

- **Image Recognition:** Uses a pretrained Vision Transformer (ViT) model through Hugging Face Transformers to predict image categories.
- **Text Recognition (OCR):** Uses Tesseract OCR through `pytesseract` to extract text from images.
- **Sample Images:** Includes example images to test both recognition tasks.
- **Prediction Scores:** Displays the top predicted image labels with their confidence scores.

## Project Structure

```text
Decodelab-internships/
├── recognition_model/
│   ├── recognition.py
│   ├── requirements.txt
│   └── README.md
├── samples/
│   ├── sample_photo.jpg
│   └── sample_text.png
└── .gitignore
```

## Technologies Used

- Python
- Hugging Face Transformers
- PyTorch
- Pillow
- Pytesseract
- Tesseract OCR

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/banahanshika/Decodelab-internships.git
cd Decodelab-internships
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Python dependencies

```powershell
python -m pip install -r recognition_model/requirements.txt
```

### 4. Install Tesseract OCR

Install Tesseract OCR for Windows using the [UB Mannheim Tesseract installer page](https://github.com/UB-Mannheim/tesseract/wiki).

If Tesseract is installed in the default location, configure its executable path in `recognition.py`:

```python
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
```

Adjust the path if Tesseract is installed elsewhere.

## Run the Project

From the repository root:

```powershell
python recognition_model/recognition.py
```

The script uses the sample images in the `samples/` directory. The pretrained image recognition model may download its model files the first time it runs.

## Sample Output

### Image Recognition

The model predicts image categories and displays their scores.

Example categories from the sample run:

- Lynx / catamount
- Cougar / mountain lion
- Snow leopard

These are model predictions, not guaranteed identifications.

### Text Recognition (OCR)

Example extracted text:

```text
Hello World! Python Recagnition Project
```

OCR output can contain spelling errors depending on image quality and text layout.

## Learning Outcomes

- Working with pretrained computer vision models
- Understanding image classification and prediction scores
- Extracting text from images using OCR
- Managing Python dependencies and virtual environments
- Organizing and documenting a machine learning project

## Future Improvements

- Improve OCR accuracy with image preprocessing
- Allow users to provide their own image paths
- Save recognition results to a text file
- Build a simple web interface for image uploads

## Author

**Hanshika Bana**

Developed as part of my Decode Labs internship.
