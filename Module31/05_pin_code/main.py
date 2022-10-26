import itertools


for pin_code in itertools.product('0123456789', repeat=4):
    print(''.join(pin_code))
