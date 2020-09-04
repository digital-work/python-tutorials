# Installing Python 2 & 3 on Windows 10


## Installing Python cores

1. Download [Python 2 & 3 (64-bit)]((https://www.python.org/downloads/)).
2. Install Python 2 to C:\Program Files\Python\Python27, & Python 3 to C:\Program Files\Python\Python38. (You might have to give Admin rights if there is an error message.)
3. Go to Edit the system environment variables > Advanced > Environment Variables…
4. Highlight Path > Edit…
5. Add for New variables
  * C:\Program Files\Python\Python27
  * C:\Program Files\Python\Python27\Scripts
  * C:\Program Files\Python\Python38
  * C:\Program Files\Python\Python38\Scripts
6. Rename the executables in C:\Program Files\Python\Python27 to python2.exe & C:\Program Files\Python\Python38 to python3.exe
7. Check that you can:
  * Execute Python in the terminal with ```python2``` & ```python3```. Check that the right versions are used.
  * Check that the right executables are used with ```where python2``` & ```where python3```

## Installing pip & virtualenv

8. Check if pip is already installed ```python2 -m pip --version``` & ```python3 -m pip --version```
    1. If yes: Upgrade to newest version:  ```python2 -m pip install --upgrade pip``` & ```python3 -m pip install --upgrade pip```
    2. If no: Install it.
9. Check if pip is already installed ```python2 -m virtualenv --version``` & ```python3 -m virtualenv --version```
    1. If yes: Upgrade top newest version: ```python2 -m pip install --upgrade virtualenv``` & ```python3 -m pip install --upgrade virtualenv```
	2. If no: Install virtualenv: ```python2 -m pip install --user pip``` & ```python3 -m pip install --user pip```
  
_Source:_  
* [Installing Python 2 & 3](https://datascience.com.co/how-to-install-python-2-7-and-3-6-in-windows-10-add-python-path-281e7eae62a)
* 
