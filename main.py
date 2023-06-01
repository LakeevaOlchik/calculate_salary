from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import date

def current_date():
    current_date = date.today()
    print(current_date)

if __name__ == '__main__':
    current_date()
    calculate_salary()
    get_employees()



