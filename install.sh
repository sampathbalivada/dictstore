#!/bin/bash

python3 -m pip uninstall dictstore -y

python3 setup.py bdist_wheel 

python3 -m pip install dist/dictstore-*.whl