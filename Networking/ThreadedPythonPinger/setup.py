import sys
from cx_Freeze import setup, Executable

#from distutils.core import setup

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win64":
    base = "Win64GUI"


setup(
    name='ThreadedPythonPinger',
    version='1',
    packages=[''],
    url='',
    license='MIT',
    author='JoachimR',
    author_email='joachimrexsinemail@gmail.com',
    description='',
    options = {"build_exe": build_exe_options},
    executables = [Executable("TPP_alpha2.py", base=base)]
)
