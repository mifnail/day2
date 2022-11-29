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

    def __lt__(self, other): #<
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate < other_bdate


def str_to_date (self_date, other_date):
    dt1 = self_date.split('.')
    dt2 = self_date.split('.')
    self_date=dt.date(int(dt1[2]),int(dt1[1]),int(dt1[0]))
    other_date = dt.date(int(dt2[2]), int(dt2[1]), int(dt[0]))
    return self_date , other_date






ivanov= Employee(1, 'Иванов',"01.01.2000",100000)
petrov = Employee(1, 'Петров',"01.01.1990",200000)
