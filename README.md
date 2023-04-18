# adcleaner - Altium Designer & Autodesk Invenor trash cleaner
Small utility for cleaning the mess after work in AD and AI

# Installing
You'll need `Python 3.7` or newer. You can download it from [python.org](https://www.python.org/),or your OS's repository.
For dependecy installation you will need `pip`:
```
pip install -r requirements.txt
```
If you want to build executable, you also need `make` utility. Most POSIX-compatible OS (like Linux distros, macOS etc.) have already preinstalled. If you use windows (probably, because AD & AI works only on windows), you can download make from [gunwin32.sourceforge.net](https://gnuwin32.sourceforge.net/packages/make.htm)

# Launch
To launch, just type
```
python adcleaner.py -p <path_to_folder>
```
Argument `-p` is optional. If not specified, `.` is folder where scan begins.
Example:
```
python adcleaner.py -p "C:\Users\nickellick\ADprojects"
```