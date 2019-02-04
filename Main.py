#Divisore PDF
import PyPDF2

pdf_input = open(input('Inserisci il nome del PDF : ')+'.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_input)
number_of_pages = pdf_reader.getNumPages()
print('Numero totale di pagine :'+str(number_of_pages))
second_half_pages = (number_of_pages/2)
print('Prima meta\' :'+str(0)+' - '+str(int(second_half_pages)))
print('Prima meta\' :'+str(int(second_half_pages+1))+' - '+str(number_of_pages))

pdf_writer = PyPDF2.PdfFileWriter()
for number_of_pages in range(int(number_of_pages/2),number_of_pages,1):
    pdf_writer.addPage(pdf_reader.getPage(int(second_half_pages)))
    second_half_pages += 1
split_file = open('C:/Users/FrancescoForesti/Desktop/PDF_divisor/split_second_half.pdf','wb')
pdf_writer.write(split_file)


pdf_writer_2 = PyPDF2.PdfFileWriter()
indice=0
for number_of_pages in range(0,int(number_of_pages/2),1):
    pdf_writer_2.addPage(pdf_reader.getPage(indice))
    indice+=1
split_file_2 = open('C:/Users/FrancescoForesti/Desktop/PDF_divisor/split_first_half.pdf','wb')
pdf_writer_2.write(split_file_2)


split_file_2.close()
split_file.close()
pdf_input.close()
