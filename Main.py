#Divisore PDF
import PyPDF2

pdf_input = open(input('Inserisci il nome del PDF : '),'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_input)
number_of_pages = pdf_reader.getNumPages()
print(str(number_of_pages))



pdf_writer = PyPDF2.PdfFileWriter()

second_half_page = (number_of_pages/2)
for number_of_pages in range(int(number_of_pages/2),number_of_pages,1):
    
    pdf_writer.addPage(pdf_reader.getPage(int(second_half_pages)))
    second_half_pages += 1

split_file = open('C:/Users/FrancescoForesti/Desktop/PDF_divisor/split.pdf','wb')
pdf_writer.write(split_file)

split_file.close()
pdf_input.close()
