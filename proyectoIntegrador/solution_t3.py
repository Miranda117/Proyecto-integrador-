# -*- coding: utf-8 -*-

from airportUI import User_op

#Esto es lo que inicia el programa
if __name__ == '__main__':
    while 1: 
        menu_1=User_op()
        principal_menu=menu_1.menu()
        if principal_menu ==4:
            break
        else :
            pass
