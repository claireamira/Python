class User:
    def __init__(self, username, fname, lname):
        self.username = username
        self.fname = fname
        self.lname = lname
        self.cart = ShoppingCart(self)  
        self.orders = []  

    def __str__(self):
        return f"User: {self.username}, Name: {self.fname} {self.lname}"

    def addToCart(self, product):
        self.cart.addProduct(product)

    def order(self, location):
        new_order = Order(self, self.cart.products, location)
        self.orders.append(new_order)
        self.cart.clear()  

    def removeProduct(self, product):
        self.cart.removeProduct(product)

    def cancelOrder(self, order):
        if order in self.orders:
            self.orders.remove(order)

    def completeOrder(self, order):
        if order in self.orders:
            order.paymentStatus = 'Completed'

    def viewOrders(self):
        for order in self.orders:
            print(order)

#
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def changeName(self, new_name):
        self.name = new_name

    def changePrice(self, new_price):
        self.price = new_price

    def changeCategory(self, new_category):
        self.category = new_category

    def __str__(self):
        return f"Product: {self.name}, Category: {self.category}, Price: ${self.price:.2f}"

#
class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.products = []

    def addProduct(self, product):
        self.products.append(product)

    def removeProduct(self, product):
        if product in self.products:
            self.products.remove(product)

    def viewCart(self):
        if not self.products:
            print("Your cart is empty.")
        else:
            print(f"{self.user.fname}'s Shopping Cart:")
            total_price = 0
            for product in self.products:
                print(product)
                total_price += product.price
            print(f"Total Price: ${total_price:.2f}")

    def clear(self):
        self.products = []

#
class Order:
    def __init__(self, user, products, location):
        self.user = user
        self.products = products
        self.location = location
        self.paymentStatus = 'Pending'  

    def __str__(self):
        product_list = ', '.join([product.name for product in self.products])
        return (f"Order for {self.user.fname} {self.user.lname}:\n"
                f"Products: {product_list}\n"
                f"Delivery Location: {self.location}\n"
                f"Payment Status: {self.paymentStatus}")




handbag = Product(name="Handbag", price=50.0, category="Accessories")
stationery = Product(name="Stationery", price=15.0, category="Office Supplies")
mugs = Product(name="Mugs", price=12.0, category="Kitchenware")

hanifa = User(username="hanifa123", fname="Hanifa", lname="Ahmed")

hanifa.addToCart(handbag)
hanifa.addToCart(stationery)
hanifa.addToCart(mugs)

hanifa.cart.viewCart()

hanifa.order(location="123 Main St, Cityville")

hanifa.viewOrders()

order_to_complete = hanifa.orders[0]
hanifa.completeOrder(order_to_complete)

hanifa.viewOrders()
