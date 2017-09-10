class Bicycle(object):
	"""docstring for Bicycle"""
	def __init__(self, modelname, weight, prodcost):
		super(Bicycle, self).__init__()
		self.modelname = modelname
		self.weight = weight
		self.prodcost = prodcost

	def __repr__(self):
		return self.modelname


class Bike_Shop(object):
	"""docstring for Bike_Shop"""
	def __init__(self, shopname, inventory = None, bike_prices = None, bikes_sold = None,
				 price_margin = 1.2, profits = None):
		super(Bike_Shop, self).__init__()
		self.shopname = shopname
		self.inventory = {}
		self.bike_prices = {}
		self.bikes_sold = {}
		self.price_margin = price_margin
		self.profits = profits

	def add_inventory(self):

		for model in modelslist:
			self.inventory[model] = input("How many {}s would you like to the {} stock? "
										   .format (model.modelname, self.shopname))

		return self.inventory

	def price_list(self):

		for bike_model in self.inventory:
			self.bike_prices[bike_model.modelname] = bike_model.prodcost * self.price_margin

		return self.bike_prices

	def sales_profits(self):
		


		pass


class Customers(object):
	"""docstring for Customers"""
	def __init__(self, custname, custacct, affordable_bikes = None):
		super(Customers, self).__init__()
		self.custname = custname
		self.custacct = custacct
		self.affordable_bikes = []

	def affordable(self):
		for shop in shopslist:
			for bike in shop.bike_prices:
				if self.custacct >= shop.bike_prices[bike]:
					self.affordable_bikes.append(bike)

		return self.affordable_bikes
		

# Add new bicycle models
modelslist = [Bicycle('mountain_bike', 20, 400), 
			  Bicycle('electric_bike', 25, 500),
			  Bicycle('tricycle_bike', 30, 300),
			  Bicycle('sporting_bike', 15, 600),
			  Bicycle('foldable_bike', 10, 150),
			  Bicycle('quadgear_bike', 40, 700),
			  Bicycle('jungle_bike', 15, 100)
			  ]

# Create a bicycle shop
shopslist = [Bike_Shop('forest_shop'),
			 Bike_Shop('walmart')
			]

# Create customers
customerlist = [Customers('Tommy', 200),
				Customers('Kelly', 500),
				Customers('Drum', 1000)
				]

# Add stock to the shops
for shop in shopslist:
	print('Available stock at {}, {}'.format(shop.shopname, shop.add_inventory()))
# print('Available stock at {}, {}'.format(shopslist[1].shopname, shopslist[1].add_inventory()))

# Print store price lists
for shop in shopslist:
	print('Price list for {}: {}'.format(shop.shopname, shop.price_list()))
# print('Price list for {}: {}'.format(shopslist[1].shopname, shopslist[1].price_list()))

#print list of bikes each customer can afford
for customer in customerlist:
	print('{} can afford the following bikes: {}'.format(customer.custname, list(set(customer.affordable()))))