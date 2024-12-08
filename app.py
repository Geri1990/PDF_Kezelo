
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(output_path, *input_paths):
    writer = PdfWriter()
    for path in input_paths:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    print(f"PDF-ek összefűzve: {output_path}")

if __name__ == "__main__":
    # Példa használatra
    merge_pdfs("output.pdf", "file1.pdf", "file2.pdf")

    from PyPDF2 import PdfReader


def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        print(page.extract_text())

# Példa hívás:
# extract_text("file.pdf")


def rotate_pdf(input_path, output_path, rotation):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for page in reader.pages:
        page.rotate(rotation)  # Pozitív érték: óramutató járásával megegyező
        writer.add_page(page)
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    print(f"PDF forgatva: {output_path}")

import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename()
    print(f"Kiválasztott fájl: {file_path}")

root = tk.Tk()
tk.Button(root, text="PDF kiválasztása", command=browse_file).pack()
root.mainloop()

