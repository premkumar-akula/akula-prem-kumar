class Calculator:
    def __init__(self, a, b, operator):
        self.a = float(a)       # double
        self.b = float(b)       # double
        self.operator = operator

    def calculate(self):
        if self.operator == '+':
            return self.a + self.b
        elif self.operator == '-':
            return self.a - self.b
        elif self.operator == '*':
            return self.a * self.b
        elif self.operator == '/':
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Invalid operator"


a = input("Enter a value: ")
b = input("Enter b value: ")
op = input("Enter an operator (+, -, *, /): ")


calc = Calculator(a, b, op)


print("Result:", calc.calculate())
