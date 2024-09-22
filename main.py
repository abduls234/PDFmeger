import PyPDF2



pdfiles=["Recommendation Letter 1.pdf", "Recommendation Letter 2.pdf"]

merger = PyPDF2.PdfFileMerger()

for file in pdfiles:
    pdf=open(file,"rb")
    pdfreader=PyPDF2.PdfReader(pdf)
    merger.append(pdfreader)
pdf.close()
merger.write("merged.pdf")


