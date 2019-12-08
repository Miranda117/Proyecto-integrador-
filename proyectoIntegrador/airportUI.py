
# -*- coding: utf-8 -*-
from airportDP import Options_to_modify , Write_correct


class User_op : 
    def menu (self):

        global flight
        global traveller
        global passenger
        print ("choose an option: \n\r\t1.- Generate a report\n\r\t2.-Add data\n\r\t3.-Chage data")

        print ("choose the option of your choice \n\r\t1.- Generate a report\n\r\t2.-Add data\n\r\t3.-Chage data\n\r\t4.-exit the program")
        option=int(input())
        if option ==1:
            Csv().csv_writer() 
            pass    
        elif option==2:

            op=int(input(("1) flight data\n2) traveller data\n3) passenger data\nPlease choose the type of data you want to add: ")))
            if op==1:
                id=str(input("Write id to add(AA###): "))
                plate=str(input("Write plate to add: "))
                origin = str(input("Write origin to add(city or place - COUNTRY): "))
                destiny = str(input("Write destiny to add(city or place - COUNTRY): "))
                departure = str(input("Write departure to add(######_####_Continent/City): "))
                arriving = str(input("Write arriving to add(######_####_Continent/City): "))
                status = str(input("\nboarded\nboarding\nin transit\nlanded\nlanding\nwaiting\nWrite status to add: "))
                departure_gate = str(input("Write departure gate to add(A# or A##): "))
                take_off_track = str(input("Write take off track to add(#): "))
                arriving_gate = str(input("Write arriving gate to add(A# or A##): "))
                landing_track = str(input("Write landing track to add(#): "))
                pilot = str(input("Write pilot to add(AA####): "))
                copilot = str(input("Write copilot to add(AA####): "))
                attendants = str(input("Write attendants to add(AA####;AA####...): "))
                flight = Add_data()
                all_flights=Add_data().add_flight(id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, arriving_gate, landing_track, pilot, copilot, attendants)
                print(all_flights)

            elif op==2:
                
                passport=str(input("Write passport to add(AA####): "))
                forename = str(input("Write forename to add: "))
                surname = str(input("Write surname to add: "))
                date_of_birth = str(input("Write date of birth to add(YYMMDD): "))
                country = str(input("Write country to add: "))
                gender = str(input("Write gender to add(M ,F, NA): "))
                marital_status = str(input("Write marital status to add(Single, Married, Widowed, Divorced): "))
                traveller=Add_data()
                traveller.add_traveller(passport, forename, surname, date_of_birth, country, gender, marital_status)

            elif op==3:
                flight=str(input("Write flight to add(AA###): "))
                passport = str(input("Write passport to add(AA####): "))
                flight_class = str(input("Write class to add: "))
                seat = str(input("Write seat to add(##A): "))
                location = str(input("Write location to add(check-in, security, boarded): "))
                passenger=Add_data()
                passenger.add_passenger(flight, passport, flight_class, seat, location)

        elif option==3:

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
                    
        elif option == 4:
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

