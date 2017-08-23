

class Bicycle(object):
	"""docstring for Bicycle"""
	model_costs = {}
	def __init__(self, model_name, weight, cost):
		self.model_name = model_name
		self.weight = weight
		self.cost = cost

		# self.model_costs = {}

		# Bicycle.model_list.append(self.model_name)
		self.model_costs[self.model_name] = self.cost


class Bike_Shop(object):
	"""docstring for Bike_Shop"""
	models_prices = {}
	# in_stock = {}
	price_topup = 1.2
	# amount_sold = 0
	# sales_profits = 0

	def __init__(self, name):
		self.name = name
		
		# self.models_prices = {}
		self.in_stock = {}
		self.amount_sold = 0
		self.sales_profits = 0

	def inventory(self, model, stock):

		self.models_prices[model.model_name] = model.cost * self.price_topup
		self.in_stock[model.model_name] = stock
		# print ([_model.model_name for _model in self.models])

	def bike_sale(self):
		bikes_sold = {}
		pass


class Customers(object):
	"""docstring for Customers"""
	customer_list = {}
	# afforded_list = []
	def __init__(self, name, budget):
		self.name = name
		self.budget = budget

		self.customer_list[self.name] = self.budget

	def shopping_list(self):
		
		afforded_list = []

		for bike in Bike_Shop.models_prices:
			if Bike_Shop.models_prices[bike] <= self.budget:
				afforded_list.append(bike)
			
		print("{}'s shopping list is: {}".format (self.name, afforded_list))


	def purchase(self):
		bikes_owned = []
		pass


#Creat bycicle models
electric = Bicycle('electric_bike', 20, 500)
mountain = Bicycle('mountain_bike', 15, 700)
tricycle = Bicycle('tricycle_bike', 25, 100)
foldable = Bicycle('foldable_bike', 10, 300)
bigwheel = Bicycle('bigwheel_bike', 30, 200)
sporting = Bicycle('sporting_bike', 10, 800)
quadcycle = Bicycle('quadcycle_bike', 40, 1000)

#Create a bicycle shop that has 6 different bicycle models in stock
shop_1 = Bike_Shop('victoria_bikes')

#Add the available bicycle model lists to the shop's inventory
shop_1.inventory(electric, 50)
shop_1.inventory(mountain, 10)
shop_1.inventory(tricycle, 30)
shop_1.inventory(foldable, 15)
shop_1.inventory(bigwheel, 20)
shop_1.inventory(sporting, 40)

# Print the initial inventory of the bike shop for each bike it carries
print("Dealer's stock:{}".format (shop_1.in_stock))

#Create customers
customer_1 = Customers('Ben', 200)
customer_2 = Customers('Jack', 500)
customer_3 = Customers('Chris', 1000)

# print([_model.model_name for _model in shop_1.models])
print('Available factory models: {}'.format (Bicycle.model_costs))
print("Dealer's model list and Prices: {}".format (shop_1.models_prices))
print("Customer's bicycle budgets: {}".format (Customers.customer_list))

# Print the name of each customer and a list of the bikes they can afford
customer_1.shopping_list()
customer_2.shopping_list()
customer_3.shopping_list()