from datetime import datetime
from os import path

BASE_PATH = path.dirname(__file__) + '/'
with open(BASE_PATH + '../index.md') as md_file:
    BASE_TITLE = md_file.readline().strip() + " v" + datetime.today().strftime('%Y.%m.%d')

DEBUG_MODE = True
