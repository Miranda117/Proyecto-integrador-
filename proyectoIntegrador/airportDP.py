import csv
from collections import ChainMap

class Passengers:
	def __init__(self, _flight, _passport, _flight_class, _seat, _location):
		self.flight = _flight
		self.passport = _passport
		self.flight_class = _flight_class
		self.seat = _seat
		self.location = _location

class Planes:
	def __init__(self, _plate, _manufacturer, _model, _passengers_capacity, _luggage_capacity, _max_speed):
		self.plate = _plate
		self.manufacturer = _manufacturer
		self.model = _model
		self.passengers_capacity = _passengers_capacity
		self.luggage_capacity = _luggage_capacity
		self.max_speed = _max_speed


class Pilot:#
	def __init__(self, _passport, _forename, _surname, _date_of_birth, _country, _marital_status, _gender):
		self.passport = _passport
		self.forename = _forename
		self.surname = _surname
		self.date_of_birth = _date_of_birth
		self.country = _country
		self.gender = _gender
		self.marital_status = _marital_status

class Attendants(Pilot):
	pass

class Flights:
	def __init__(self, _id, _plate, _origin, _destiny, _departure, _arriving, _status, _departure_gate, _take_off_track, _arriving_gate, _landing_track, _pilot, _copilot, _attendants):
		self.id = _id
		self.plate = _plate
		self.origin = _origin
		self.destiny = _destiny
		self.departure = _departure
		self.arriving = _arriving
		self.status = _status
		self.departure_gate = _departure_gate
		self.take_off_track = _take_off_track
		self.arriving_gate = _arriving_gate
		self.landing_track = _landing_track
		self.pilot = _pilot
		self.copilot = _copilot
		self.attendants = _attendants

#Esta clase, así como attendants, van de inicio con el pass porque, a diferencia de las demás, es más conveniente que se inicialice de esa forma
class Travellers(Pilot):#
	pass#

class Catch_data:
	#flight tools
	def document_flight(self, id, plate, origin, destiny, departure, take_off_track, arriving_gate, lading_track, pilot, copilot, attendants):
		documented_info=[id, plate, origin, destiny, departure, take_off_track, arriving_gate, lading_track, pilot, copilot, attendants]
		chain_flight_info=",".join(documented_info)
		return chain_flight_info

	def WriteFlight(self, new_flight):
		flight_file=open("data/flights.csv", "a+")
		flight_file.write(new_flight)
		flight_file.close()

	def new_flight(self,id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, arriving_gate, landing_track, pilot, copilot, attendants):
		nFlight={}
		n_flight= Flights(id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, arriving_gate, landing_track, pilot, copilot, attendants)
		nFlight[id+plate]=n_flight
		return nFlight
	#traveller tools
	def document_traveller(self,passport, forename, surname, date_of_birth, country, gender, marital_status):
		documented_info=[passport, forename, surname, date_of_birth, country, gender, marital_status]
		chain_traveller_info=",".join(documented_info)
		return chain_traveller_info

	def WriteTraveller(self, new_traveller):
		traveller_file=open("data/travellers.csv", "a+")
		traveller_file.write(new_traveller)
		traveller_file.close()

	def new_traveller(self,passport, forename, surname, date_of_birth, country, gender, marital_status):
		nTraveller={}
		n_traveller=Travellers(passport, forename, surname, date_of_birth, country, gender, marital_status)
		nTraveller[passport]=n_traveller
		return nTraveller
	#Passenger tools
	def document_passenger(self,flight, passport, flight_class, seat, location):
		documented_info=[flight, passport, flight_class, seat, location]
		chain_passenger_info=",".join(documented_info)
		return chain_passenger_info

	def WritePassenger(self,new_passenger):
		passenger_file=open("data/passengers.csv", "a+")
		passenger_file.write(new_passenger)
		passenger_file.close()

	def new_passenger(self,flight, passport, flight_class, seat, location):
		nPassenger={}
		n_passenger=Passengers(flight, passport, flight_class, seat, location)
		nPassenger[flight+passport]=n_passenger
		#pos=AirportAD().read_passengers_file().values()
		#for flightPass in pos:
			#if flight==pos[flightPass]:
				#if pos[3]==seat:
					#print("...seat is not available...")
				#else:
					#return nPassenger
		return nPassenger


