#! /bin/bash

/anaconda2/bin/python/python fetch.py
git add *
git commit -m "Automatic daily update"
git push origin master