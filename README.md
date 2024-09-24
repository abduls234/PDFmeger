# PDF Merger in Python

This project demonstrates a simple Python script for merging multiple PDF files into a single document. Using the `PyPDF2` library, the script reads two PDF files and combines them into a single output PDF.

## Features:
- Merges multiple PDF files into one
- Utilizes `PyPDF2` for efficient PDF manipulation
- Simple and easy-to-understand Python code

## How it works:
1. The script takes a list of PDF file names.
2. It reads each file using `PyPDF2.PdfReader()`.
3. The files are merged into a single document using `PyPDF2.PdfFileMerger()`.
4. The merged output is saved as `merged.pdf`.

## Requirements:
- Python 3.x
- `PyPDF2` library

You can install `PyPDF2` using pip:
```bash
pip install PyPDF2
