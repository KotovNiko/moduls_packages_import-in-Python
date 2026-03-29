from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    current_date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    print(f'Программа Бухгалтерия запущена {current_date}')

    get_employees()
    calculate_salary()

    print('Программа завершена')