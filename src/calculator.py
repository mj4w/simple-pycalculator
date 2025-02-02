class Calculator:
    """A simple calculator class for basic arithmetic operations."""
    
    def add(self, a:float, b:float) -> float:
        return a + b
    
    def subtract(self, a:float, b:float) -> float:
        return a - b
    
    def multiply(self, a:float, b:float) -> float:
        return a * b
    
    def divide(self, a:float, b:float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b