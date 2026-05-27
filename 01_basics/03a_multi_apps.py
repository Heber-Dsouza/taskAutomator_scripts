from classes.programs.calculator import Calculator
from classes.programs.libre_office.writer import Writer

def init():
    calc1 = Calculator()
    writer1 = Writer()


    calc1.open()
    writer1.open()
    calc1.open()
    writer1.open()


if __name__ == '__main__':
    init()