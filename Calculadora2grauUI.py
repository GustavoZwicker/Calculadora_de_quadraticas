# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:37:24 2021

@author: GUSTAVOGRANDISOLLIZW
"""

import PySimpleGUI as sg
from math import sqrt


class Calculator:
    
    def __init__(self):
        
        layout = [
            [sg.Text('Equação: ',size=(8,0)),sg.Input(size=(40,0))],
            [sg.Button('Calcular')],
            [sg.MLine(size=(48,2),disabled=True,key='output',no_scrollbar=True)]
            ]
        
        self.window = sg.Window('Calculadora de Equações de segundo grau').layout(layout) 
        self.output = self.window.FindElement('output')
        
    def Calcular(self):
        
        while True:
            self.button, self.equation = self.window.Read()
            
            #Tratamento da equação inputada pelo usuário, transformando-a em uma lista
            treatedEq = self.equation[0].replace(' ','').replace('+',' ')\
                    .replace('-',' -').replace('=0','').replace('=',' -')\
                    .replace('--','').strip().split(' ')
            
            #Valor base do A,B,C da equação
            a,b,c = 0,0,0
        
        
            #Esse 'try' irá tentar rodar o código da linha 20 até 40
            try:
                #Varredura da lista treatedEq e alteração dos valores de A,B,C
                for x in treatedEq:
                    if x.find('x²') != -1:
                        if x.find('-x²') != -1:
                            a = -1
                        elif len(x) > 2:
                            a = int(x.replace('x²',''))
                        else:
                            a = 1
                    elif x.find('x') != -1:
                        if x.find('-x') != -1:
                            b = -1
                        if len(x) > 1:
                            b = int(x.replace('x',''))
                        else:
                            b = 1
                    else:
                        c = int(x)
            
            
                #Cálculo do delta
                delta = pow(b,2) - 4 * a * c
            
            
                #Cálculo do x
                x1 = (-b + sqrt(delta)) / (2*a)
                x2 = (-b - sqrt(delta)) / (2*a)
            
            
                #Escreve no output o resultado da equação
                self.output.Update(disabled=False)
                self.output.Update(f'X1 = {x1}\nX2 = {x2}')
                self.output.Update(disabled=True)
        
            #Esse 'except' será executado caso ocorra algum erro nas linhas anteriores até o 'try'
            except:
                self.output.Update(disabled=False)
                self.output.Update('\nx = Vazio')
                self.output.Update(disabled=True)

        
calculadora = Calculator()

calculadora.Calcular()