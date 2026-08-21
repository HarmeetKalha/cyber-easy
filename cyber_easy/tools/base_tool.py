from abc import ABC, abstractmethod

class Tool(ABC):
    def __init__(self, toolName, toolDescription):
        self.toolName = toolName
        self.toolDescription = toolDescription
    
    @abstractmethod
    def run(self):
        pass
    
    
    def display_info(self):
        return f"TOOL NAME: {self.toolName} \nDESCRIPTION: {self.toolDescription}"