class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]  
        self.current_index = 0  
        self.max_index = 0  

    def visit(self, url: str) -> None:
        self.current_index += 1  
        if self.current_index < len(self.history):
            self.history[self.current_index] = url 
        else:
            self.history.append(url) 
        self.max_index = self.current_index 

    def back(self, steps: int) -> str:
        self.current_index = max(0, self.current_index - steps)  
        return self.history[self.current_index]  

    def forward(self, steps: int) -> str:
        self.current_index = min(self.max_index, self.current_index + steps) 
        return self.history[self.current_index] 
