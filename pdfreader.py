import pyttsx3
import PyPDF2
book = open('IntroCybersecurity - Additional Resources and Activities.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()

for i in range(0, pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()




