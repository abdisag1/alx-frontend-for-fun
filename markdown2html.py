#!/usr/bin/python3
import sys
import os


if(len(sys.argv) < 3):
    print("Usage: ./markdown2html.py README.md README.html" ,file=sys.stderr)
    exit (1)
if(sys.argv[1] == "README.md"):    
    markdown = sys.argv[1]
    markdownfile = os.path.exists(markdown)
    if(markdownfile == False):
        print("missing README.md")
        exit (1)