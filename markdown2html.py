#!/usr/bin/python3
import sys
import os

markdown = sys.argv[1]
if(len(sys.argv) < 3):
    print("Usage: ./markdown2html.py README.md README.html" ,file=sys.stderr)
    exit (1)
   
markdownfile = os.path.exists(markdown)
if(markdownfile == False):
    print("missing {markdown}", file=sys.stderr)
    exit (1)