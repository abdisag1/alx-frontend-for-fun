#!/usr/bin/python3
"""
takes two argumnets
"""
import sys
import os

if __name__ == '__main__':
    """ this function takes two arguments markdown and htmlfile"""
    if(len(sys.argv) < 3):
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    markdown = sys.argv[1]
    markdownfile = os.path.exists(markdown)
    if(markdownfile == False):
        print(f'missing {markdown}')
        exit(1)
