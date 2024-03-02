class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, new_price):
        self.price = new_price
        print(f"Price of {self.name} updated to {self.price}")

    def update_stock(self, stock_change):
        # Assuming stock management is handled elsewhere and this method is a placeholder
        print(f"Stock for {self.name} updated by {stock_change} units.")


class User:
    def __init__(self, user_id, name, email, address):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.address = address

    def update_address(self, new_address):
        self.address = new_address
        print(f"Address for {self.name} updated to {self.address}")


class Customer(User):
    def __init__(self, user_id, name, email, address):
        super().__init__(user_id, name, email, address)
        self.cart = []  # List of Product objects
        self.order_history = []  # List of Order objects

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product.name} added to {self.name}'s cart.")

    def place_order(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        # Placeholder for order placement logic
        print(f"Order placed for {len(self.cart)} items.")
        self.order_history.append(self.cart)
        self.cart = []


class Admin(User):
    def __init__(self, user_id, name, email, address):
        super().__init__(user_id, name, email, address)

    def add_product(self, product, product_list):
        product_list.append(product)
        print(f"{product.name} added to the catalog.")

    def remove_product(self, product_id, product_list):
        for i, product in enumerate(product_list):
            if product.product_id == product_id:
                removed_product = product_list.pop(i)
                print(f"{removed_product.name} removed from the catalog.")
                return
        print("Product not found.")


class Order:
    def __init__(self, order_id, customer, products=None, status='Pending'):
        self.order_id = order_id
        self.customer = customer
        self.products = products if products else []
        self.status = status

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [product for product in self.products if product.product_id != product_id]

    def update_status(self, new_status):
        self.status = new_status
        print(f"Order {self.order_id} status updated to {new_status}.")


class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to the cart.")

    def remove_item(self, product_id):
        self.items = [item for item in self.items if item.product_id != product_id]
        print(f"Removed product {product_id} from the cart.")

    def checkout(self):
        order = Order(order_id=str(uuid.uuid4()), customer=self.customer, products=self.items, status='Pending')
        self.items = []  # Empty the cart after checkout
        print(f"Checkout successful for order {order.order_id}.")
        return order


class Payment:
    def __init__(self, payment_id, order, amount, status='Pending'):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.status = status

    def process_payment(self):
        # Simulate payment processing
        self.status = 'Completed'
        self.order.update_status('Paid')
        print(f"Payment {self.payment_id} for order {self.order.order_id} completed.")


class ProductCategory:
    def __init__(self, category_id, name, description):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        product.category = self.name
        print(f"Added {product.name} to category {self.name}.")

    def remove_product(self, product_id):
        self.products = [product for product in self.products if product.product_id != product_id]
        print(f"Removed product {product_id} from category {self.name}.")


class Inventory:
    def __init__(self, product, stock=0):
        self.product = product
        self.stock = stock

    def update_stock(self, change_in_stock):
        self.stock += change_in_stock
        print(f"Stock for {self.product.name} updated to {self.stock}.")

    def check_availability(self):
        return self.stock > 0


class Review:
    def __init__(self, review_id, product, customer, rating, comment):
        self.review_id = review_id
        self.product = product
        self.customer = customer
        self.rating = rating
        self.comment = comment

    def post_review(self):
        # Assuming a mechanism to add this review to the product's review list
        print(f"Review posted for {self.product.name} by {self.customer.name}: {self.comment}")


class Shipping:
    def __init__(self, order, address, status='Pending'):
        self.order = order
        self.address = address
        self.status = status

    def update_status(self, new_status):
        self.status = new_status
        print(f"Shipping status for order {self.order.order_id} updated to {self.status}.")


class Notification:
    def __init__(self, notification_id, user, message):
        self.notification_id = notification_id
        self.user = user
        self.message = message

    def send_notification(self):
        # Simulating sending a notification to the user
        print(f"Notification sent to {self.user.name}: {self.message}")


class Wishlist:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to {self.customer.name}'s wishlist.")

    def remove_item(self, product_id):
        self.items = [item for item in self.items if item.product_id != product_id]
        print(f"Removed product {product_id} from {self.customer.name}'s wishlist.")



class Analytics:
    @staticmethod
    def generate_sales_report(orders):
        total_sales = sum(order.products[0].price for order in orders if order.status == 'Paid')  # Simplified
        print(f"Total sales: ${total_sales}")
        return total_sales

    @staticmethod
    def generate_user_activity_report(users):
        active_users = [user for user in users if user.order_history]
        print(f"Total active users: {len(active_users)}")
        return active_users


class Search:
    @staticmethod
    def search_products(products, query):
        matching_products = [product for product in products if query.lower() in product.name.lower()]
        print(f"Found {len(matching_products)} products matching '{query}'.")
        return matching_products

    @staticmethod
    def filter_by_category(products, category_name):
        filtered_products = [product for product in products if product.category == category_name]
        print(f"Found {len(filtered_products)} products in category '{category_name}'.")
        return filtered_products