class Add_data:
	def __init__(self):
		self.existent=AirportAD()
		self.new=Catch_data()
	
	def add_passenger(self,flight, passport, flight_class, seat, location):
		global all_passengers
		existent=self.existent.read_passengers_file()
		new=self.new.new_passenger(flight, passport, flight_class, seat, location)
		all_passengers=ChainMap(existent, new)
		return all_passengers

	def add_traveller(self,passport, forename, surname, date_of_birth, country, gender, marital_status):
		global all_travellers
		existent=self.existent.read_travellers_file()
		new=self.new.new_traveller(passport, forename, surname, date_of_birth, country, gender, marital_status)
		all_travellers=ChainMap(existent, new)
		return all_travellers

	def add_flight(self,id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, arriving_gate, landing_track, pilot, copilot, attendants):
		global all_flights
		existent=self.existent.read_flights_file()
		new=self.new.new_flight(id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, arriving_gate, landing_track, pilot, copilot, attendants)
		all_flights=ChainMap(existent, new)
		return all_flights

class Date_options:
	def dateInfo(self):
		print("ingrese fecha para generar reporte (YYMMDD): ")
		yymmdDate = int(input())
		return yymmdDate

	def timeInfo(self):
		print("Ingrese hora para generar reporte (HHMM): ")
		hhmmTime = int(input())
		return hhmmTime

class Csv:
	def csv_writer(self):
		global yymmdDate
		global hhmmTime
		yymmdDate = Date_options().dateInfo()####### Meter esto como parametros 
		hhmmTime =  Date_options().timeInfo()########
		file = open("statistics.csv", "w+")
		file.write("date, time, # empty tracks, # busy tracks, # passengers in check-in, # passengers in security, # passengers boarded, # flights landed, # flights departured, available gates, occupied gates")
		file.write("\n")
		file.write("," * 11)
		file.close()

		file = open("statistics.csv", "r")
		lst = list(csv.reader(file))
		file.close()

		file = open("statistics.csv", "w")
		lst[1][0] = yymmdDate#
		lst[1][1] = hhmmTime#
		lst[1][2] = tracks_checkMode().nEmpty_tracks(yymmdDate, hhmmTime)#
		lst[1][3] =	tracks_checkMode().nBusy_tracks(count)#
		flight_finder = Checkpoint_check().flight_finder()#
		lst[1][4] = Checkpoint_check().checkIn_counter()#
		lst[1][5] = Checkpoint_check().security_counter()#
		lst[1][6] = Checkpoint_check().boarded_counter()#
		lst[1][7] = Flights_actual().flights_off()#
		lst[1][8] = Flights_actual().flights_taken()#
		lst[1][9] = Gates_check().cAvailable_list()#
		lst[1][10] = Gates_check().cBusy_list()#

		print(lst)
		csv.writer(file).writerows(lst)#
		file.close()#

class AirportAD:
	def read_pilots_file(self):
		pilots_file = open("data/pilots.csv", "r")
		lines = pilots_file.readlines()
		lines.pop(0)

		pilots = {}

		for line in lines:
			fields = line.split(",")
			passport = fields[0]
			forename = fields[1]
			surname = fields[2]
			date_of_birth = fields[3]
			country = fields[4]
			gender = fields[5]
			marital_status = fields[6]

			pilot = Pilot(passport, forename, surname, date_of_birth, country, gender, marital_status)
			pilots[passport] = pilot
		return pilots

	def read_travellers_file(self):
		travellers_file = open("data/travellers.csv", "r")
		lines = travellers_file.readlines()
		lines.pop(0)

		travellers = {}

		for line in lines:
			fields = line.split(",")
			passport = fields[0]
			forename = fields[1]
			surname = fields[2]
			date_of_birth = fields[3]
			country = fields[4]
			gender = fields[5]
			marital_status = fields[6]

			traveller = Travellers(passport, forename, surname, date_of_birth, country, gender, marital_status)
			travellers[passport] = traveller
		return travellers

	def read_passengers_file(self):
		passengers_file = open("data/passengers.csv", "r")
		lines = passengers_file.readlines()
		lines.pop(0)

		passengers = {}

		for line in lines:
			fields = line.split(",")
			flight = fields[0]
			passport = fields[1]
			flight_class = fields[2]
			seat = fields[3]
			location = fields[4]

			passenger = Passengers(flight, passport, flight_class, seat, location)
			passengers[flight + passport] = passenger
		return passengers

	def read_flights_file(self):
		flights_file = open("data/flights.csv", "r")
		lines = flights_file.readlines()
		lines.pop(0)

		flights = {}

		for line in lines:
			fields = line.split(",")
			id = fields[0]
			plate = fields[1]
			origin = fields[2]
			destiny = fields[3]
			departure = fields[4]
			arriving = fields[5]
			status = fields[6]
			departure_gate = fields[7]
			take_off_track = fields[8]
			arriving_gate = fields[9]
			landing_track = fields[10]
			pilot = fields[11]
			copilot = fields[12]
			attendants = fields[13]

			flight = Flights(id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, arriving_gate, landing_track, pilot, copilot, attendants)
			flights[id + plate] = flight
		return flights

	def read_attendants_file(self):
		attendants_file = open("data/attendants.csv", "r")
		lines = attendants_file.readlines()
		lines.pop(0)

		attendants = {}

		for line in lines:
			fields = line.split(",")
			passport = fields[0]
			forename = fields[1]
			surname = fields[2]
			date_of_birth = fields[3]
			country = fields[4]
			gender = fields[5]
			marital_status = fields[6]

			attendant = Attendants(passport, forename, surname, date_of_birth, country, marital_status,gender)
			attendants[passport] = attendant
		return attendants

	def read_planes_file(self):
		planes_file = open("data/planes.csv", "r")
		lines = planes_file.readlines()
		lines.pop(0)

		planes = {}
		for line in lines:
			fields = line.split(",")
			plate = fields[0]
			manufacturer = fields[1]
			model = fields[2]
			passengers_capacity = fields[3]
			luggage_capacity = fields[4]
			max_speed = fields[5]

			plane = Planes(plate, manufacturer, model, passengers_capacity, luggage_capacity, max_speed)
			planes[plate] = plane
		return planes

