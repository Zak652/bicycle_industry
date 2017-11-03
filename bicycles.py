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