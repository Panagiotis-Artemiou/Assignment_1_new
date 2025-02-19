# Assignment 1


### Conda environment, install, and testing <a name="install"></a>

To install this package, please begin by setting up a conda environment (mamba also works):
```bash
conda create --name newtons-method-env python=3.12
```
Once the environment has been created, activate it:

```bash
conda activate newtons-method-env
```
Double check that python is version 3.12 in the environment:
```bash
python --version
```
Ensure that pip is using the most up to date version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```
Create an editable install of the bisection method code (note: you must be in the correct directory):
```bash
pip install -e .
```
Test that the code is working with pytest:
```bash
pytest -v --cov=newtonsmethod --cov-report term-missing
```
Code coverage should be 100%. Now you are prepared to write your own code based on this method and/or run the tutorial. 

If you would like, you can also open python and check to make sure that the import works properly:
```bash
(newtons-method-env) $ python
Python 3.12.8 | packaged by Anaconda, Inc. | (main, Dec 11 2024, 11:37:13) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from bisectionmethod import bisection_method as bim
>>> bim.hello_world()
'hello world'
```
If you are using VSCode to run this code, don't forget to set VSCode virtual environment to newtons-method-env.