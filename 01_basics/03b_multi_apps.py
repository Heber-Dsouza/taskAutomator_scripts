from classes.programs.calculator import Calculator

def init():
    calc1 = Calculator()
    calc1.open()
    calc2 = Calculator()
    calc2.open()
    # calc1.sum(12, 12)
    # calc2.close()
    # calc1.close()


if __name__ == '__main__':
    init()