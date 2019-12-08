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
                op_passenger.modify_passenger_op() 
                
            elif op==5:
                op_flight_=Options_to_modify()
                op_flight_.modify_flight_op()                                                                                                                                                                                                                                                                                                                                                                                                                           

        elif option == 4:
            print ("Before leaving you could remind the program, do you correct data? \n\r\t1.-yes\n\r\t2.-No ")
            op_2 =int (input())
            if op_2 ==1:
                print ("what data you corrected \n\r\t1.-pilot data\n\r\t2.-attendant\n\r\t3.-travellers data\n\r\t4.-passengers data\n\r\t5.-flights data ")
                option_3=int(input())
                if option_3==1:
                    c=Write_correct()
                    c.write_pilot_co()

                elif option_3==2:
                    write_att= Write_correct()
                    write_att.write_attendants()
            
                elif option_3==3:
                    d=Write_correct()
                    d.write_travellers_co()

                elif option_3==4:
                    b=Write_correct()
                    b.write_passen_co()
                elif option_3==5:
                    a=Write_correct()
                    a.write_flight_co()
            elif op_2==2:
                pass
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
