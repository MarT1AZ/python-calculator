class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        while a > b:
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        while b <= a:
            a = a - b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(1, 2))        # Output: 3
    print(calc.subtract(5, 3))   # Output: 2
    print(calc.multiply(4, 3))   # Output: 12
    print(calc.divide(10, 2))    # Output: 5.0
    print(calc.modulo(13, 2))    # Output: 1