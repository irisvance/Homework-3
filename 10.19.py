#Iris Vance
#1270481

class ItemsToPurchase:
    def __init__(self, item_name='None', item_price=0, item_quantity=0, item_description='None'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        item_cost = self.item_price + self.item_quantity;
        return item_cost

    def print_item_description(self):
        print(self.item_description)

    def item_info(self):
        print('Item 1')
        print('Enter the item name:'.format(buy.item_name))
        print('Enter the item price:'.format(buy.item_price))
        print('Enter the item quantity:'.format(buy.item_quantity))
        print()

        print('Item 2')
        print('Enter the item name:'.format(buy2.item_name))
        print('Enter the item price:'.format(buy2.item_price))
        print('Enter the item quantity:'.format(buy2.item_quantity))


class ShoppingCart:
    def __init__(self, name='None', date="January 1, 2016"):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    def add_item(self, added_item):
        self.cart_items.append(added_item)

    def remove_item(self, deleted_item):
        count = 0
        item = self.cart_items[:]
        for x in range(len(item)):
            removeItem = item[x]
            if removeItem.name == item_name:
                del self.cart_items[x]
                count += 1

        if count == 0:
            print(" ")
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_quantity):
        self.item_quantity.append(modified_quantity)

    def get_num_items_in_cart(self):
        count = 0
        items_in_cart = self.cart_items[:]
        for i in range(len(items_in_cart)):
            total_items = items_in_cart[i]
            count += items_in_cart.item_quantity
        return total_items

    def get_cost_of_cart(self):
        cost = 0
        cart_cost = self.cart_items[:]
        for x in range(len(cart_cost)):
            total_cart_cost = cart_cost[x]
            cost += (total_cart_cost._quantity * total_cart_cost._price)
        return cost

    def print_total(self):
        print(self.customer_name, "'s Shopping Cart - ", self.current_date)
        count = len(self.cart_items)
        if count == 0:
            print('')
            print("SHOPPING CART IS EMPTY")
            return 0

    def print_descriptions(self):
        print(self.item_description)

    def print_menu(customer_cart):
        print("MENU\n")
        print("a - Add item to cart\n")
        print("r - Remove item from cart\n")
        print("c - Change item quantity\n")
        print("i - output items' descriptions\n")
        print("o - Output shopping cart\n")
        print("q - Quit\n")
        print("Choose an option: \n")

    def main():
        customerName = ""
        todaysDate = ""

        customerName = input("Enter customer's name: ")
        todaysDate = input("Enter today's date: ")

        customerCart = ShoppingCart(customer_name,current_date)

        menuOptions = ""
        
        while menuOptions != "q":
            print_menu(customerCart)
            menuOptions = input("Choose an option: ").lower()
            if option == "o":
                customerCart.print_descriptions()
            elif option == "a":
                print("ADD ITEM TO CART")
                item_name = input("Enter the item name")
                item_description = input("Enter the item description")
                item_
                


if __name__ == "__main__":
    buy = ItemsToPurchase()
    item_name = input()
    item_price = int(input())
    item_quantity = int(input())
    item_description = input()

    buy.item_name = item_name
    buy.item_price = item_price
    buy.item_quantity = item_quantity
    buy.item_description = item_description

    buy2 = ItemsToPurchase()

    item_name = input()
    item_price = int(input())
    item_quantity = int(input())
    item_description = input()

    buy2.item_name = item_name
    buy2.item_price = item_price
    buy2.item_quantity = item_quantity
    buy2.item_description = item_description

    print(buy.item_info())

    print('TOTAL COST')
    print(buy.item_name, ' ', buy.item_quantity, ' @ ', '$', buy.item_price, ' = $', buy.print_item_cost(), sep='')
    print(buy2.item_name, ' ', buy2.item_quantity, ' @ ', '$', buy2.item_price, ' = $', buy2.print_item_cost(), sep='')
    print()
    print('Total: $', buy.print_item_cost() + buy2.print_item_cost(), sep='')









