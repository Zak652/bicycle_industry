

class Bicycle(object):
	"""docstring for Bicycle"""
	model_list = []
	def __init__(self, model_name, weight, cost):
		self.model_name = model_name
		self.weight = weight
		self.cost = cost

		Bicycle.model_list.append(self)


class Bike_Shop(object):
	"""docstring for Bike_Shop"""
	models = {}
	stock = {}
	model_price = 1.2
	def __init__(self, name):
		self.name = name

	def inventory(self, model):

		self.models[model.model_name] = model.cost * self.model_price
		# print ([_model.model_name for _model in self.models])


	def bike_sale(self):
		bikes_sold = {}
		pass


	def profits(self):
		prof_margin = 1.2
		pass


class Customers(object):
	"""docstring for Customers"""
	def __init__(self, name, budget):
		self.name = name


	def account(self):
		acc_balance = 0
		pass


	def purchases(self):
		bikes_owned = {}
		pass


#Create bicycle shop
shop_1 = Bike_Shop('victoria_bikes')

#Creat bycicle models
electric = Bicycle('electric_bike', 20, 500)
mountain = Bicycle('mountain_bike', 15, 700)
tricycle = Bicycle('tricycle_bike', 25, 600)
foldable = Bicycle('foldable_bike', 10, 300)
bigwheel = Bicycle('bigwheel_bike', 30, 200)
sporting = Bicycle('sporting_bike', 10, 800)

#create available bicycle model lists
shop_1.inventory(electric)
shop_1.inventory(mountain)
shop_1.inventory(tricycle)
shop_1.inventory(foldable)
shop_1.inventory(bigwheel)
shop_1.inventory(sporting)

#Create customers
customer_1 = Customers('Ben', 200)
customer_2 = Customers('Jack', 500)
customer_3 = Customers('Chris', 1000)

# print([_model.model_name for _model in shop_1.models])
print(shop_1.models)
print(Bicycle.model_list)