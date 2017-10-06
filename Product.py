class Product(object): 
	def __init__(self, price, item_name, weight, brand, cost, status="for_sale"):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = status

	def sell(self):
		self.status = "sold"
		return self

	def tax(self, tax_amount):
		return self.price + self.tax_amount * self.price
		return self


	def returned(self, reason):
		if reason == "defective":
			self.status = "defective"
			self.price = 0
		elif reason == "in box":
			self.status = "for sale"
		elif reason == "open box":
			self.status = "used"
			self.price = self.price * .8
		return self

	def display_info(self):
		print self.price 
		print self.item_name
		print self.weight 
		print self.brand 
		print self.cost 
		print self.status 
		return self

product1 = Product(10.99, "Bag of Candy", 2, "Hershey", 5.99)
print product1.display_info().returned("defective").display_info()