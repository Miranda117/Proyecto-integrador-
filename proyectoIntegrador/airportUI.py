# -*- coding: utf-8 -*-
from airportDP import Options_to_modify , Write_correct


class User_op : 
    def menu (self):
        print ("choose the option of your choice \n\r\t1.- Generate a report\n\r\t2.-Add data\n\r\t3.-Chage data\n\r\t4.-exit the program")
        option=int(input())
        if option ==1 :
            # COLOca LA CLASE 
            pass    
        elif option==2:
            pass

        elif option==3 :
            print ("\n\r\t1.-Correct pilot data\n\r\t2.-Correcta attendant\n\r\t3.-Correct travellers data\n\r\t4.-Correct passengers data\n\r\t5.-Correct flights data") 
            op=int(input())
            if op ==1:
                op_p= Options_to_modify()
                op_p.modify_pilot_op()
            elif op==2:
                opt=Options_to_modify()
                opt.modify_attendants_op()
            elif op==3:
                op_trave=Options_to_modify()
                op_trave.modify_travellers_op()
            elif op==4:
                op_passenger=Options_to_modify()
                op_passenger.modify_passenger_op 
                
            elif op==5:
                op_flight_=Options_to_modify()
                op_flight_.modify_flight_op()

        elif option == 4:
            write_att= Write_correct()
            write_att.write_attendants()
            print("Se estan guradando los datos ")
            #a=Write_correct()
            #a.write_flight_co()
            print("Espere un momento")
            #b=Write_correct()
            #b.write_passen_co
            print("Ya casi acabamos")
            #c=Write_correct()
            #c.write_pilot_co()
            print("Terminamos")
            #d=Write_correct()
            #d.write_travellers_co
        else:
            pass
        return option

    def dateInfo(self):
        print("ingrese fecha para generar reporte (YYMMDD): ")
        yymmdDate = int(input())
        return yymmdDate

    def timeInfo(self):
        print("Ingrese hora para generar reporte (HHMM): ")
        hhmmTime = int(input())
        return hhmmTime
