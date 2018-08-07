import PyPDF2
import os

#Extracting text from PDF

pdfFileObj = open ('filenName.pdf', 'rb')
pdfReader = PyPDF2.pdfReader(pdfFileObj)

pdfReader.numPages

pageObj = pdfReader.getPage(0)
pageObj.extractText()

#Decryping PDF

pdfReader = PyPDF2.PdfFileReader(open('encrytedFIeName.pdf', 'rb'))
pdfReader.isEncryppted
pdfReader.getPage(0)
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)

