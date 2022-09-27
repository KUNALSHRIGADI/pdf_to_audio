from tkinter import filedialog
import pyttsx3
import PyPDF2


book_string = ""

file = filedialog.askopenfile(mode='r')
print(file.name)

pdfFileObj = open(file.name, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

page_no = int(pdfReader.numPages)

for num in range(page_no):
    # creating a page object
    pageObj = pdfReader.getPage(num)

    # extracting text from page
    book_string += (pageObj.extractText())

    # closing the pdf file object
pdfFileObj.close()

engine = pyttsx3.init()  # object creation

""" RATE"""
rate = engine.getProperty('rate')  # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty('rate', 120)  # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file(book_string, 'test.mp3')
engine.runAndWait()
