from pizzapi import *

customer = Customer("FirstName", "LastName", "Email", "Phone")
address = Address("AddressName", "City", "Province", "PostalCode")
card = PaymentObject('4100123422343234', '0115', '777', '90210') # not a real card

store = address.closest_store() # set closes dominos store

menu = store.get_menu() # see entire menu, [itemcode, item description]

order = Order(store, customer, address)
order.add_item('P12IPAZA') # add a 12-inch pan pizza
order.add_item('MARINARA') # with an extra marinara cup

order.pay_with(card) # test paying