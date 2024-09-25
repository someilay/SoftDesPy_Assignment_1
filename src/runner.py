import uvicorn
from types import ModuleType
from pathlib import Path
from fastapi import FastAPI
from plugin import Plugin


class ExtendableWebApp:
    def __init__(self, host: str = "localhost", port: int = 8000) -> None:
        self.app = FastAPI()
        self.host = host
        self.port = port
        self.plugins = {}

        self.app.get("/list")(lambda: list(self.plugins.keys()))
        self.app.get("/")(lambda: "Use /list to see plugins list")

    def add_plugin(self, plugin: Plugin):
        if plugin.name in self.plugins:
            raise ValueError(f"{plugin.name} is duplicate")
        self.plugins[plugin.name] = plugin
        self.app.add_api_route(**plugin.create_route(), methods=["GET"])

    def add_plugins(self, module: ModuleType):
        path = Path(module.__path__[0])
        modules = [i.stem for i in path.iterdir() if i.is_file() and i.name.endswith(".py")]
        for sub_name in modules:
            submodule = __import__(f"plugins.{sub_name}")
            self.add_plugin(getattr(submodule, sub_name).plugin)

    def run(self):
        uvicorn.run(self.app, host=self.host, port=self.port)
