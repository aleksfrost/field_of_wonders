import re
regex = r'[а-яА-ЯЁё]'
words1 = 'абвгд'
words2 = 'абвгдy'

res1 = all(map(lambda x: re.findall(regex, x), words1))
res2 = all(map(lambda x: re.findall(regex, x), words2))

print(res1, res2)
