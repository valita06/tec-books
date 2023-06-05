from PyPDF2 import PdfFileWriter, PdfFileReader

def split_pdf(OrgulloYPrejuicio.pdf, page_num):
    pdf_reader = PdfFileReader(open('OrgulloYPrejuicio.pdf', "rb"))
    pdf_writer1 = PdfFileWriter()
    pdf_writer2 = PdfFileWriter()
    for page in range(page_num):
        pdf_writer1.addPage(pdf_reader.getPage(page))
    for page in range(page_num, pdf_reader.getNumPages()):
        pdf_writer2.addPage(pdf_reader.getPage(page))
    with open("doc1.pdf", 'wb') as file1:
        pdf_writer1.write(file1)
    with open("doc2.pdf", 'wb') as file2:
        pdf_writer2.write(file2)