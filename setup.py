from urllib.request import urlretrieve as download
import os

JAHR = '2024'
WETTBEWERB = str(int(JAHR) - 1981)
URL = 'https://bwinf.de/fileadmin/wettbewerbe/bundeswettbewerb/'+ WETTBEWERB + '/1_runde/Aufgaben' + WETTBEWERB + '1.pdf'
DATEI = 'Aufgaben.pdf'
ORDNER = os.path.dirname(os.path.abspath(__file__))

def replaceInFile(fileName: str):
  with open(fileName, 'r') as file:
    filedata = file.read()

  filedata = filedata.replace('[JAHR]', JAHR)

  with open(fileName, 'w') as file:
    file.write(filedata)

download(URL, DATEI)

replaceInFile(ORDNER + '/build.py')
replaceInFile(ORDNER + './README.md')

os.remove(ORDNER + 'setup.py')