import PyPDF2
from learn import list_datasets
import os

source_docs = list_datasets("source_docs")


def read_pdf_to_text(filepath):
    with open(filepath, 'rb') as pdffileobj:
        pdfreader = PyPDF2.PdfFileReader(pdffileobj)
        numpages = pdfreader.numPages
        all_pages = ""
        for i in range(1, numpages):
            pageobj = pdfreader.getPage(i)
            text = pageobj.extractText()
            text.encode('ascii', 'ignore')
            all_pages += text
        return all_pages


for cat, files in source_docs.items():
    for file in files:
        text = read_pdf_to_text(file)
        print(os.path.basename(file))
        with open(os.path.join("data", cat, os.path.basename(file)) + ".txt", "w", encoding="utf-8") as f:
            f.writelines(text)
