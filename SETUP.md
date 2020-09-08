# Installing Anaconda 3 on Windows 10

## Getting rid of previous Anaconda installations

1. Uninstall all previous version of Anaconda.
2. Delete all things associate to Anacond from ```~\AppData\Roaming``` and ```~\AppData\Local\``` (jupyter, etc.).

## Installing Anaconda 3 core
_Instructions for Anaconda 4.8.3|4_

3. Download [Anaconda (64-bit)](https://www.anaconda.com/products/individual/get-started).
4. Install Anaconda to ```C:\Program Files\Anaconda3```: All users; _do not_ add to system path; _do not_ register Anaconda 3 as system Python 3.8

## Getting started

5. Verifying installation by searching for Anaconda Prompt.
6. Type: ```conda info```.
7. Update Anaconda: ```conda update conda```
8. Type: ```python``` and exit.
9. Create your first environment: ```conda create --name yoshi python=3.8```
10. Activate your environment: ```conda activate yoshi``` 

Source:
* [Conda cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

# Installing Eclipse
_Instruction for Eclipse IDE for C/C++ Developers  2020-06 (4.16.0)_

1. Download latest [Java JDK](https://www.java.com/en/).
2. Download [Eclipse](https://www.eclipse.org/downloads/).
3. Install Eclipse.
4. Open Eclipse.
5. Go to ```Help > Install New Software…```
6. Paste ```http://www.pydev.org/updates``` into ```Work with: ``` field, and press ```Add…```
7. Check parts you want to install, and restart.
8. Choose default workspace.
9. Create new project: ```New > Project…``` using the ```PyDev > PyDev Project``` wizard.

Source:
* [Linking Anaconda Python in Eclipse](https://docs.anaconda.com/anaconda/user-guide/tasks/integration/eclipse-pydev/)
 
## Adding Anaconda Python to Eclipse
_Instructions for:
* Eclipse IDE for C/C++ Developers  2020-06 (4.16.0)
* Anaconda 4.8.4
* PyDev 8.0.0.202009061309_
10. Go to ```Preferences > PyDev > Interpreters > Python Interpreter > Browse for python/pypy exe```
11. Choose one of the Python interpreter from you environments. Typically in ```C:\Users\joschua\.conda\envs```
12. Under ```Packages```: Check off ```Load conda env vars before run?```.
13. Under ```Environment```: ```Add…``` variable ```CONDA_DLL_SEARCH_MODIFICATION_ENABLE``` with value ```1```.
14. Press ```Apply and Close```. 
15. Right click on the project and choose ```Properties```.
16. Go to ```PyDev - Interpreter```.
17. Choose the desired ```Ìnterpreter```.
18. Press ```Apply and Close```.
 
Source: 
* [Setup Eclipse with PyDev](http://www.scopefoundry.org/advanced_dev_windows_step_by_step.html)

# Installing PyCharm
_Instructions for: 
* PyCharm Community 2020.2.1
* Anaconda 4.8.4
* PyDev 8.0.0.202009061309_   

1. Download [PyCharm Community](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows)
2. Install PyCharm Community.
3. Open PyCharm Community.
4. Got to  ```File > Settings > Project <name> > Python Interpreter```
5. Click on the gear symbol in the top right corner, next to the drop down menu.
6. Press ```Add…```.
7. Go to ```Conda Environment > Existing Environment```
8. Under ```Interpreter```, choose your environment in ```C:\Users\<usr>\.conda\envs\<env>\python.exe```.
9. Under ```Conda executable```, choose your Anaconda exe in ```C:\Program files\Anaconda3\_conda.exe```.
10. Press ```OK```.
11. Choose your desired interpreter in the drop down menu under ```File > Settings > Project <name> > Python Interpreter```. 
(You might have to press ```Show all…``` to see previously added interpreters.)

Source: 
* [Configure a Conda virtual environment]()https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html

# Installing original Python 3 on Windows 10

## Getting rid of previous Python installations

1. Uninstall all version of Python 2 & 3.
2. Delete your Python folder(s): ```C:\Program Files\Python\PythonXX```. 
3. Delete your your Scripts folder if it exists: ```~\AppData\Roaming```. Do the same with any Python packages (pip, virtualenv, etc.) under ```~\AppData\Local\```.

## Installing Python cores

4. Download [Python 3 (64-bit)]((https://www.python.org/downloads/)).
5. Install  Python 3 to ```C:\Program Files\Python\Python38```. (You might have to give Admin rights if there is an error message.)
6. Go to Edit the system environment variables > Advanced > Environment Variables…
7. Highlight ```Path > Edit…``` and add two ```New variables```
  * ```C:\Program Files\Python\Python38```
  * ```C:\Program Files\Python\Python38\Scripts```
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
