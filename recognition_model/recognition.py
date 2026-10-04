
from pathlib import Path
from urllib.request import urlretrieve

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image, ImageDraw, ImageFont
from transformers import pipeline

# 1. Create a folder for sample inputs
Path("samples").mkdir(exist_ok=True)

# 2. Download a sample photograph
image_path = "samples/sample_photo.jpg"

image_url = (
    "https://huggingface.co/datasets/"
    "huggingface/documentation-images/resolve/main/"
    "pipeline-cat-chonk.jpeg"
)

if not Path(image_path).exists():
    print("Downloading sample photograph...")
    urlretrieve(image_url, image_path)

# 3. Create a sample image containing text
text_image_path = "samples/sample_text.png"

if not Path(text_image_path).exists():
    img = Image.new("RGB", (700, 200), "white")
    draw = ImageDraw.Draw(img)

    draw.text(
        (30, 60),
        "Hello World! Python Recognition Project",
        fill="black"
    )

    img.save(text_image_path)

# 4. IMAGE RECOGNITION
print("\n" + "=" * 45)
print("IMAGE RECOGNITION")
print("=" * 45)

classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)

photo = Image.open(image_path).convert("RGB")
predictions = classifier(photo, top_k=3)

print("Input image:", image_path)
print("\nPredicted labels:")

for result in predictions:
    print(
        f"- {result['label']}: "
        f"{result['score'] * 100:.2f}%"
    )

# 5. TEXT RECOGNITION (OCR)
print("\n" + "=" * 45)
print("TEXT RECOGNITION (OCR)")
print("=" * 45)

# If Tesseract is not on PATH, uncomment and
# adjust this line for your installation:
# pytesseract.pytesseract.tesseract_cmd = (
#     r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# )

text_image = Image.open(text_image_path)
recognized_text = pytesseract.image_to_string(
    text_image,
    config="--psm 6"
)

print("Input image:", text_image_path)
print("\nRecognized text:")
print(recognized_text.strip() or "(No text detected)")

print("\nRecognition tasks completed.")
