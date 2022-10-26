while True:
  password = list(input('Придумайте пароль: '))
  letter = len([letter + 1 for letter in range(len(password)) if password[letter].istitle()])
  digit = len([digit for digit in range(len(password)) if password[digit].isdigit()])
  if len(password) > 8 and letter >= 1 and digit >= 1:
    print('Это надёжный пароль!')
    break
  else:
    print('Пароль ненадёжный. Попробуйте ещё раз.\n')