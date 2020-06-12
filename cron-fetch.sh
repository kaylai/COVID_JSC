#! /bin/bash

/anaconda2/bin/python fetch.py
git add *
git commit -m "Automator auto-update"
git push origin master