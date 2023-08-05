from colorama import Fore
from .constants import *
from .Print import *
import subprocess
import json
import sys
import os

__all__ = ['generate_vanilla']


def generate_vanilla(project: str, scss: bool, package_manager: str, tailwind: bool):
    # Creating Vite
    result = subprocess.call(
        f"npm create vite@latest {project} -- --template vanilla --pm {package_manager}", shell=True)
    if result == 0:
        project_abs = os.path.abspath(project)
        print(f"\033[9A\033[0J")
        Print.general(f"Scaffolding project in {project_abs}...\n")
        # print(f"\033[0J")
    else:
        Print.error("Error occured while initializing project")
        sys.exit(1)
    os.chdir(project)

    Print.progress_s("Re-Structuring Project Structure")
    try:
        # Removing Unwanted files
        os.remove("counter.js")
        os.remove("javascript.svg")
        os.remove("main.js")
        os.remove("style.css")

        # Making static folder
        os.makedirs("statics\\css")
        os.mkdir("statics\\js")

        # Creating Stylesheet
        if scss:
            css_file = open("statics\\css\\style.scss", 'w')
        else:
            css_file = open("statics\\css\\style.css", 'w')
        css_file.seek(0)
        css_file.truncate()
        if tailwind:
            css_file.write(TAILWIND_DIRECTIVES + "\n" + CSS_TEMPLATE)
        else:
            css_file.write(CSS_TEMPLATE)
        css_file.close()

        # Creating JavaScript
        with open('statics\\js\\app.js', "w") as file:
            file.seek(0)
            file.truncate()
            if scss:
                file.write('import "../css/style.scss"')
            else:
                file.write('import "../css/style.css"')

        # Creating index.html
        with open("index.html", "w") as file:
            file.seek(0)
            file.truncate()
            file.write(HTML_TEMPLATE)
        print(f"\033[1A\033[2K")
        Print.success("Project Restructured successfully ✓\n")
    except Exception as e:
        Print.error(
            "Following Error Occured while re-structuring project directory. Although, Project has been initialized successfully\n", str(e))

    # Reading Package.json file
    with open('package.json', 'r') as file:
        package: dict = json.load(file)
    dep = " ".join(package.get('dependencies', {}).keys()).strip()
    dev = " ".join(package.get('devDependencies', {}).keys()).strip()

    Print.progress_st("Installing Following Packages")
    if len(dep) > 0:
        Print.progress_st(f"    dependencies: {dep}", arrow='')
    if len(dev) > 0:
        Print.progress_st(f"    devDependencies: {dev}", arrow='')

    # Installing Packges
    result = subprocess.run("npm install", shell=True,
                            capture_output=True, text=True)
    if result.returncode != 0:
        error = result.stderr
        Print.error(f"Error Occured while installing dependencies\n{error}")
    else:
        Print.success("Packages Installed Successfully ✓\n")

    # Installing devDependencies
    if any([scss, tailwind]):
        Print.progress_s("Installing additional dev-dependency")

        if scss:
            result = subprocess.run(
                "npm install -D sass", shell=True, capture_output=True, text=True)

            if result.returncode != 0:
                error = result.stderr
                Print.error(
                    f"Error Occured while installing devDependency: sass\n{error}")
            else:
                Print.progress_s("""sass (installed)""")
        if tailwind:
            result = subprocess.run(
                "npm install -D tailwindcss postcss autoprefixer", shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                error = result.stderr
                Print.error(
                    f"Error Occured while installing devDependency: tailwindcss\n{error}")
            else:
                result = subprocess.run(
                    "npx tailwindcss init -p", capture_output=True, shell=True)
                if result.returncode == 0:
                    with open('tailwind.config.js', 'w') as file:
                        file.seek(0)
                        file.truncate()
                        file.write(TAILWINDCSS % "statics")
                    Print.progress_s(
                        """tailwindcss, postcss, autoprefixer (installed)""")
                else:
                    Print.error(
                        f"Error Occured while installing devDependency: (tailwindcss postcss autoprefixer)\n{result.stderr}")
    Print.success("\nGenerated Successfully")
    Print.code(f"cd {project}")
    Print.code(f"npm run dev")
    Print.progress_st(f"Happy Coding!!!", arrow='')
