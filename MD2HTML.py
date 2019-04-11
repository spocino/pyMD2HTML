#!/usr/bin/python
'''
Samuel Pocino
Created 4/11/2019

reads all files in arguments as markdown to be parsed, or stdin if no files are specified.
'''

import sys
import fileinput

mdfile = ""
for line in fileinput.input():
  mdfile = mdfile + line
