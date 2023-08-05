from colorama import init, Fore
from packages import *
import argparse
import shutil
import os
import sys

init(autoreset=True)
BASE_PATH: str = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

argument_parser: argparse.ArgumentParser = argparse.ArgumentParser()
argument_parser.add_argument(
    'project', type=str, help="Name of the project to initialize")
argument_parser.add_argument(
    '--template', type=str, choices=('html', 'vanilla'), help="Templates for the Project", default="html")
argument_parser.add_argument(
    '--pm', type=str, help="Package Manager for the project", default='npm')
argument_parser.add_argument(
    "--scss", action="store_true", help="Use SCSS preprocessor or not", default=True)
argument_parser.add_argument(
    '--tailwind', action='store_true', help="Initialize Tailwaindcss?", default=False)

parser = argument_parser.parse_args()


def main():
    project: str = parser.project
    template: str = parser.template
    package_manager: str = parser.pm
    scss: bool = parser.scss
    tailwind: bool = parser.tailwind

    if template == 'vanilla':
        generate_vanilla(project, scss, package_manager, tailwind)
    elif template == 'html':
        try:
            os.makedirs(f"{project}\\statics\\css")
            os.mkdir(f"{project}\\statics\\js")
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}Project Initialization Failed (Invalid Path). Please make sure following conditions applies\n\t1. The path {project} shouldn't exists\n\t2. If the path exists, then it should be a directory")
            sys.exit()
        shutil.copy(BASE_PATH + "\\templates\\html\\index.html", project)
        if scss:
            shutil.copy(BASE_PATH + "\\templates\\html\\style.css",
                        f"{project}\\statics\\css\\style.scss")
            shutil.copy(BASE_PATH + "\\templates\\html\\variables.css",
                        f"{project}\\statics\\css\\variables.scss")
        else:
            shutil.copy(BASE_PATH + "\\templates\\html\\style.css",
                        f"{project}\\statics\\css\\style.css")
            shutil.copy(BASE_PATH + "\\templates\\html\\variables.css",
                        f"{project}\\statics\\css\\variables.css")
        shutil.copy(BASE_PATH + "\\templates\\html\\app.js",
                    f"{project}\\statics\\js\\app.js")

        print(f"{Fore.LIGHTGREEN_EX}Generated Successfully")
        print(f"{Fore.LIGHTBLUE_EX}cd {project}")
        print(f"{Fore.LIGHTBLUE_EX}code .")
        print(f"{Fore.LIGHTBLUE_EX}Happy Coding!!!")


main()
