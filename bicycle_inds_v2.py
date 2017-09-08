class Bicycle(object):
	"""docstring for Bicycle"""
	modelslist = []
	def __init__(self, modelname, weight, prodcost):
		super(Bicycle, self).__init__()
		self.modelname = modelname
		self.weight = weight
		self.prodcost = prodcost

		self.modelslist.append(self)


class Bike_Shop(object):
	"""docstring for Bike_Shop"""
	inventory = {}
	def __init__(self, shopname):
		super(Bike_Shop, self).__init__()
		self.shopname = shopname

		self.inventory = {}

	def add_inventory(self):

		for model in Bicycle.modelslist:
			self.inventory[model] = input("How many {}s would you like to the {} stock? ".format (model.modelname, self.shopname))

	def price_list(self):
		stock_prices = {}
		sales_margin = 0.2

		for bike_model in self.inventory:
			stock_prices[bike_model.modelname] = bike_model.prodcost + (bike_model.prodcost * sales_margin)

		print(stock_prices)

	def sales_profits(self):
		sold_bikes = {}
		


		pass


class Customers(object):
	"""docstring for Customers"""
	def __init__(self, custname, custacct):
		super(Customers, self).__init__()
		self.custname = custname
		self.custacct = custacct
		

# Add new bicycle models		
model1 = Bicycle('mountain_bike', 20, 400)
model2 = Bicycle('electric_bike', 25, 500)

# Create a bicycle shop
shop1 = Bike_Shop('forest_shop')
shop2 = Bike_Shop('walmart')

# Add stock to shop 1
shop1.add_inventory()
print('Available stock at {}, {}'.format(shop1.shopname, shop1.inventory))

# Add stock to shop 2
shop2.add_inventory()
print('Available stock at {}, {}'.format(shop2.shopname, shop2.inventory))

# Print store price lists
shop1.price_list()
shop2.price_list()