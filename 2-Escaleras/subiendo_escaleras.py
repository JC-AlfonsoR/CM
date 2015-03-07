# -*- coding: utf-8 -*-
"""
subiendo_escaleras.py
@author: J. Camilo
Python 3.4

Solution for computational methods homework 3
"""
print("Subiendo Escaleras\n")

"""Pasos para resolver el problema

La subida de las escaleras se comporta como serie de Fibonacci

1. Definir Funcion de Fibonacci para las escaleras
    La voy a llamar Fibo_s(n)
2. Imprimir resultados para N = [13, 15]

"""

def Fibo_s(N):
    """
    Devuelve el número de formas diferentes para subir una escalera de N [int]
    escalones, dado que solo se puede subir de a 1 o 2 escalones en cada 
    tiempo.
    """
    if(N==0): 
        return 1
    elif N==1:
        return 1
    else:
        return Fibo_s(N-1)+Fibo_s(N-2)
    
def Escaleras(A,B):
    """
    A y B son arreglos Lx1 de enteros
    """
    #Validar Datos    
    if len(A)!=len(B):
        print("Error, los arreglos A y B deben ser del mismo tamaño")
    else:    
        L = len(A)
        C = [0]*L
        
        for i in range(L):
            a = A[i]
            b = B[i]
            c = Fibo_s(a%(2*b)) #Calcular cada elemento c
            C[i] = c
        return C
#%% Punto a
print("Dadas las reglas para subir la escalera:\n"\
"Para N=13, se tienen", Fibo_s(13),"formas diferentes de subir la escalera\n"\
"para N=15, se tienen", Fibo_s(15),"formas diferentes de subir la escalera\n")

#%% Punto b
A = [4, 4, 5, 5, 1]
B = [3, 2, 4, 3, 1]
C = Escaleras(A,B)
print("\nA =",A,"\nB =",B,"\nC =",C)