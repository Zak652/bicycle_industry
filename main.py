# from bicycles import Bicycle, Bike_Shop, Customers
import bicycles


def main():

	# Add new bicycle models
	modelslist = [bicycles.Bicycle('mountain_bike', 20, 400), 
				  bicycles.Bicycle('electric_bike', 25, 500),
				  bicycles.Bicycle('tricycle_bike', 30, 300),
				  bicycles.Bicycle('sporting_bike', 15, 600),
				  bicycles.Bicycle('foldable_bike', 10, 150),
				  bicycles.Bicycle('quadgear_bike', 40, 700),
				  bicycles.Bicycle('jungle_bike', 15, 100)
				  ]

	# Create a bicycle shop
	shopslist = [bicycles.Bike_Shop('forest_shop'),
				 bicycles.Bike_Shop('walmart')
				]

	# Create customers
	customerlist = [bicycles.Customers('Tommy', 200),
					bicycles.Customers('Kelly', 500),
					bicycles.Customers('Drum', 1000)
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

if __name__=="__main__":
	main()