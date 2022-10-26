students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


num, age = [i_key for i_key in students], [i_value['age'] for _, i_value in students.items()]
print('Список пар "ID студента - Возраст":', list(zip(num, age)))

interest = {i for _, i_value in students.items() for i in i_value['interests']}
print('Полный список интересов всех студентов:', interest)

surname = [j for _, i_value in students.items() for j in i_value['surname']]
print('Общая длина всех фамилий студентов:', len(surname))

