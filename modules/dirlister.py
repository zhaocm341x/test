__author__ = 'Administrator'
import os

def run(**args):
    print "[*]in list dir module"
    files=os.listdir(".")
    return str(files)

