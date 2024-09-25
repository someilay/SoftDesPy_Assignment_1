from abc import ABC
from op import Operator


class Plugin(ABC):
    def __init__(self, name: str, op: Operator):
        super().__init__()
        self.name = name
        self.op = op

    def create_route(self):
        return {
            "path": f"/plugins/{self.name}",
            "endpoint": self.op.get_endpoint(),
            "description": self.op.desc,
        }
