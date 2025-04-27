import re
regex = r'[а-яА-ЯЁё]'
words1 = 'j'
words2 = 'абв'


res1 = all(map(lambda x: re.findall(regex, x), words1))
res2 = all(map(lambda x: re.findall(regex, x), words2))

print(res1, res2)
