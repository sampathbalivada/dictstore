#!/bin/bash

# create a virtual environment for testing

echo '--------------------------------'
echo 'Setting Up Virtual Environment'
echo '--------------------------------'

python3 -m venv testvenv

# activate the virtual environment

source testvenv/bin/activate

# remove dictstore if it already exists

echo '--------------------------'
echo 'Removing Existing Package'
echo '--------------------------'

python -m pip uninstall dictstore -y

echo '------------------'
echo 'Installing Package'
echo '------------------'

python setup.py install

# run the tests using test.py

echo '------------------'
echo 'Running Tests'
echo '------------------'

python tests/test.py