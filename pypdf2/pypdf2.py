import PyPDF2
dffile=open("C:\\Users\\Rhea Arora\\Documents\\extras\\Resume_Akanksha_Arora_Apr14.pdf","rb")
pdfreader=PyPDF2.PdfFileReader(dffile)
ob=pdfreader.getPage(0)
print(ob.extractText())
