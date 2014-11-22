# Be aware to first setup a valid Python 3 environment with the proper requirements installed.
# Also activate your Python installation/venv before executing those commands. 

usage:
	echo "use: make freeze-all"

freeze-cli:
	nuitka --recurse-all --standalone ../../apps/cli.py

freeze-gui:
	nuitka --recurse-all --standalone ../../apps/gui.py

freeze-all: freeze-cli freeze-gui