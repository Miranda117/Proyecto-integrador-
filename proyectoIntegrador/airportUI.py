# -*- coding: utf-8 -*-
from airportDP import*


class User_op :
    def menu (self):
        print ("choose the option of your choice \n\r\t1.- Generate a report\n\r\t2.-Add data\n\r\t3.-Chage data")
        option=int(input())
        if option ==1 :
            # COLOca LA CLASE 
            pass    
        if option==2:
            pass

        if option==3 :
            print ("\n\r\t1.-Correct pilot data\n\r\t2.-Correcta attendant\n\r\t3.-Correct travellers data\n\r\t4.-Correct passengers data\n\r\t5.-Correct flights data") 
            op=int(input())
            if op ==1:
                op_p=Options_to_modify()
                op_p.modify_pilot_op()
            elif op==2:
                opt=Options_to_modify()
                opt.modify_attendants_op()
            elif op==3:
                passport_tra=str(input("Enter the traveller's passport: "))
                civil_tra=str (input("Enter the new civil status: "))
                gender_tra=str (input("Enter the new gender: "))
                birthdate=str (input("Enter the new gender: "))
                forname=str(input("Enter the new forname: "))
                surname=str(input("Enter the new surname: "))
                traveller=ModificarDatos()
                traveller.modify_travellers(passport_tra,civil_tra,gender_tra,birthdate,forname,surname)
            elif op==4:
                flight=str(input("Enter the passenger's flight: "))
                passport_pass=str(input("Enter the passport: "))
                seat=str(input("Enter the new seat"))
                flight_class=str(input("Enter the new flight class"))
                location=str(input("Enter the new location"))
                passenger=ModificarDatos()
                passenger.modify_passenger_data(flight,passport_pass,seat,flight_class,location) 
                

            elif op==5:
                id_op=str(input("Enter the flight's id: "))
                plate=str(input("Enter the plane: "))
                seat=str(input("Enter the new door:"))
                track_track=str(input("Enter the new track"))
                attendants_fligth=str(input("Enter the new attendants"))
                pilot_fligth= str (input("Enter new pilot"))
                copilot=str(input("Enter new copilot"))
                fligth_fr=ModificarDatos()
                fligth_fr.modify_flight= (id_op,plate,seat,track_track,attendants_fligth,pilot_fligth,copilot)

        if option == 4:
            archivo=open("data/attendants.csv", "w+")
            a=Options_to_modify()
            dic_modificado=a.modify_attendants_op()
            for m in dic_modificado.keys():
                archivo.write(dic_modificado[m].passport )
                archivo.write(",")
                archivo.write(dic_modificado[m].forename )
                archivo.write(",")
                archivo.write(dic_modificado[m].surname)
                archivo.write(",")
                archivo.write(dic_modificado[m].date_of_birth)
                archivo.write(",")
                archivo.write(dic_modificado[m].country)
                archivo.write(",")
                archivo.write(dic_modificado[m].gender)
                archivo.write(",")
                archivo.write(dic_modificado[m].marital_status)
                archivo.write("\n")
            archivo.close()
            exit()

    def dateInfo(self):
        print("ingrese fecha para generar reporte (YYMMDD): ")
        yymmdDate = int(input())
        return yymmdDate

    def timeInfo(self):
        print("Ingrese hora para generar reporte (HHMM): ")
        hhmmTime = int(input())
        return hhmmTime
class Options_to_modify:
    def modify_attendants_op(self):
        passport_at=str(input("Enter the attendant's passport: "))
        new_marital=str (input("Enter the new marital status: "))
        correct_at= ModificarDatos()
        dic_modificado= correct_at.modify_attendants(passport_at,new_marital)
        return dic_modificado
    def modify_pilot_op(self):
        passport=str(input("Enter the pilot's passport: "))
        marital_status=str(input("Enter the new marital status: "))
        correct= ModificarDatos ()
        pilot_dic=correct.modify_pilot_data(passport, marital_status) 
        return pilot_dic
 

