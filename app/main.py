from app.calculator import Calculator

def run_calculator():
    a, b = 10, 5
    print(f"Adding {a} + {b} = {Calculator.add(a, b)}")
    print(f"Subtracting {a} - {b} = {Calculator.subtract(a, b)}")
    print(f"Multiplying {a} * {b} = {Calculator.multiply(a, b)}")
    print(f"Dividing {a} / {b} = {Calculator.divide(a, b)}")
    print(f"Squaring {a} = {Calculator.square(a)}")
    print(f"Cubing {a} = {Calculator.cube(a)}")

    print(f"Last calculation: {Calculator.get_last_calculation()}")

if __name__ == "__main__":
    run_calculator()
