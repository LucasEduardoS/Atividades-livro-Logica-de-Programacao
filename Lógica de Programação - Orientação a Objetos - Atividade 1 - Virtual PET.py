# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:34:01 2022

Lógica de Programação - Orientação a Objetos - Atividade 1:
Virtual PET
Objetivo: Exercitar a técnica de abstração para identificar 
objetos e classes possíveis na criação de um sistema
Tarefa: Exercitar a identificação e criação de classes e objetos
Problema: Crie um programa que represente um jogo de pets 
virtuais usando objetos
@author: Lucas Eduardo
"""
def main():
    
    class ANIMAL:
        def NASCER(NASCER, N, C, F):
            NASCER.NOME = N
            NASCER.CLASSE = C
            NASCER.FAMILIA = F
            NASCER.CALORIA = 10
            NASCER.FORCA = 10
            NASCER.ESTADO = True
            NASCER.IDADE = 0
    
        def MORRER(MORRER):
            MORRER.ESTADO = False
            MORRER.FORCA = 0
            return print("Morto!")
        
        def COMER(COMER):
            if(ANIMAL.ESTADO and ANIMAL.FORCA > 10):
                ANIMAL.CALORIA = ANIMAL.CALORIA + 20
                ANIMAL.FORCA = ANIMAL.FORCA - 10
            elif(ANIMAL.ESTADO):
                print("O animal está morto e não pode comer!")
            else:
                print("O animal está exausto! Faça-o dormir um pouco!")
                
        def CORRER(CORRER):
            if(ANIMAL.ESTADO and ANIMAL.FORCA > 10 and ANIMAL.CALORIA > 10):
                ANIMAL.CALORIA = ANIMAL.CALORIA - 10
                ANIMAL.FORCA = ANIMAL.FORCA - 10
            elif(ANIMAL.ESTADO):
                print("O animal está morto e não pode correr!")
                if(ANIMAL.CALORIA < 10):
                    print("O animal está fraco! Faça-o comer!")
                else:
                    print("O animal está exausto! Faça-o dormir!")
        
        def DORMIR(DORMIR):
            if(ANIMAL.ESTADO):
                ANIMAL.CALORIA = ANIMAL.CALORIA - 5
            else:
                print("O animal está morto!")
main()


