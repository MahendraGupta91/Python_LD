# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:36:40 2020

@author: Mahendra
"""

import clipboard
clipboard.copy("abc")  # now the clipboard content will be string "abc"
text = clipboard.paste()  # text will have the content of clipboa
print(text);