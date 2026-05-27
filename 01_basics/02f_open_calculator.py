from classes.programs.calculator import Calculator

def init():
    calc1 = Calculator()
    calc2 = Calculator()

    calc1.open()
    calc1.sum(1, 11)
    calc2.run()
    calc1.open()

if __name__ == '__main__':
    init()
