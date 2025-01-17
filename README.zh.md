# FastAPI x Vue

簡易的攜帶式網頁伺服器建置教學

前端使用 [Vue.js](https://vuejs.org/)
後端使用 [FastAPI](https://fastapi.tiangolo.com/)

[English](/README.md)

## 環境建置

- 安裝 [Python3](https://www.python.org/downloads/) 與 [Node.js](https://nodejs.org/zh-tw/download)
- 在合適的地方建立專案資料夾 (以下簡稱為 `root_dir`)
- 進入 `root_dir`
- 建立 Python 的虛擬環境
    ```bash
    python3 -m venv .venv
    ```
- 進入 Python 虛擬環境
    - Windows
        ```bash
        .venv\Script\activate
        ```
    - Linux
        ```bash
        source .venv/bin/activate
        ```
- 安裝 Python 所需依賴
    - 使用 [requirements.txt](/requirements.txt) 安裝
        ```bash
        pip install -r requirements.txt
        ```
    - 手動安裝
        ```bash
        pip install fastapi[standard] pyinstaller
        ```
- 退出虛擬環境 (可選)
    ```bash
    deactivate
    ```
- 安裝 Vue Cli
    ```bash
    npm install @vue/cli -g
    ```

## 前端建置

- 進入 `root_dir`
- 建立 Vue 專案
    ```bash
    vue create frontend
    ```
- 刪除 `root_dir/frontend`中的 `.git` 與 `.gitignore` (可選)

## 前端開發

- 進入 `root_dir/frontend`
- 編譯運行並熱重載
    ```bash
    vue serve
    ```
- 瀏覽 [http://localhost:8080](http://localhost:8080)

## 前端匯出

- 進入 `root_dir/frontend`
- 編譯並匯出資源到 `root_dir/frontend/dist`
    ```bash
    vue build
    ```

## 後端建置

- 建立 `root_dir/backend/app/__init__.py`
    ```python
    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles


    app = FastAPI()

    app.mount("/", StaticFiles(directory="static", html=True))

    ```
- 建立 `root_dir/backend/__main__.py`
    ```python
    from pathlib import Path
    import shutil
    import sys

    import fastapi_cli.cli as fastapi_cli
    import uvicorn


    if __name__ == "__main__":
        if getattr(sys, "frozen", None): # 已被 pyinstaller 打包時
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
        else: # 開發階段
            shutil.copytree(
                src=Path("frontend/dist"),
                dst=Path("static"),
                dirs_exist_ok=True,
            )
            
            fastapi_cli.dev(Path("backend/app"))
            
            for pycache in Path(".").rglob("__pycache__"):
                shutil.rmtree(pycache)

    ```

## 後端開發

- 進入 `root_dir`
- 運行並熱重載
    ```python
    python backend
    ```
- 瀏覽 [http://localhost:8000](http://localhost:8000)

## 後端匯出 (=專案匯出)

- 進入 `root_dir`
- 匯出成可執行檔至 `root_dir/dist`
    - Windows
        ```bash
        pyinstaller backend/__main__.py --onefile --add-data "static;static"
        ```
    - Linux
        ```bash
        pyinstaller backend/__main__.py --onefile --add-data "static:static"
        ```
- 重新命名可執行檔
    - 也可在打包時在命令加上 `--name filename`

## 授權條款

[LICENSE](/LICENSE)
