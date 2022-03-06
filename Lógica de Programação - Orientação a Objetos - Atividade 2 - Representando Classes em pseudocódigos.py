# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 23:04:50 2022

Objetivo: Fixar conceitos de OO em pseudocódigo
Tarefa: Exercitar a representação de classes presentes em diagramas
OO em pseudocódigo

@author: Lucas Eduardo
"""
def main():
    
    class Animal:
        def animal(animal, n, c, f):
            animal.nome = n
            animal.classe = c
            animal.familia = f
            animal.caloria = 10
            animal.forca = 10
            animal.estado = True
            animal.idade = 0
        
        def animal(animal, n):
            animal.nome = n
            animal.classe = "Mamífero"
            animal.familia = "Canídeo"
            animal.caloria = 10
            animal.forca = 10
            animal.estado = True
            animal.idade = 0
        
        def animal():
            animal.estado = False
            animal.forca = 0
            return print("Morto!")
        
        def comer():
            if(animal.estado and animal.forca > 10):
                animal.caloria = animal.caloria + 20
                animal.forca = animal.forca - 10
            elif(animal.estado):
                return print("O animal está morto e não pode comer!")
            else:
                return print("O animal está exausto! Faça-o dormir um pouco!")
        
        def correr():
            if(animal.estado and animal.forca > 10 and animal.caloria > 10):
                animal.caloria = animal.caloria - 10
                animal.forca = animal.forca - 10
            elif(animal.estado):
                return print("O animal está morto!")
                if(animal.caloria < 10):
                    return print("O animal está fraco! Faça-o comer!")
                else:
                    return print("O animal está exausto! Faça-o dormir!")
        
        def dormir():
            if(animal.estado):
                animal.caloria = animal.caloria - 5
                animal.forca = animal.forca + 20
                return print("O animale está morto!")
main()