class Checkpoint_check:
	def security_counter(self):
		security = 0

		for data_passenger in AirportAD().read_passengers_file().values():
			flight = data_passenger.flight
			location = data_passenger.location
			for plate in cut:
				if flight == plate[0:5] and str(location) == "seguridad\n":
						security += 1

		return security
	
	def boarded_counter(self):
		boarded = 0

		for data_passenger in AirportAD().read_passengers_file().values():
			flight = data_passenger.flight
			location = data_passenger.location
			for plate in cut:
				if flight == plate[0:5] and str(location) == "abordado\n":
						boarded += 1

		return boarded

	def checkIn_counter(self):
		check_in = 0

		for data_passenger in AirportAD().read_passengers_file().values():
			flight = data_passenger.flight
			location = data_passenger.location
			for plate in cut:
				if flight == plate[0:5] and str(location) == "check-in\n":
						check_in += 1

		return check_in
	
	def flight_finder(self):#
		global cut
		cut = []
		for flight in plate_flights.values():
			if int(flight[0]) == yymmdDate:
				if int(flight[1]) <= hhmmTime:
					cut.append(list(plate_flights.keys())[list(plate_flights.values()).index(flight)])

			elif flight[2] == yymmdDate:
				if int(flight[3]) <= hhmmTime:
					cut.append(list(plate_flights.keys())[list(plate_flights.values()).index(flight)])

		return cut

class Flights_actual:
	def flights_off(self):
		flights_off = 0

		for flight_data in AirportAD().read_flights_file().values():
			destiny = flight_data.destiny
			id = flight_data.id
			for plates in cut:
				if destiny == "Ciudad de Mexico - MEXICO" and plates[0:5] == id:
					flights_off += 1

		return flights_off
	
	def flights_taken(self):
		taken_flights = 0

		for flight_data in AirportAD().read_flights_file().values():
			origin = flight_data.origin
			id = flight_data.id
			for plates in cut:
				if origin == "Ciudad de Mexico - MEXICO" and plates[0:5] == id:
					taken_flights += 1

		return taken_flights

class tracks_checkMode:
	def nEmpty_tracks(self, _YYMMDD, _HHMM):
		#en las siguientes partes del programma, se usa global, lo cual nos permite acceder a la variable, en este caso, desde otras funciones
		global count
		global plate_flights
		plate_flights = {}
		count = 3
		#El conteo de vuelos se centra en "Ciudad de Mexico, Mexico" porque es de los datos de mayor repeticion, de esa forma es mas sencilo "subdividir" el documento
		for flight in AirportAD().read_flights_file().values():
			departure = flight.departure
			arrival = flight.arriving
			id = flight.id
			plate = flight.plate
			destiny = flight.destiny
			origin = flight.origin

			departure_time = departure.split("_")
			arrival_time = arrival.split("_")
			plate_flights[id + plate] = [departure_time[0], departure_time[1], arrival_time[0], arrival_time[1]]

		for flight in plate_flights.values():
			
			if origin == "Ciudad de Mexico - MEXICO":
				if int(flight[0]) == _YYMMDD and int(flight[1]) == _HHMM:
					count -= 1
			
			elif destiny == "Ciudad de Mexico - MEXICO":
				if int(flight[2]) == _YYMMDD and int(flight[3]) == _HHMM:
					count -= 1
			
		return count

	def nBusy_tracks(self, count):
		nBusy_tracks =  3 - count

		return nBusy_tracks

