from plugins.callbacks import Callbacks

class Dispatcher:
    def __init__(self) -> None:
        self.plugins = Callbacks.plugins
    def __call__(self, command:str):
        return self.dispatch(command)
    
    def dispatch(self, command:str):
        if "time" in command:
            resolver = self.plugins['time']()
        else:
            return {"msg":"Sorry commad not found", "content":None}
        return resolver(command)

if __name__ == '__main__':
    d = Dispatcher()
    print(d("time"))