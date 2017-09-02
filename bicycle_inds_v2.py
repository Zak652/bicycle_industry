class Bicycle(object):
	"""docstring for Bicycle"""
	modelslist = []
	def __init__(self, modelname, weight, prodcost):
		super(Bicycle, self).__init__()
		self.modelname = modelname
		self.weight = weight
		self.prodcost = prodcost

		self.modelslist.append(self.modelname)


class Bike_Shop(object):
	"""docstring for Bike_Shop"""
	def __init__(self, shopname):
		super(Bike_Shop, self).__init__()
		self.shopname = shopname


class Customers(object):
	"""docstring for Customers"""
	def __init__(self, custname, custacct):
		super(Customers, self).__init__()
		self.custname = custname
		self.custacct = custacct
		
		
bike1 = Bicycle('model1', 20, 400)
bike2 = Bicycle('model2', 25, 500)

print(Bicycle.modelslist)
print(bike2.__dict__)