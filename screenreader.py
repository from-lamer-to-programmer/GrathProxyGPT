import pytesseract
from PIL import ImageGrab
# Set the path to the Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Take a screenshot of the screen
screenshot = ImageGrab.grab()
# Convert the screenshot to grayscale
screenshot = screenshot.convert('L')
# Use pytesseract to extract text from the screenshot
text = pytesseract.image_to_string(screenshot)
# Print the extracted text
print(text)