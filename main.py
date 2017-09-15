import random

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
	def __init__(self, shopname, shopacct = 0, inventory = None, bike_prices = None, bikes_sold = None,
				 price_margin = 1.2, profits = 0, orderrequests = None):
		super(Bike_Shop, self).__init__()
		self.shopname = shopname
		self.shopacct = shopacct
		self.inventory = {}
		self.bike_prices = {}
		self.bikes_sold = {}
		self.price_margin = price_margin
		self.profits = profits
		self.orderrequests = {}

	def __repr__(self):
		return self.shopname

	def add_inventory(self):

		for model in modelslist:
			self.inventory[model] = int(input("How many {}s would you like to the {} stock? "
										   .format (model.modelname, self.shopname)))

		return self.inventory

	def price_list(self):

		for bike_model in self.inventory:
			self.bike_prices[bike_model] = bike_model.prodcost * self.price_margin

		return self.bike_prices

	def sales_profits(self):
		#process customer orders
		for customer in self.orderrequests:
			customer.purchases.append(self.orderrequests[customer])

			#update sales list
			if self.orderrequests[customer] in self.bikes_sold:
				self.bikes_sold[self.orderrequests[customer]] += 1

			else:
				self.bikes_sold.update({self.orderrequests[customer] : 1})

			#update inventory list
			self.inventory[self.orderrequests[customer]] -= 1
			# self.inventory.update({self.orderrequests[customer] : -- 1})

		#calculate profits
		self.profits = self.shopacct - (self.shopacct / 1.2)

		return (self.bikes_sold, self.inventory, self.profits)


class Customers(object):
	"""docstring for Customers"""
	def __init__(self, custname, custacct, affordable_bikes = None, myorders = None, purchases = None,
				 totalspend = 0, shopchoice = None):
		super(Customers, self).__init__()
		self.custname = custname
		self.custacct = custacct
		self.affordable_bikes = []
		self.myorders = []
		self.purchases = []
		self.totalspend = totalspend
		self.shopchoice = random.choice(shopslist)

	def __repr__(self):
		return self.custname

	def affordable(self):
		"""select a bike within budget from available models"""
		for shop in shopslist:
			for bike in shop.bike_prices:
				if self.custacct >= shop.bike_prices[bike]:
					self.affordable_bikes.append(bike)

		return self.affordable_bikes

	def place_order(self):

		# Select a bike to buy and update personal order list
		if len(self.affordable_bikes) > 0:
			self.myorders.append(random.choice(self.affordable_bikes))

			#Send order to the shop / dealer
			self.shopchoice.orderrequests[self] = random.choice(self.myorders)

		else:
			print("{} can't afford any bike".format(self.custname))

		return self.myorders

	def order_payment(self):
		for bike in self.myorders:
			#credit shop account per purchase ordered
			self.shopchoice.shopacct += self.shopchoice.bike_prices[bike]

			#debt customer account per purchase ordered
			self.custacct -= self.shopchoice.bike_prices[bike]

			#update expenditure account
			self.totalspend += self.shopchoice.bike_prices[bike]

		return (self.totalspend, self.custacct)



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

#print cutsomer's orders
for customer in customerlist:
	print('{} has ordered for: {}'.format(customer.custname, list(set(customer.place_order()))))

#print order requests from customers
for shop in shopslist:
	print('{} has recieved the following requests: {}'.format(shop.shopname, shop.orderrequests))

#Track total spent and account balance
for customer in customerlist:
	customer.order_payment()
	print('{} has spent {} and his account balance is {}'
		  .format(customer.custname, customer.totalspend, customer.custacct))

#Print available inventory after sales and sales profit
for shop in shopslist:
	shop.sales_profits()
	print('{} has sold {} and made {} in profits, remaining inventory is: {}'
		  .format(shop.shopname, shop.shopacct, shop.profits, shop.inventory))