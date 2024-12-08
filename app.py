
import tkinter as tk
from tkinter import filedialog
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

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    print(text)

def rotate_pdf(input_path, output_path, rotation):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for page in reader.pages:
        page.rotate(rotation)
        writer.add_page(page)
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    print(f"PDF forgatva: {output_path}")

def browse_and_merge():
    file_paths = filedialog.askopenfilenames(title="Válaszd ki az összefűzendő PDF-eket")
    output_path = filedialog.asksaveasfilename(title="Mentsd el az új PDF-et", defaultextension=".pdf")
    if file_paths and output_path:
        merge_pdfs(output_path, *file_paths)
        print(f"Összefűzött fájl: {output_path}")

def browse_and_extract():
    file_path = filedialog.askopenfilename(title="Válassz egy PDF fájlt")
    if file_path:
        print("Kinyert szöveg:")
        extract_text(file_path)

def browse_and_rotate():
    input_path = filedialog.askopenfilename(title="Válassz egy PDF fájlt")
    output_path = filedialog.asksaveasfilename(title="Mentsd el az új PDF-et", defaultextension=".pdf")
    if input_path and output_path:
        rotation = int(input("Add meg a forgatás szögét (+90 vagy -90): "))
        rotate_pdf(input_path, output_path, rotation)

# GUI létrehozása
root = tk.Tk()
root.title("PDF Kezelő Alkalmazás")

tk.Button(root, text="PDF-ek összefűzése", command=browse_and_merge).pack(pady=5)
tk.Button(root, text="Szöveg kinyerése PDF-ből", command=browse_and_extract).pack(pady=5)
tk.Button(root, text="PDF forgatása", command=browse_and_rotate).pack(pady=5)

root.mainloop()