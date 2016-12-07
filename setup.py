from distutils.core import setup

import py2exe ,sys ,os

sys.argv.append('py2exe')


op = { "py2exe": {
                "includes": ["pyautogui"]
          }}

setup(
    windows=['Main.py'],options=op
)