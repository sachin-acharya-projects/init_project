VITE_ICON: str = '<link rel="icon" type="image/svg+xml" href="/vite.svg" />'
JS_MODULE: str = '<script type="module" src="./statics/js/app.js"></script>'
CSS_STATICS: str = '<link rel="stylesheet" href="./statics/css/style.css" />'
JS_STATICS: str = '<script src="./statics/js/app.js"></script>'

GITIGNORE: str = """.vite

# Logs
logs
*.log

dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
"""

HTML_TEMPLATE: str = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        %s

        <title>Vite App</title>
    </head>
    <body>

        %s
    </body>
</html>
"""

CSS_TEMPLATE: str = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
    line-height: 1.5;
    font-weight: 400;

    color-scheme: light dark;
    color: rgba(255, 255, 255, 0.87);
    background-color: #242424;

    font-synthesis: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    -webkit-text-size-adjust: 100%;
}

a {
    font-weight: 500;
    color: #646cff;
    text-decoration: inherit;
}

a:hover {
    color: #535bf2;
}

body {
    margin: 0;
    display: flex;
    min-width: 320px;
    min-height: 100vh;
}

h1 {
    font-size: 3.2em;
    line-height: 1.1;
}

button {
    border-radius: 8px;
    border: 1px solid transparent;
    padding: 0.6em 1.2em;
    font-size: 1em;
    font-weight: 500;
    font-family: inherit;
    background-color: #1a1a1a;
    cursor: pointer;
    transition: border-color 0.25s;
}

button:hover {
    border-color: #646cff;
}

button:focus,
button:focus-visible {
    outline: 4px auto -webkit-focus-ring-color;
}

@media (prefers-color-scheme: light) {
    :root {
        color: #213547;
        background-color: #ffffff;
    }

    a:hover {
        color: #747bff;
    }

    button {
        background-color: #f9f9f9;
    }
}
"""

TAILWINDCSS: str = """/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./%s/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {},
    },
    plugins: [],
}
"""

TAILWIND_DIRECTIVES: str = """@tailwind base;
@tailwind components;
@tailwind utilities;
"""
