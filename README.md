# Simple Python Autoclicker
## By Tommeeboi
A very simple autoclicker made in Python. Due to Python being incredibly slow it only clicks around 9.2 cps

You can use this as a template if you want

## How To Use
For the default exe file, just run it. Your antivirus might see it as suspicious, just wait for it to scan the file

If you want to run the source code, install pyautogui:
```
pip install pyautogui
```

## Compile Source Code
First, you need to have Python installed, and have it added to PATH

You need to install pyinstaller if you haven't already:
```
pip install pyinstaller
```
And compile to executable:
```
pyinstaller --onefile clicker.py
```
After you compile, you can delete the build folder and .spec file

## Releases
Beta v1.0: Should be fully done, just checking for bugs

Beta v1.1: Updated License

v1.0 (LATEST):

1. FixedLimit is no longer turned into an integer in the while loop, due to it already being an integer
2. While loop isn't cramped anymore
3. Source code and compiled code now have different file names. There should no longer be issues when compiling source code

This'll probably be the last release, because there isn't really anything for me to add at this point