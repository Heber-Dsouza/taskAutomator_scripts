from classes.programs.calculator import Calculator
from classes.programs.libre_office.writer import Writer

def init():
    calc1 = Calculator()
    calc1.run()
    writer1 = Writer()
    writer1.run()
    calc2 = Calculator()
    calc2.run()
    calc2.sum(100, 100)
    calc1.sum(12, 12)
    calc2.sum(400, 400)
    calc1.close()
    writer1.close()
    calc2.close()


if __name__ == '__main__':
    init()