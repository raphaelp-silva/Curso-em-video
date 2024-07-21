
from math import asin, acos, atan, radians

an = float(input('Digite o angulo desejado: '))
sen = asin(radians(an))
cos = acos(radians(an))
tan = atan(radians(an))

print (f'O angulo {an} tem como seno {sen:.2f}, cosseno {cos:.2f} e tangente {tan:.2f}')