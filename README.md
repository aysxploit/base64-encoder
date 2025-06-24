# base64-encoder
Encode and decode string to and from base64 format

Base64 Encoder & Decoder (Python CLI Tool)
==========================================

A lightweight Python tool to encode and decode text strings and image files using Base64. 
Ideal for developers, students, and cybersecurity learners needing a simple encoder/decoder 
for text or image-based payloads.

Features
--------
- Encode plain text to Base64
- Decode Base64 back to plain text
- Encode images (e.g., PNG, JPG) to Base64
- Decode Base64 text back into an image file
- Built-in CLI – no external dependencies

How to Use
----------

1. Clone the Repository
-----------------------
git clone https://github.com/yourusername/base64-tool.git
cd base64-tool

2. Run the Script
-----------------
python base64tool.py --mode <mode> [--string "text"] [--file filename] [--input input.txt] [--output output.jpg]

Modes & Examples
----------------

Encode a Text String:
python base64tool.py --mode encode --string "Hello World"

Decode a Base64 String:
python base64tool.py --mode decode --string "SGVsbG8gV29ybGQ="

Encode an Image File:
python base64tool.py --mode encode_image --file image.png
> Saves output to image.png.b64.txt

Decode a Base64-Encoded Image File:
python main.py --mode decode_image --input image.png.b64.txt --output restored.png

Project Structure
-----------------
base64-tool/
├── base64tool.py        # Main script
├── README.txt           # This file
├── sample/
│   ├── image.png        # Sample image
│   ├── image.b64.txt    # Encoded Base64 text

Requirements
------------
- Python 3.6 or above
- No external libraries required

License
-------
All Rights Reserved
This code is proprietary. You may not copy, distribute, or reuse without the author’s explicit permission.

Disclaimer
----------
This tool is for educational purposes only. Base64 is not encryption and provides no actual data security. 
Do not use it to secure sensitive information.
