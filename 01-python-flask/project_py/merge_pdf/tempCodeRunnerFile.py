from PyPDF2 import PdfWriter,PdfMerger

merger = PdfMerger()
pdfs=[]
n=int(input("Enter The Number of PDFs:"))

for i in range(0,n):
    print()
    name=input(f"Enter the name of the PDF No {i+1} : ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()