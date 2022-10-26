import re

i = r"https://exp.cdn-hotels.com/hotels/37000000/36790000/36789900/36789845/c229d8d5_{size}.jp"
#c = re.sub(r"\B{size}", "z", i)
#print(c)

a = re.sub(r'{size}', 'z', i)
print(a)