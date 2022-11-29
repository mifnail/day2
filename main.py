import datetime as dt


class Employee:
    def __init__(self, number, fio, bdate, oklad, on_live=False):
        self.number =number
        self.fio = fio
        self.bdate =bdate
        self.oklad = oklad
        self.on_live = on_live

    def increasebl_salary (self, summa):
        self.oklad+=summa

    def __str__(self):
        return f"Сотрудник {self.number}{self.fio}{self.bdate},оклад {self.oklad}, в отпуске" \
               f"{'да' if self.on_live else 'нет'}"

    def __eq__(self, other):
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate == other_bdate

    def __le__(self, other): #<
        if self.__eq__(other):
            return True
        if self.__lt__(other):
            return True
        else:
            return False

    def __lt__(self, other): #>
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate < other_bdate


def str_to_date(self_date, other_date):
    dt1 = self_date.split('.')
    dt2 = self_date.split('.')
    self_date=dt.date(int(dt1[2]),int(dt1[1]),int(dt1[0]))
    other_date = dt.date(int(dt2[2]), int(dt2[1]), int(dt2[0]))
    return self_date, other_date


class Department:
    def __init__(self, title, chief=None, employees=None):
        self.title = title
        if employees is None:
            employees = list()
        self.employees = employees
        self.chief = chief

    def append(self, emp):
        self.employees.append(emp)

    def __str__(self):
        return f"Отдел:{self.title},начальник: {self.chief}, количество сотрудников: {len(self.employees)}"

    def print_emloyees(self):
        for emp in self.employees:
            print(emp)
    def print_employees_on_live(self, status=True):
        for emp in self.employees:
            if emp.on_live==status:
                print(emp)





ivanov= Employee(1, 'Иванов',"01.01.2000",100000)
petrov = Employee(2, 'Петров',"01.01.1990",200000, True)
sidorov = Employee(3, 'Сидоров',"05.05.2005",70000, True)
print(ivanov>petrov)
print(ivanov<petrov)
print(ivanov != petrov)

arhiv= Department('Архив',employees=[petrov])
arhiv.append (ivanov)
arhiv.append (sidorov)
arhiv.print_employees_on_live(False)


