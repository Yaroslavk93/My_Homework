import re


reg_marks = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
private_car = re.findall(r'\D\d{3}\D{2}\d{2,3}', reg_marks)
taxi = re.findall(r'\w{2}\d{5,6}', reg_marks)

print(f'Список номеров частных автомобилей: {private_car}')
print(f'Список номеров такси: {taxi}')
