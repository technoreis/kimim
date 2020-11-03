#!/usr/bin/env python3 
# -*-coding: utf-8 -*-


import os 
import sys
import webbrowser
import time

os.system("pkg install figlet")
os.system("sudo apt install figlet")
os.system("clear")

logo =  """
\33[93m
    *********************************************************
    *********************************************************
    ***  _____         _                          _       ***
    *** |_   _|__  ___| |__  _ __   ___  _ __ ___(_)___   ***
    ***   | |/ _ \/ __| '_ \| '_ \ / _ \| '__/ _ \ / __|  ***
    ***   | |  __/ (__| | | | | | | (_) | | |  __/ \__ \  ***
    ***   |_|\___|\___|_| |_|_| |_|\___/|_|  \___|_|___/  ***
    ***                                                   ***
    ***         Technoreis => V1.0 <= Technoreis          ***
    *********************************************************
    *********************************************************
"""

menu = """

 [-1-]  BEN KİMİM
 [-2-]  INSTAGRAM
 [-3-]  TELEGRAM
 [-4-]  GITHUB
 [-5-]  ÇIKIŞ YAP
 """

social = """

 [-1-]  INSTAGRAM
 [-2-]  TELEGRAM
 [-3-]  GITHUB
 [-4-]  ÇIKIŞ YAP
 """
kimim = """

BEN KİMİM :

            TECHNOREİS 

KISACA KİMSİN SORULARINI ATLATMAK
TANIŞMA FASTINI ATLATMAK İÇİN YAPILMIŞTIR 
BİLİŞİM KONUSUYLA BİLGİLİ VE BAZI ŞEYLERE İLGİLİ
ALTINA BELLİ BİR ŞEKİLDE KATAGORİZE ETTİM

________________________________________________

YETENEKLERİM : 

GÜÇ :    [************          ] %50
HIZ :    [**********************] %100
HACK :   [********************* ] %96

________________________________________________

KAMP :     [********              ]%40
PARKOUR :  [******************    ]%80
GİTAR :    [************          ]%60
KİCKBOKS : [****************      ]%70
SOLAK :    [**********************]%100
GAMER :    [*****                 ]%25
ÇEVRE :    [*                     ]%5
________________________________________________

                ---- SON  ----

"""
while(1):
    os.system("clear")
    print (logo + menu)
    secim = input("seçenek : ")
    os.system("clear")
    print(logo)
    if (secim == "1"):
        print(kimim)
        input()
    if secim == "2":
        os.system("clear")  
        webbrowser.open("https://www.instagram.com/technoreis")
    if secim == "3":
        os.system("clear")
        webbrowser.open("https://t.me/technoreis")   
    if secim == "4":
        os.system("clear")
        webbrowser.open("https://www.github.com/technoreis")          

    elif (secim == "5"):
        os.system("clear")
        os.system("figlet Tekrar Gel")
        time.sleep(0.5)
        quit()



# herkesin kendi github arşivine böyle bir şey yapmasını istiyorum hadi bakalım :D