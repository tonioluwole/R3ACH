#imported necessary libraries
from zipfile import ZipFile
from tkinter.filedialog import askopenfilename
import img2pdf
import glob

# pass the name of the zip file to extract
filename = askopenfilename()
mypath = 'C:/Users/tonio/Downloads/DP/CanvaPNGs'
newpath = 'C:/Users/tonio/Downloads/DP/CanvaPDFs'

# opening the zip file in read mode
with ZipFile(filename, 'r') as zip:
    # display the contents of the zip file
    zip.printdir()

    # extracting all the files
    print('Extract in progress...')
    zip.extractall(path=mypath, members=None, pwd=None)
    print('All files are extracted!')
    
#creating a list of all the extracted filenames
imglist = glob.glob(mypath+"\*")
print(imglist)

#naming the new pdf
print("Please type file name of new pdf")
name = input()

#creating the new pdf
with open(newpath+name+".pdf","wb") as f:
    f.write(img2pdf.convert(imglist))
    print('PDF has been created!')
