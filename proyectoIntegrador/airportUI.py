# -*- coding: utf-8 -*-
from airportDP import Options_to_modify , Write_correct, Add_data, Catch_data, Csv



class User_op : 
    def menu (self):
        print ("choose the option of your choice \n\r\t1.- Generate a report\n\r\t2.-Add data\n\r\t3.-Chage data\n\r\t4.-exit the program")
        option=int(input())
        if option ==1 :
             Csv().csv_writer()

        elif option==2:
            print("choose the kind of data you want to add \n\r\t1.- Add flight\n\r\t2.- Add traveller\n\r\t3.-Add passenger\n")
            op=int(input())
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
                global new_flight
                new_flight=Catch_data().document_flight(id, plate, origin, destiny, departure, take_off_track, arriving_gate, landing_track, pilot, copilot, attendants)

            elif op==2:
                passport=str(input("Write passport to add(AA####): "))
                forename = str(input("Write forename to add: "))
                surname = str(input("Write surname to add: "))
                date_of_birth = str(input("Write date of birth to add(YYMMDD): "))
                country = str(input("Write country to add: "))
                gender = str(input("Write gender to add(M ,F, NA): "))
                marital_status = str(input("Write marital status to add(Single, Married, Widowed, Divorced): "))
                traveller=Add_data()
                all_travellers=traveller.add_traveller(passport, forename, surname, date_of_birth, country, gender, marital_status)
                global new_traveller
                new_traveller=Catch_data().document_traveller(passport, forename, surname, date_of_birth, country, gender, marital_status)

            elif op==3:
                flight=str(input("Write flight to add(AA###): "))
                passport = str(input("Write passport to add(AA####): "))
                flight_class = str(input("Write class to add: "))
                seat = str(input("Write seat to add(##A): "))
                location = str(input("Write location to add(check-in, security, boarded): "))
                passenger=Add_data()
                all_passengers=passenger.add_passenger(flight, passport, flight_class, seat, location)
                global new_passenger
                new_passenger=Catch_data().document_passenger(flight, passport, flight_class, seat, location)


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
                print("Did you add data?\n1.-yes\n2.-no\n ")
                op=int(input("choose an option: "))
                if op==1:
                    print("select the type of data you added\n1.-new passenger\n2.-new traveller\n3.-new flight")
                    opt=int(input("choose an option: "))
                    if opt==1:
                        Catch_data().WritePassenger(new_passenger)
                    elif opt==2:
                        Catch_data().WriteTraveller(new_traveller)
                    elif opt==3:
                        Catch_data().WriteFlight(new_flight)
                elif op==2:
                    print("...ending program...")


        return option

    

