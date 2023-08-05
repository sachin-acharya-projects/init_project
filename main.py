from colorama import init, Fore
from packages import *
import argparse
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
        generate_plainweb(project, scss, tailwind)


main()
