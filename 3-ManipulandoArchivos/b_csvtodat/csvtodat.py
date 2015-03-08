# -*- encodigin: utf-8 -*-
#!/bin/python
#
#Python 2.7
#csvtodat.py
#
#Lee archivo Notas.csv
#Cambia las comas "," por signo "+"
#y crea el archivo Notas.dat con las modificaciones
#Requiere que exista ela rchivo Notas.csv en la misma carpeta que este script

#Importar Librerias
import os

#Solucion con Python
os.system("ls")
F = open("Notas.csv","r")
W = open("Notas.dat","w")
for line in F:
    l = line.replace(",","+")
    W.write(line.replace(",","+"))
W.close()
F.close()
os.system("ls")
print("\nThe file 'Notas.dat' has been created in the actual folder\n\n")


#Solucion con comandos de la terminal
os.system("rm Notas.dat") #Borrar el archivo para que los 'ls' demuestren que se crea el archivo
os.system("ls")
os.system("sed 's/,/+/g' Notas.csv > Notas.dat")
os.system("ls")
print("\nThe file 'Notas.dat' has been created in the actual folder\n\n")
