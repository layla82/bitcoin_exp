#!/bin/bash
virtualenv --python=python2.7 venv && . venv/bin/activate
pip install -r requirements.txt
