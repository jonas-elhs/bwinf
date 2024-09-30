import os
import shutil
from docx2pdf import convert as pdf

ROOT = 'BWINF_[JAHR]'
ZIP_ROOT = ROOT + '.zip'

def main():
  prepare()
  compile()
  archive()

def prepare():
  if os.path.exists(ROOT):
    shutil.rmtree(ROOT)

  if os.path.exists(ZIP_ROOT):
    os.remove(ZIP_ROOT)

def compile():
  for name in [ dir.name for dir in os.scandir('.') if dir.is_dir() and not (dir.name.startswith(['.', '-'])) ]:
    folder = os.path.join(ROOT, name)
    py = name.lower() + '.py'
    docx = name + '.docx'

    if not os.path.exists(folder):
      os.makedirs(folder)

    pdf(os.path.join(name, docx), ROOT)
    shutil.copy(os.path.join(name, py), os.path.join(folder, py))

def archive():
  shutil.make_archive(ROOT, 'zip', ROOT)
  shutil.rmtree(ROOT)

if __name__ == '__main__':
  main()