# FastAPI x Vue

A simple portable web server setup tutorial

Frontend using [Vue.js](https://vuejs.org/)
Backend using [FastAPI](https://fastapi.tiangolo.com/)

[中文](/README.zh.md)

## Environment Setup

- Install [Python3](https://www.python.org/downloads/) and [Node.js](https://nodejs.org/en/download)
- Create a project folder in a suitable location (referred to as `root_dir`)
- Navigate to `root_dir`
- Create a Python virtual environment
    ```bash
    python3 -m venv .venv
    ```
- Activate the Python virtual environment
    - Windows
        ```bash
        .venv\Scripts\activate
        ```
    - Linux
        ```bash
        source .venv/bin/activate
        ```
- Install Python dependencies
    - Using [requirements.txt](/requirements.txt)
        ```bash
        pip install -r requirements.txt
        ```
    - Manually
        ```bash
        pip install fastapi[standard] pyinstaller
        ```
- Deactivate the virtual environment (optional)
    ```bash
    deactivate
    ```
- Install Vue CLI
    ```bash
    npm install @vue/cli -g
    ```

## Frontend Setup

- Navigate to `root_dir`
- Create a Vue project
    ```bash
    vue create frontend
    ```
- Remove `.git` and `.gitignore` in `root_dir/frontend` (optional)

## Frontend Development

- Navigate to `root_dir/frontend`
- Compile, run, and hot-reload
    ```bash
    vue serve
    ```
- Browse [http://localhost:8080](http://localhost:8080)

## Frontend Build

- Navigate to `root_dir/frontend`
- Compile and export resources to `root_dir/frontend/dist`
    ```bash
    vue build
    ```

## Backend Setup

- Create `root_dir/backend/app/__init__.py`
    ```python
    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles


    app = FastAPI()

    app.mount("/", StaticFiles(directory="static", html=True))

    ```
- Create `root_dir/backend/__main__.py`
    ```python
    from pathlib import Path
    import shutil
    import sys

    import fastapi_cli.cli as fastapi_cli
    import uvicorn


    if __name__ == "__main__":
        if getattr(sys, "frozen", None): # When packaged by pyinstaller
            temp_mei_path = Path(sys._MEIPASS)
            shutil.copytree(
                src=temp_mei_path / "static",
                dst=Path("static"),
                dirs_exist_ok=True,
            )

            from app import app
            
            uvicorn.run(
                app,
                host="0.0.0.0",
            )
        else: # Development stage
            shutil.copytree(
                src=Path("frontend/dist"),
                dst=Path("static"),
                dirs_exist_ok=True,
            )
            
            fastapi_cli.dev(Path("backend/app"))
            
            for pycache in Path(".").rglob("__pycache__"):
                shutil.rmtree(pycache)

    ```

## Backend Development

- Navigate to `root_dir`
- Run and hot-reload
    ```python
    python backend
    ```
- Browse [http://localhost:8000](http://localhost:8000)

## Backend Build (Project Build)

- Navigate to `root_dir`
- Export as an executable to `root_dir/dist`
    - Windows
        ```bash
        pyinstaller backend/__main__.py --onefile --add-data "static;static"
        ```
    - Linux
        ```bash
        pyinstaller backend/__main__.py --onefile --add-data "static:static"
        ```
- Rename the executable
    - You can also add `--name filename` to the command during packaging

## License

[LICENSE](/LICENSE)
