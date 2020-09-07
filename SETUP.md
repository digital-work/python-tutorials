# Installing Anaconda on Windows 10

## Getting rid of previous Anaconda installations

1. Uninstall all previous version of Anaconda.
2. Delete all things associate to Anacond from ```~\AppData\Roaming``` and ```~\AppData\Local\``` (jupyter, etc.).

## Installing Anaconda core

3. Download [Anaconda (64-bit)](https://www.anaconda.com/products/individual/get-started).
4. Install Anaconda to ```C:\Program Files\Anaconda3```: All users; _do not_ add to system path; _do not_ register anaconda 3 as system Python 3.8

## Getting started

5. Verifying installation by searching for Anaconda Prompt.
6. Type: ```conda info```.
7. Update Anaconda: ```conda update conda```
7. Type: ```python```

# Installing original Python 3 on Windows 10

## Getting rid of previous Python installations

1. Uninstall all version of Python 2 & 3.
2. Delete your Python folder(s): ```C:\Program Files\Python\PythonXX```. 
3. Delete your your Scripts folder if it exists: ```~\AppData\Roaming```. Do the same with any Python packages (pip, virtualenv, etc.) under ```~\AppData\Local\```.

## Installing Python cores

4. Download [Python 3 (64-bit)]((https://www.python.org/downloads/)).
5. Install  Python 3 to ```C:\Program Files\Python\Python38```. (You might have to give Admin rights if there is an error message.)
6. Go to Edit the system environment variables > Advanced > Environment Variables…
7. Highlight Path > Edit… and add two New variables
  * C:\Program Files\Python\Python38
  * C:\Program Files\Python\Python38\Scripts
8. Rename the executables in  C:\Program Files\Python\Python38 to python3.exe
9. Check that you can:
  * Execute Python in the terminal with ```python3```. Check that the right versions are used.
  * Check that the right executables are used with ``where python3```
10. Make sure that your user has Full Control allowed in the folder properties of Python38.

## Installing pip & virtualenv

11. Check if pip is already installed: ```python3 -m pip --version```
    1. If yes: Upgrade to newest version:  ```python3 -m pip install --upgrade pip```
    2. If no: Install it.

_Source:_  
* [Installing Python 2 & 3](https://datascience.com.co/how-to-install-python-2-7-and-3-6-in-windows-10-add-python-path-281e7eae62a)
* [Installing Pip and virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
