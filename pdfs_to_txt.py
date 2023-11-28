from pypdf import PdfReader
import os


pdfs = os.listdir("programmas_pdf")

def text_from_pdf(pdf_path):
    pdf_reader = PdfReader(pdf_path)
    num_pages = len(pdf_reader.pages)
    for page_num in range(num_pages):
        yield pdf_reader.pages[page_num].extract_text()


def text_to_file(pdf_path, text):
    base_name = os.path.basename(pdf_path)
    file_name, _ = os.path.splitext(base_name)
    output_file_path = f"programmas_txt/{file_name}.txt"

    with open(output_file_path, 'a', encoding='utf-8') as output_file:
        output_file.write(text)


exceptions = []

for pdf_path in pdfs:
    try:
        pdf_path = f"programmas_pdf/{pdf_path}"
        for i, page_text in enumerate(text_from_pdf(pdf_path)):
            print(f"Writing text from page {i + 1} to file...")
            text_to_file(pdf_path, page_text)
            
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        exceptions.append(pdf_path)


