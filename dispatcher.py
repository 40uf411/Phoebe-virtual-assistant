from plugins.callbacks import Callbacks

class Dispatcher:
    def __init__(self) -> None:
        self.plugins = Callbacks.plugins
    def __call__(self, command:str):
        return self.dispatch(command)
    
    def dispatch(self, command:str):
        tokens = command.split()
        
        if tokens[0] == 'time':
            resolver = self.plugins['time']()
        elif tokens[0] == 'ping':
            resolver = self.plugins['ping']()
        elif tokens[0] == 'calendar':
            resolver = self.plugins['calendar']()
        else:
            return {"msg":"Sorry commad not found", "content":None}
        return resolver(command)

if __name__ == '__main__':
    d = Dispatcher()
    print(d("time"))