class Gates_check:
	def cAvailable_list(self):
		aGate_list = []
		global bGate_list
		bGate_list = []

		for flight_data in AirportAD().read_flights_file().values():
			arriving_gate = flight_data.arriving_gate
			departure_gate = flight_data.departure_gate
			destiny = flight_data.destiny
			origin = flight_data.origin
			departure = flight_data.departure
			arrival = flight_data.arriving

			departure_time = departure.split("_")
			arrival_time = arrival.split("_")

			if origin == "Ciudad de Mexico - MEXICO" and str(departure_gate) not in aGate_list:
					aGate_list.append(str(departure_gate))

					if str(departure_time[2]) == str(yymmdDate) and str(departure_time[3]) == str(hhmmTime):
						bGate_list.append(str(departure_gate))

			elif destiny == "Ciudad de Mexico - MEXICO" and str(arriving_gate) not in aGate_list:
					aGate_list.append(str(arriving_gate))

					if str(arrival_time[0]) == str(yymmdDate) and str(arrival_time[1]) == str(hhmmTime):
						bGate_list.append(str(arriving_gate))

		for gate in bGate_list:
			aGate_list.remove(gate)

		return aGate_list

	def cBusy_list(self):

		return bGate_list

class ModificarDatos :
	def modify_attendants(self,_passport_t,_marital_status):
		modification_for_attendants = AirportAD().read_attendants_file()
		modification_for_attendants[_passport_t].marital_status= _marital_status 
		return modification_for_attendants
    
	
	def modify_travellers(self,_passport_travellers,_civil_status,_gener,_birthdate,name,surname_):
		modification_for_travellers=AirportAD().read_travellers_file()
		modification_for_travellers[_passport_travellers].marital_status=_civil_status
		modification_for_travellers[_passport_travellers].gender=_gener
		modification_for_travellers[_passport_travellers].date_of_birth=_birthdate
		modification_for_travellers[_passport_travellers].forename=name
		modification_for_travellers[_passport_travellers].surname=surname_
		return modification_for_travellers
		
	def modify_passenger_data(self,_flight_passanger,_passport_passangert,_seat_,_flight_class_,_location_):
		modification_for_passenger=AirportAD().read_passengers_file()
		modification_for_passenger[_flight_passanger +_passport_passangert].seat=_seat_
		modification_for_passenger[_flight_passanger +_passport_passangert].flight_class=_flight_class_
		modification_for_passenger[_flight_passanger + _passport_passangert].location=_location_
		return modification_for_passenger
			
	def modify_pilot_data(self,_passport_pilots,_marital_status_p):
		modification_for_pilots=AirportAD().read_pilots_file()
		modification_for_pilots[_passport_pilots].marital_status=_marital_status_p
		return modification_for_pilots


	def modify_flight(self,id_op,__plate,_status,_door,_track,_attendants,_pilots_for_fligth,_copilot_):
		modidication_for_pilots=AirportAD().read_flights_file()
		modidication_for_pilots[id_op+__plate].pilot=_pilots_for_fligth
		modidication_for_pilots[id_op+__plate].attendants=_attendants
		modidication_for_pilots[id_op+__plate].copilot=_copilot_
		modidication_for_pilots[id_op+__plate].status =_status
		modidication_for_pilots[id_op+__plate].departure_gate=_door
		modidication_for_pilots[id_op+__plate].take_off_track=_track
		return modidication_for_pilots

