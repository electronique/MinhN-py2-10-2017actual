# Demo

daniel = {
	"first_name":"Daniel",
	"last_name": "Morgan",
	"age": 35,
	"location":"Washington DC"
}
carlos = {
	"first_name":"Carlos",
	"last_name": "Arosemena",
	"age": 35,
	"location":"Toronto"
}
collin = {
	"first_name":"Collin",
	"last_name": "Prusse",
	"age": 28,
	"location":"Denver"
}
alicia = {
	"first_name":"Alicia",
	"last_name": "Alexander",
	"age": 31,
	"location":"Baltimore"
}
# print dir(alicia)
# print dir(object)
# instances
class Mammal(object):
	def __init__(self, year_of_birth):
		self.year_of_birth = year_of_birth
	def death(self):
		self.age = None

class Person(Mammal):
	def __init__(self, year_of_birth, first_name, last_name, age, location):
		super(Person,self).__init__(year_of_birth)
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
	def dieing(self):
		super(Person, self).death()
		print "hello my name is " + self.first_name + " " + self.last_name + " and i am dead"
	def running(self):
		print "running"
		return self
		# return None
	def walk(self):
		print "walking"
# daniel = Person("Daniel", "Morgan", 35, "Washington DC")
# carlos = Person("Carlos", "Arosemena", 35, "Toronto")
# collin = Person("Collin", "Prusse", 28, "Denver")
# alicia = Person("Alicia", "Alexander", 31, "Baltimore")
# daniel.greet()
# carlos.greet()
# collin.greet()
# alicia.greet()
daniel = Person(1982,"Daniel", "Morgan", 35, "Washington DC")
# daniel.running()
# daniel.running()
# daniel.running()
# daniel.running()


