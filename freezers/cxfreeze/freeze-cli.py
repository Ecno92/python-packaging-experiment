import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": [], "excludes": []}
gui_app = False
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32" and gui_app:
    base = "Win32GUI"

setup(  name = "Hello World Example! - CLI",
        version = "0.1",
        description = "Result of packaging a hello world example.",
        options = {"build_exe": build_exe_options},
        executables = [Executable("../../apps/cli.py", base=base)])
