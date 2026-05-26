from classes.programs.calculator import Calculator

def init():
    calc1 = Calculator()
    calc2 = Calculator()
    calc3 = Calculator()

    calc1.sum(1, 11)
    calc2.run()
    calc3.sum(3, 33)
    calc1.sum(4, 44)
    calc2.sum(777, 777)

if __name__ == '__main__':
    init()