class Options_to_modify:
	def modify_attendants_op(self):
		global dic_modificado
		passport_at=str(input("Enter the attendant's passport: "))
		new_marital=str (input("Enter the new marital status: "))
		correct_at= ModificarDatos()
		dic_modificado= correct_at.modify_attendants(passport_at,new_marital)
		return dic_modificado
	def modify_pilot_op(self):
		global pilot_dic
		passport=str(input("Enter the pilot's passport: "))
		marital_status=str(input("Enter the new marital status: "))
		correct= ModificarDatos ()
		pilot_dic=correct.modify_pilot_data(passport, marital_status) 
		return pilot_dic
    
	def modify_flight_op(self):
		global dic_flight__
		flight=str(input("Enter the passenger's flight: "))
		passport_pass=str(input("Enter the passport: "))
		seat=str(input("Enter the new seat"))
		flight_class=str(input("Enter the new flight class"))
		location=str(input("Enter the new location"))
		passenger=ModificarDatos()
		dic_flight__=passenger.modify_passenger_data(flight,passport_pass,seat,flight_class,location)
		return dic_flight__
	def modify_travellers_op(self):
		global dic_trave
		passport_tra=str(input("Enter the traveller's passport: "))
		civil_tra=str (input("Enter the new civil status: "))
		gender_tra=str (input("Enter the new gender: "))
		birthdate=str (input("Enter the new gender: "))
		forname=str(input("Enter the new forname: "))
		surname=str(input("Enter the new surname: "))
		traveller=ModificarDatos()
		dic_trave=traveller.modify_travellers(passport_tra,civil_tra,gender_tra,birthdate,forname,surname)
		return dic_trave

	def modify_passenger_op(self):
		global dic_passenger__
		flight=str(input("Enter the passenger's flight: "))
		passport_pass=str(input("Enter the passport: "))
		seat=str(input("Enter the new seat"))
		flight_class=str(input("Enter the new flight class"))
		location=str(input("Enter the new location"))
		passenger=ModificarDatos()
		dic_passenger__= passenger.modify_passenger_data(flight,passport_pass,seat,flight_class,location) 
		return dic_passenger__

class Write_correct: 
	def write_attendants(self):
		archivo=open("data/attendants.csv", "w+")
		archivo.write("passport,forename,surname,date of birth, country, gender, marital status\n")
		for m in dic_modificado.keys():
			archivo.write(dic_modificado[m].passport + "," )
			archivo.write(dic_modificado[m].forename + "," )
			archivo.write(dic_modificado[m].surname +",")
			archivo.write(dic_modificado[m].date_of_birth + ",")
			archivo.write(dic_modificado[m].country + ",")
			archivo.write(dic_modificado[m].gender + ",")
			archivo.write(dic_modificado[m].marital_status )

		archivo.close()
	def write_passen_co(self):
		archivo=open("data/passengers.csv", "w+")
		archivo.write("flight,passport,class,seat,location\n")
		for m in dic_passenger__.keys():
			archivo.write(dic_passenger__[m].flight + "," )
			archivo.write(dic_passenger__[m].passport + "," )
			archivo.write(dic_passenger__[m].flight_class +",")
			archivo.write(dic_passenger__[m].seat + ",")
			archivo.write(dic_passenger__[m].location + ",")
		archivo.close()
	def write_pilot_co(self):
		archivo=open("data/pilots.csv", "w+")
		archivo.write("passport,forename,surname,date of birth, country, gender, marital status\n")
		for m in pilot_dic.keys():
			archivo.write(pilot_dic[m].passport + "," )
			archivo.write(pilot_dic[m].forename + "," )
			archivo.write(pilot_dic[m].surname +",")
			archivo.write(pilot_dic[m].date_of_birth + ",")
			archivo.write(pilot_dic[m].country + ",")
			archivo.write(pilot_dic[m].gender + ",")
			archivo.write(pilot_dic[m].marital_status )

		archivo.close()
	def write_travellers_co(self):
		archivo=open("data/travellers.csv", "w+")
		archivo.write("passport,forename,surname,date of birth, country, gender, marital status\n")
		for m in dic_trave.keys():
			archivo.write(dic_trave[m].passport + "," )
			archivo.write(dic_trave[m].forename + "," )
			archivo.write(dic_trave[m].surname +",")
			archivo.write(dic_trave[m].date_of_birth + ",")
			archivo.write(dic_trave[m].country + ",")
			archivo.write(dic_trave[m].gender + ",")
			archivo.write(dic_trave[m].marital_status ) 

		archivo.close()
	def write_flight_co(self):
		archivo=open("data/flights.csv", "w+")
		archivo.write("passport,forename,surname,date of birth, country, gender, marital status\n")
		for m in dic_flight__.keys():
			archivo.write("\n"+dic_flight__[m].id+ "," )
			archivo.write(dic_flight__[m].plate + "," )
			archivo.write(dic_flight__[m].origin +",")
			archivo.write(dic_flight__[m].destiny + ",")
			archivo.write(dic_flight__[m].departure + ",")
			archivo.write(dic_flight__[m].arriving + ",")
			archivo.write(dic_flight__[m].status + ",")
			archivo.write(dic_flight__[m].departure_gate + ",")
			archivo.write(dic_flight__[m].take_off_track + ",")
			archivo.write(dic_flight__[m].arriving_gate + ",")
			archivo.write(dic_flight__[m].landing_track + ",")
			archivo.write(dic_flight__[m].pilot + ",")
			archivo.write(dic_flight__[m].copilot + ",")
			archivo.write(dic_flight__[m].attendants )
		archivo.close()

