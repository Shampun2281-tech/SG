import os
import random
from playsound import playsound
name = "	Soviet Guy"
version = "v1.0"
def menu():
	os.system('cls||clear')
	print(" " + name + " " + (version) + "		Made by Shampun2281" )
	print("")
	print("		1 - Миссии (В разработке)")
	print("		2 - Настройки (В разработке)")
	print("		3 - Статистика (В разработке)")
	print("")
	zapros = input("	Ввод:	")
	if zapros == "1":
		missions()
	if zapros == "2":
		settings()
	if zapros == "3":
		stats()
	menu()
def missions():
	os.system('cls||clear')
	print(" " + name + " " + (version) + "		Made by Shampun2281" )
	print("")
	print("		0 - Выход")
	print("		1 - Учебка")
	print("")
	zapros = input("	Ввод:	")
	if zapros == "0":
		menu()
	missions()
def settings():
	os.system('cls||clear')
	print(" " + name + " " + (version) + "		Made by Shampun2281" )
	print("")
	print("		0 - Выход")
	print("		1 - Персонаж (В разработке)")
	print("")
	zapros = input("	Ввод:	")
	if zapros == "0":
		menu()
	settings()
def stats():
	os.system('cls||clear')
	print(" " + name + " " + (version) + "		Made by Shampun2281" )
	print("")
	print("		0 - Выход")
	print("")
	zapros = input("	Ввод:	")
	if zapros == "0":
		menu()
	stats()
menu()