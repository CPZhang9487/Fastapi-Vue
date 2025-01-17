from pathlib import Path
import shutil
import sys

import fastapi_cli.cli as fastapi_cli
import uvicorn


if __name__ == "__main__":
    if getattr(sys, "frozen", None):  # 已被 pyinstaller 打包時
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
    else:  # 開發階段
        shutil.copytree(
            src=Path("frontend/dist"),
            dst=Path("static"),
            dirs_exist_ok=True,
        )

        fastapi_cli.dev(Path("backend/app"))

        for pycache in Path(".").rglob("__pycache__"):
            shutil.rmtree(pycache)
