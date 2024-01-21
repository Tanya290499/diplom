#!/bin/zsh
cd ../../
pwd
pytest -s -v class_work/test_api.py --alluredir=results
