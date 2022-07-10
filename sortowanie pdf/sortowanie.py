import PyPDF2
pdfFile = PyPDF2.PdfFileReader('Automatyzacja-nudnych-zadań-z-Pythonem_Al-Sweigart.pdf')
text = pdfFile.extractText()
print(text)