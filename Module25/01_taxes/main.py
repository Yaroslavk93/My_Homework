class Property:
    def __init__(self, worth):
        self.worth = worth


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 500


class Money:

    def __init__(self, money, apartment, car, house):
        self.money = money
        self.apartment = apartment
        self.car = car
        self.house = house

    def info_money(self):
        tax_summ = self.apartment.tax() + self.car.tax() + self.house.tax()
        if self.money >= tax_summ:
            print(tax_summ)
            print('Денег хватает!')
        else:
            shortage = tax_summ - self.money
            print(f'До выплаты налога не хватает {shortage} рублей!')


man = Money(
    money=10000,
    apartment=Apartment(4000000),
    car=Car(900000),
    house=CountryHouse(2500000)
)

man.info_money()
