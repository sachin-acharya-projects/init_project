from ..constants import *
from colorama import Fore
import sys
import os

__all__ = ['generate_plainweb']

def generate_plainweb(project, scss, tailwind):
    try:
        os.makedirs(f"{project}\\statics\\css")
        os.mkdir(f"{project}\\statics\\js")
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}Project Initialization Failed (Invalid Path). Please make sure following conditions applies\n\t1. The path {project} shouldn't exists\n\t2. If the path exists, then it should be a directory")
        sys.exit()

    # Creating index.html
    with open(os.path.join(project, 'index.html'), 'w') as file:
        file.seek(0)
        file.truncate()
        JS = JS_STATICS
        if tailwind:
            JS = JS_STATICS + "\n" + '\t\t<script src="https://cdn.tailwindcss.com"></script>'
        file.write(HTML_TEMPLATE % (CSS_STATICS, JS))

    # Creating StyleSheet
    if scss:
        css_file = open(os.path.join(
            project, 'statics\\css\\style.scss'), 'w')
    else:
        css_file = open(os.path.join(
            project, 'statics\\css\\style.css'), 'w')
    css_file.seek(0)
    css_file.truncate()
    css_file.write(CSS_TEMPLATE)

    # Creating JavaScript File
    with open(os.path.join(project, 'statics\\js\\app.js'), 'w') as file:
        pass

    print(f"{Fore.LIGHTGREEN_EX}Generated Successfully")
    print(f"{Fore.LIGHTBLUE_EX}cd {project}")
    print(f"{Fore.LIGHTBLUE_EX}code .")
    print(f"{Fore.LIGHTBLUE_EX}Happy Coding!!!")