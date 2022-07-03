#!/usr/bin/python3
"""
takes two argumnets
"""
import sys
import os
import markdown

if __name__ == '__main__':
    """ this function takes two arguments markdown and htmlfile"""
    if(len(sys.argv) < 3):
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    markdownfile = sys.argv[1]
    htmlfile = sys.argv[2]
    markdownfile = os.path.exists(markdownfile)
    if(markdownfile == False):
        print(f'missing {markdownfile}',file=sys.stderr)
        exit(1)
    
    
    with open(sys.argv[1], 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    with open(sys.argv[2], 'w') as f:
        f.write(html)
