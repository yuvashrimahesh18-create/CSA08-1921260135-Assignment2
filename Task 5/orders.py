# Task 5: Mutable Default Argument Bug

# Buggy version
def add_item_buggy(item, order=[]):
    order.append(item)
    return order


print("Buggy version:")

customer1 = add_item_buggy("Tea")
customer2 = add_item_buggy("Vada")

print("Customer 1:", customer1)
print("Customer 2:", customer2)

print("Shared default list:", add_item_buggy.__defaults__)


# Corrected version
def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


print("\nCorrected version:")

customer1 = add_item("Tea")
customer2 = add_item("Vada")

print("Customer 1:", customer1)
print("Customer 2:", customer2)


# Testing three different customers
customer3 = add_item("Coffee")
customer4 = add_item("Dosa", [])
customer5 = add_item(item="Idli", order=[])

print("Customer 3:", customer3)
print("Customer 4:", customer4)
print("Customer 5:", customer5)
# Function returning a tuple (total amount, GST amount)

def calculate_bill(amount, gst_rate=5):
    gst = amount * gst_rate / 100
    total = amount + gst
    return total, gst


print("\nBill calculation:")

total, gst = calculate_bill(1000)

print("GST amount:", gst)
print("Total amount:", total)
# Variable scope examples

# Global variable
shop_name = "Ksheera Milk Shop"


def show_shop():
    # Local variable
    customer_name = "Mahesh"
    print("Shop name:", shop_name)
    print("Customer name:", customer_name)


show_shop()


# Modifying a global variable
order_count = 0


def add_order():
    global order_count
    order_count += 1


add_order()
add_order()

print("Total orders:", order_count)


# Nonlocal variable example
def customer_counter():
    count = 0

    def increase():
        nonlocal count
        count += 1

    increase()
    increase()

    print("Customer counter:", count)


customer_counter()