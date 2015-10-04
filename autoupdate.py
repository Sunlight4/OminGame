import urllib2
from utils import *
import pygame

def isClientOutdated():
    response = urllib2.urlopen('https://drive.google.com/open?id=0By3ws9NUkj5_dzE3NjhELTBSdGc').read()
    VERSION = '1.0dev'

    if VERSION in response:
        return False
    else:
        return True
