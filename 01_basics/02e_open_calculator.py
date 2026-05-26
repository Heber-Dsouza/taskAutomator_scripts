from classes.programs.calculator import Calculator

def init():
    calc1 = Calculator()

    calc2 = Calculator()

    print(calc1.running_stack)
    print(calc2.running_stack)

if __name__ == '__main__':
    init()
