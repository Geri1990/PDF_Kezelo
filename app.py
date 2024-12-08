
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