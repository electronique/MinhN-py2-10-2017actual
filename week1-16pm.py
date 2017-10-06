
# OOP - Object oriented programming
	# def __init__(self, color, legs, material)
	# 	self.color = color
	# 	self.legs = legs
	# 	# self.material = material
chair1 = {
	"color":"blue", 
	"legs":3, 
	"material":"plastic"
}
chair2 = {
	"color":"blue", 
	"legs":3, 
	"material":"plastic"
}
chair3 = {
	"color":"blue", 
	"legs":3, 
	"material":"plastic"
}
chair4 = {
	"color":"blue", 
	"legs":3, 
	"material":"plastic"
}
chair5 = {
	"color":"blue", 
	"legs":3, 
	"material":"plastic"
}
chair6 = {
	"color":"blue", 
	"legs":3, 
	"material":"plastic"
}
chair6 = {
	"color":"blue", 
	"legs":3, 
	"material":"plastic"
}
class Decoration(object):
	def __init__(self, typeOfDecor):
		self.type_of_decor = typeOfDecor

	def printMe(self):
		print "I am a " + self.type_of_decor

class Chair(Decoration):
	def __init__(self, typeOfDecor, color, legs, material):
		super(Chair, self).__init__(typeOfDecor)
		self.color = color
		self.legs = legs
		self.material = material

	def printMe(self):
		super(Chair, self).printMe()
		print self.color
		print self.legs
		print self.material

	def addingLegs(self):
		print "adding legs"
		return self
	def breakingLegs(self):
		print "breaking a leg"

c1 = Chair("chair","blue", 3, "plastic")
# print c1.addingLegs().addingLegs().addingLegs().addingLegs().breakingLegs().addingLegs()
# c2 = Chair("chair", "green", 6, "wood")
# c2.printMe()
# c1 = Chair("blue", 3, "plastic")
# c2 = Chair("green", 4, "wood")
# c3 = Chair("yellow", 3, "plastic")
# c4 = Chair("blue", 3, "plastic")
# c5 = Chair("blue", 3, "plastic")
# c6 = Chair("blue", 3, "plastic")

# print c1
# print c2