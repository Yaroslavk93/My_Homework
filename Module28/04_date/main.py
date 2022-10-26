class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'День: {self.day}\t' \
               f'Месяц: {self.month}\t' \
               f'Год: {self.year}'

    @classmethod
    def from_string(cls, date_list) -> 'Date':
        day, month, year = map(int, date_list.split('-'))
        return cls(day, month, year)

    @classmethod
    def is_date_valid(cls, date_list) -> bool:
        day, month, year = map(int, date_list.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
