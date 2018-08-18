import cmd, sys
import glob, os
from PyPDF2 import PdfFileReader, PdfFileWriter
from os.path import expanduser

class Split:
	print ("###############PDF_SPLITTER############")
	print ("Instructions: ")
	print ("1)Create a folder caled 'PDF' on your Desktop")
	print ("2)Rename the pdf file you want to split to 'MyPdf.pdf' and move it to the folder just created")
	print ("#######################################")
	print ("#######################################")
	print ("I will take about about the rest...")
	print ("#######################################")
	print ("#######################################")

def split(): 
        #Find path with file
	from os.path import expanduser
environment = expanduser("~/Desktop/PDF")
os.chdir(environment)
mypdf = "MyPdf.pdf"
pdf_file = open(os.path.join(os.getcwd(), "MyPdf.pdf"),"rb")
pdf_reader = PdfFileReader(pdf_file)
pdf_writer = PdfFileWriter()

    #Prompt user which page to pslit
split = input("Which page you want to keep?  ")
convert = int(split)
pdf_writer.addPage(pdf_reader.getPage(convert -1))
question = input ("Any more pages?......type y/n:  ")

while (question == "y"):
	newsplit = input("Which page you want to keep?  ")
	newconvert = int(newsplit)
	pdf_writer.addPage(pdf_reader.getPage(newconvert -1))
	question = input ("Any more pages?......type y/n:  ")



split_file = open(os.path.join(os.getcwd(), "NewSplit.pdf"), "wb")
pdf_writer.write(split_file)
split_file.close()
pdf_file.close()

print ("Your new file is called 'NewSplit'")
print ("#######################################")
print ("Thank you for using me! Bye Bye...")

split()
