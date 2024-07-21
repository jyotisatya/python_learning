## How to setup python modules

```python

# navigate to root folder
# install venv
python3 -m venv venv
add venv in .gitigore
source venv/bin/activate

touch requirements.txt

# add libraries in requiment.txt
# For setup as module we need setuptools as package to be added in requirements.txt

# install all the required libraries from requirements.txt file
pip install -r requirements.txt

#touch setup.py add this lines in setup.py
from setuptools import setup, find_packages

setup(
    name='python_learning',
    version='0.1',
    packages=find_packages(),
)

## make sure you have added __init_.py in all the folder which you want as module

## make the module for the setup tools
pip install -e .

#now you can import directly all the module
# to run a file

python -m {path to your file}.py

```