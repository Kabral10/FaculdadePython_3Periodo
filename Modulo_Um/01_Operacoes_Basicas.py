import os

arquivo1 = open('01_dados1.txt', 'w', encoding='utf-8')
print(os.path.abspath(arquivo1.name))

arquivo1.write('Olá, Mundo!')

print(os.path.realpath(arquivo1.name))
print(arquivo1)

arquivo1.close()