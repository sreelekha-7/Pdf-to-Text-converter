import PyPDF2
read_pdf = open('hyperloop.pdf','rb')
reader_pdf = PyPDF2.PdfFileReader(read_pdf)
num_pages = reader_pdf.numPages
convert_pages = reader_pdf.getPage(num_pages-1)
extract_text = convert_pages.extractText()
location = open(r"C:\Users\91998\Desktop\savehere\Hyperloop.txt",'a')
location.writelines(extract_text)
location.close()