from pathlib import Path
import shutil

P = Path.home() / "Downloads/Projects/filesorter"
txt = P / ("text")
png = P / ("image")
others = P / ("others")
protected_files = []

def ask_protect_file():
    while True:
        result = input("do you want to protect some files (yes, no):").lower()
        if result == "yes":
            protected_file = input("write name of the file you want to protect:").strip()
            protected_files.append(protected_file)
        else:
            break

def folder_maker():
    if not txt.exists():
        txt.mkdir()
        print("text folder has been made  ")
    else:
            print("text folder already exist")
    if not png.exists():
        png.mkdir() 
        print("image folder has been made  ")
    else:
            print("image folder already exist")
    if not others.exists():
        others.mkdir()
        print("other folder has been made    ")
    else:
        print("other folder already exist")

def main():
    for file in P.glob("*.txt"):
        if file.is_file() and file.name != "main.py" and file.name not in protected_files and not file.name.startswith(".") :
            shutil.move(file, txt)
    for file in P.glob("*.png"):
        if file.is_file() and file.name != "main.py" and file.name not in protected_files and not file.name.startswith(".") :
            shutil.move(file, png)
    for file in P.glob("*"):
        if file.is_file() and file.name != "main.py" and file.name not in protected_files and not file.name.startswith(".") :
            shutil.move(file, others)    
              

try:
    ask_protect_file()
    folder_maker()
    main()
except Exception as e:
    print("error:", e)