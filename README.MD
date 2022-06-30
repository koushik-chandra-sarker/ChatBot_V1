# Requirements

```bash
python3.9
```

At first, create a virtual environment and activate it
```bash
$ python3 -m venv [your_path]
````
# Python venv activation


### Windows venv activation
To activate your venv on Windows, you need to run a script that gets installed by venv. If you created your venv in a directory called myenv, the command would be:
``` bash
# In cmd.exe
$ cd [your project_directory]
$ venv\Scripts\activate.bat
# In PowerShell
$ venv\Scripts\Activate.ps1
````
### Linux and MacOS venv activation
On Linux and MacOS, we activate our virtual environment with the source command. If you created your venv in the myvenv directory, the command would be:
```
$ source myvenv/bin/activate
```

# Installation
#### Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Packages.

```bash
$ pip install -r requirements.txt
```