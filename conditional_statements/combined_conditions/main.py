# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct=discounted or lowStock #a 'not' infront an 'or' statement becomes an 'and'
promotion=not(movingProduct) 
print("Is the item eligible for promotion?",promotion)