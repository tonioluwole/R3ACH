#imported necessary libraries
import os
from zipfile import ZipFile
from tkinter.filedialog import askopenfilename
import img2pdf
import PySimpleGUI as psg
import glob
import easyocr

"""
filename = askopenfilename(title='Choose a file')
"""

defont = "'Monsterrat', 12 "

def listreturn(filename):
    foldername = filename[25:-4].replace(" ","")
    print(foldername)
    mypath = 'C:/Users/tonio/Downloads/DP/CanvaPNGs/'+foldername

    newpath = 'C:/Users/tonio/Downloads/DP/CanvaPDFs/'+foldername

    # opening the zip file in read mode
    with ZipFile(filename, 'r') as zip:
        # display the contents of the zip file
        zip.printdir()

        # extracting all the files
        zip.extractall(path=mypath, members=None, pwd=None)
        print('All files are extracted!')

    #creating a list of all the extracted filenames and 
    imglist = glob.glob(mypath+"\*")

    return imglist

def reader(list):
    #Reading text from the first image with oCR
    print('Getting text from first image...')
    reader = easyocr.Reader(['en'])
    read = reader.readtext(list[0], detail = 0)
    rname = ' '.join(read)
    pdfname = rname[14:].replace(':','')

    return pdfname

def namer (inp,returnedlist):
    #creating the new pdf
    with open(inp+".pdf","wb") as f:
        f.write(img2pdf.convert(returnedlist)) #need to write to specific path


column_layout = [
    []
]

def new1():
    return [
        [psg.Text("All files are extracted!", font=(defont))],
        [psg.Text("Getting text from first image...", font=(defont))]
    ]

def new3():
    return [
        [psg.Text("PDF has been created!", font=(defont))]
    ]

def new2():
    return [
        [psg.T("1st page of pdf is: "+life+"' \nWhat should file name be?\n", font=(defont))],
        [psg.Input(enable_events=True, key='-INP-', font=(defont))],
        [psg.Submit()]
    ]

psg.theme('DarkTeal6')

layout = [
   [psg.Text('Select a file',font = (defont), expand_x=True, justification='center')],
   [psg.Input(enable_events=True, key='-IN-', font=(defont), expand_x=True), psg.FileBrowse()],
   [psg.Button("Convert to PDF", font=(defont))],
   [psg.Column(column_layout, key='-Column-', font=(defont))],
   [psg.Button("Exit", font=(defont))]
]


window = psg.Window('FileChooser Demo', layout,
size=(715,800))
while True:
   event, values = window.read()

   if event == 'Convert to PDF':
      filename = values["-IN-"]
      imglist = listreturn(filename)
      life = reader(imglist)
      print(life)
      window.extend_layout(window['-Column-'], new1())
      window.extend_layout(window['-Column-'], new2())
    
   if event == 'Submit':
       input = values['-INP-']
       print(input)
       namer(input,imglist)
       window.extend_layout(window['-Column-'], new3())

   if event == psg.WIN_CLOSED or event == 'Exit':
      break
window.close()

