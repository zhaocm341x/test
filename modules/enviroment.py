__author__ = 'Administrator'
import os


def run(**args):
    print "[*]in enviroment module"
    return str(os.environ)