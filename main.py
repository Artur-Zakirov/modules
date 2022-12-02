import application.salary as app_salary
import application.db.people as app_people
import datetime
from dirty_main import *

if __name__ == "__main__":
    print(datetime.datetime.now())
    foo()
    foo_1()
    app_people.get_employees()
    app_salary.calculate_salary()

