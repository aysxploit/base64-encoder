"""
🔐 Base64 Encoder & Decoder (Python CLI Tool)
Author: aysxploit
License: All Rights Reserved – Do not distribute or reuse without permission.
"""

import base64
import argparse
import os

def encode_string(text):
    return base64.b64encode(text.encode()).decode()

def decode_string(b64_text):
    try:
        return base64.b64decode(b64_text.encode()).decode()
    except Exception as e:
        return f"[Error] Invalid Base64 string: {e}"

def encode_image(file_path):
    try:
        with open(file_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        output_path = file_path + ".b64.txt"
        with open(output_path, "w") as out:
            out.write(encoded)
        return f"Image encoded and saved to {output_path}"
    except Exception as e:
        return f"[Error] Could not encode image: {e}"

def decode_image(input_path, output_path):
    try:
        with open(input_path, "r") as f:
            encoded_data = f.read()
        with open(output_path, "wb") as out:
            out.write(base64.b64decode(encoded_data.encode()))
        return f"Image decoded and saved to {output_path}"
    except Exception as e:
        return f"[Error] Could not decode image: {e}"

def main():
    parser = argparse.ArgumentParser(description="Base64 Encoder & Decoder Tool")
    parser.add_argument("--mode", required=True, help="encode / decode / encode_image / decode_image")
    parser.add_argument("--string", help="Text string to encode or decode")
    parser.add_argument("--file", help="File path to encode (image)")
    parser.add_argument("--input", help="Input .txt file for image decoding")
    parser.add_argument("--output", help="Output image file path for decoded image")

    args = parser.parse_args()

    if args.mode == "encode" and args.string:
        print(encode_string(args.string))
    elif args.mode == "decode" and args.string:
        print(decode_string(args.string))
    elif args.mode == "encode_image" and args.file:
        print(encode_image(args.file))
    elif args.mode == "decode_image" and args.input and args.output:
        print(decode_image(args.input, args.output))
    else:
        print("[Error] Invalid arguments. Use --help for usage.")

if _name_ == "_main_":
    main()