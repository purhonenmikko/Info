class Person:

	def __init__(self, first, last, adress, gender, hetu, bd):
		self.__first_name = first
		self.__last_name = last
		self.__adress = adress
		self.__gender = gender
		self.__hetu = hetu
		self.__bd = bd

	def ret_fullname(self):
		return self.__first_name + " " + self.__last_name

	def ret_adress(self):
	   	return self.__adress

	def ret_gender(self):
	   	return self.__gender

	def ret_hetu(self):	
	   	return self.__hetu
	   	
	def ret_bd(self):
	   	return self.__bd

#-----------------------------------------

def read_name():
	name = input("Name (firstname lastname): ")
	name = name.split(" ")
	first = name[0]
	last = name[1]

	return first, last

def read_adress():
	adress = input("Adress: ")
	return adress

def read_gender():
	gender = input("Gender: ")
	return gender

def read_hetu():
	hetu = input("Hetu: ")
	total = hetu.split("-")
	BD = total[0]
	ID = hetu[1]
	bd = BD[0]+BD[1] + "." + BD[2]+BD[3] + "." + BD[4]+BD[5]
	return bd, hetu

def read_person():
	first, last = read_name()
	adress = read_adress()
	gender = read_gender()
	bday, hetu = read_hetu()

	person = Person(first, last, adress, gender, hetu, bday)
	return person 

def main():

	person1 = read_person()
	print(person1)
	print("\n")
	print(person1.ret_fullname())
	print(person1.ret_adress())
	print(person1.ret_gender())
	print(person1.ret_hetu())
	print(person1.ret_bd())

main()











