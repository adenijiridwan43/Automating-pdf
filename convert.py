from pdf2docx import Converter
pdf_file = 'convert.pdf'
docx_file = 'convert.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close