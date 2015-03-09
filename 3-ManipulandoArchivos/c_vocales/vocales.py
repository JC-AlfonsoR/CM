# -*- coding: utf-8 -*-
"""
vocales
@author: J. Camilo
Python 3.4

Solution for computational methods homework 3
"""

""" Solucion
1. Pedir el numero de lineas por parametro
2. Definir funcion que identifique vocales
"""
import unicodedata

def is_vowel(V):
    """
    'v' string de 1 caracter para validar si es vocal
    Pude recibir strings en mayusculas y minusculas sin problema
    No identifica las vocales si tienen algun acento
    """
    s = V.lower()
    vowels = "aeiou"
    a = 0;
    i = 0;
    for v in vowels:
        if(v==s): #Verificar que sea alguna de las vocales en vowels
            return True
            break
        else:
            i+=1
    if(i==len(vowels)):
        return False
    
    
def c_vowel(s):
    """
    Return the number of vowels in string 's'
    """
    c = 0
    for l in s:
        if(is_vowel(l)):
            c+=1
    return c
    
nn = input("Porfavor escriba cuantas lineas [int] quiere analizar: ")
n = int(nn)

SB = open("Sainte-Beuve.txt","r")
n1 = 116-1 #Desde la linea 116 empieza el texto

for i in range(n1):
    SB.readline()
    #Leer las lineas que contienen el preambulo del texto
    #Estas lineas no se van a usar

C = 0 #Contador de vocales
i = 1#contador de lineas
for i in range(n): #Leer las primeras 'n' lineas del texto
    s = SB.readline() #leer linea
    ss = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    #Quitar el acento de las vocales acentuadas
    sss = ''.join(e for e in ss if e.isalnum()) #Extraer solo caracters alfa-num
    c = c_vowel(sss)
    print("\nLinea ",n1+i,"--- ",c," vocales")
    C = C+c
    
print("\nEl numero total de vocales, en las ",n," primeras lineas del texto, \
es de:",C)
SB.close()

"""
Falta modificar is_vowel para que lea tambien las vocales con acento
"""