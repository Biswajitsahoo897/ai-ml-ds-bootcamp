# this is the code for the merge of two pdfs by harry
from PyPDF2 import PdfWriter
import os

merge=PdfWriter()
files =[file for file in os.listdir(".vscode/PYTHON/merge_pdf") if file.endswith(".pdf")]

for pdf in files:
    merge.append(pdf)

merge.write("merge-pdf_1.pdf")
merge.close()



# GPT which is simple and working
from PyPDF2 import PdfMerger

# Function to merge two PDFs
def merge_pdfs(pdf1, pdf2, output):
    merger = PdfMerger()
    
    # Append the two PDFs
    merger.append(pdf1)
    merger.append(pdf2)
    
    # Write the output file
    with open(output, 'wb') as output_pdf:
        merger.write(output_pdf)

# Example usage
pdf1 = ".vscode/PYTHON/merge_pdf/Recurrence relation .pdf"
pdf2 = ".vscode/PYTHON/merge_pdf/Recurssion Tree.pdf"
output = ".vscode/PYTHON/merge_pdf/mergepdf_1_sample.pdf"

merge_pdfs(pdf1, pdf2, output)

print(f"PDFs merged into {output}")
