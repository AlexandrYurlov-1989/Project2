import textwrap  
 
a = input('Введите строку:')
print(''.join(reversed((a[-2:]))))  
print(a[:-3:-1])
