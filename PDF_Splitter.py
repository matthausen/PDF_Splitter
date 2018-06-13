import cmd, sys
import glob, os
from PyPDF2 import PdfFileReader, PdfFileWriter
from os.path import expanduser


class Split:
	#Show some instructions
	print (" ")
	print (" ")
	print (" ")
	print (" ")
	print (" ")
	print (" ")
	print (" ")
	print ("###############PDF_SPLITTER############")
	print ("Instructions: ")
	print ("1)Create a folder caled 'PDF' on your Desktop")
	print ("2)Rename the pdf file you want to split to 'MyPdf.pdf' and move it to the folder just created")
	print ("#######################################")
	print ("#######################################")
	print ("I will take about about the rest...")
	print ("#######################################")
	print ("#######################################")


	def search_destroy():

		#Find path with file
		from os.path import expanduser
        environment = expanduser("~/Desktop/PDF")
        os.chdir(environment)

    	pdf_file = open ("C:\Users\Matthausen\Desktop\PDF\MyPdf.pdf", "rb")
	pdf_reader = PdfFileReader(pdf_file)
	pdf_writer = PdfFileWriter()

        #Prompt user which page to pslit
	split = raw_input("Which page you want to keep?  ")
	convert = int(split)
	pdf_writer.addPage(pdf_reader.getPage(convert -1))

	question = raw_input ("Any more pages?......type y/n:  ")

	while (question == "y"):
		newsplit = raw_input("Which page you want to keep?  ")
		newconvert = int(newsplit)
		pdf_writer.addPage(pdf_reader.getPage(newconvert -1))
		question = raw_input ("Any more pages?......type y/n:  ")



	split_file = open("C:\Users\Matthausen\Desktop\PDF\MySplit.pdf", "wb")
	pdf_writer.write(split_file)
	split_file.close()
	pdf_file.close()


	print (" ")
	print (" ")
	print (" ")
	print ("Your new file is called 'MySplit'")
	print ("#######################################")
	print ("Thank you for using me! Bye Bye...")



