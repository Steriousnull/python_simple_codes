import PyPDF2

# Open the PDF file in binary read mode
pdfFileObj = open("C://Users//c24a1/Downloads/Dhanush-Resume.pdf", 'rb')

# Create a PdfReader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Get the page at index 0
pageObj = pdfReader.pages[0]

# Extract and print the text content of the page
text = pageObj.extract_text()
print(text)

# Close the PDF file
pdfFileObj.close()
