import cx_Freeze
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("[Game Project 6] Card Meister v2.0.0a.py")]

cx_Freeze.setup(
    name="Card Meister",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["Data", "Tutorial", "readme.txt"]}},
    executables=executables,
    version="2.0.0"
)