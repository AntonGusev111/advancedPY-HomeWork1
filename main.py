from application.salary import calculate_salary as calc
from application.DB.people import get_employees as get_e
from datetime import datetime

if __name__ == '__main__':
    print(datetime.date(datetime.now()))
    calc()
    get_e()