
class Plugin:
    def __init__(self, plugin=None) -> None:
        pass
    def __call__(self, command):
        return self.execute(command)
    def execute(command):
        return {"msg":"Sorry commad not found", "content":None}