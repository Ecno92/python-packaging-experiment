# Be aware to first setup a valid Python 3 environment with the proper requirements installed.
# Also activate your Python installation/venv before executing those commands. 

usage:
	echo "use: make freeze-all"

freeze-cli:
	python freeze-cli.py build -b build/cli/

freeze-gui:
	python freeze-gui.py build -b build/gui/

freeze-all: freeze-cli freeze-gui
