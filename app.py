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

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def rotate_pdf(input_path, output_path, rotation):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for page in reader.pages:
        page.rotate(rotation)
        writer.add_page(page)
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

def browse_and_merge():
    file_paths = filedialog.askopenfilenames(title="Válaszd ki az összefűzendő PDF-eket", filetypes=[("PDF files", "*.pdf")])
    output_path = filedialog.asksaveasfilename(title="Mentsd el az új PDF-et", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_paths and output_path:
        merge_pdfs(output_path, *file_paths)
        label_result.config(text="PDF-ek sikeresen összefűzve!", fg="green")

def browse_and_extract():
    file_path = filedialog.askopenfilename(title="Válassz egy PDF fájlt", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        extracted_text = extract_text(file_path)
        label_result.config(text="Szöveg kinyerve a terminálban!", fg="green")
        print("Kinyert szöveg:\n", extracted_text)

def browse_and_rotate():
    input_path = filedialog.askopenfilename(title="Válassz egy PDF fájlt", filetypes=[("PDF files", "*.pdf")])
    output_path = filedialog.asksaveasfilename(title="Mentsd el az új PDF-et", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if input_path and output_path:
        try:
            rotation = int(input("Add meg a forgatás szögét (+90 vagy -90): "))
            rotate_pdf(input_path, output_path, rotation)
            label_result.config(text="PDF sikeresen forgatva!", fg="green")
        except ValueError:
            label_result.config(text="Érvénytelen szögérték!", fg="red")

# Fő ablak
root = tk.Tk()
root.title("PDF Kezelő Alkalmazás")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#2E2E2E")  # Háttérszín: sötét szürke

# Keret (Frame)
frame_main = tk.Frame(root, padx=10, pady=10, bg="#2E2E2E")
frame_main.pack(expand=True, fill="both")

# Címke (Label)
label_title = tk.Label(
    frame_main,
    text="PDF Kezelő Alkalmazás",
    font=("Helvetica", 16),
    fg="#F2F2F2",  # Világos szürke szöveg
    bg="#2E2E2E",  # Sötét szürke háttér
)
label_title.grid(row=0, column=0, columnspan=2, pady=20)

# PDF összefűzése gomb
btn_merge = tk.Button(
    frame_main,
    text="PDF-ek összefűzése",
    command=browse_and_merge,
    width=20,
    bg="#585858",  # Középszürke háttér
    fg="#FFFFFF",  # Fehér szöveg
    relief="flat",
)
btn_merge.grid(row=1, column=0, pady=10)

# Szöveg kinyerése PDF-ből gomb
btn_browse = tk.Button(
    frame_main,
    text="Szöveg kinyerése PDF-ből",
    command=browse_and_extract,
    width=20,
    bg="#585858",
    fg="#FFFFFF",
    relief="flat",
)
btn_browse.grid(row=2, column=0, pady=10)

# PDF forgatása gomb
btn_rotate = tk.Button(
    frame_main,
    text="PDF forgatása",
    command=browse_and_rotate,
    width=20,
    bg="#585858",
    fg="#FFFFFF",
    relief="flat",
)
btn_rotate.grid(row=3, column=0, pady=10)

# Eredmény kijelzése
label_result = tk.Label(
    frame_main,
    text="",
    fg="#A4A4A4",  # Világos szürke szöveg
    font=("Arial", 10),
    bg="#2E2E2E",
)
label_result.grid(row=4, column=0, pady=20)

# Ablak közepére helyezés
frame_main.grid_rowconfigure(0, weight=1)
frame_main.grid_rowconfigure(1, weight=1)
frame_main.grid_rowconfigure(2, weight=1)
frame_main.grid_rowconfigure(3, weight=1)
frame_main.grid_rowconfigure(4, weight=1)
frame_main.grid_columnconfigure(0, weight=1)

root.mainloop()