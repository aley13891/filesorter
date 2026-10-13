# File Sorter

A Python script that sorts files in a folder into subfolders by file type.

## What it does
- Moves `.txt` files into `text/`
- Moves `.png` files into `image/`
- Moves everything else into `others/`
- Lets you protect files so they are never moved
- Skips hidden files and the script itself

## How to run
```bash
python3 main.py
```
The script asks if you want to protect any files, then sorts the folder.

## Requirements
Python 3. No extra packages are needed.

## Warning
Test on a folder of fake files first. Moving files is hard to undo.
