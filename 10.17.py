#Iris Vance
#1270481

class ItemsToPurchase:
    def __init__(self, item_name = 'None', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        item_cost = self.item_price + self.item_quantity;
        return item_cost

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


if __name__ == "__main__":
    buy = ItemsToPurchase()
    item_name = input()
    item_price = int(input())
    item_quantity = int(input())

    buy.item_name = item_name
    buy.item_price = item_price
    buy.item_quantity = item_quantity

    buy2 = ItemsToPurchase()

    item_name = input()
    item_price = int(input())
    item_quantity = int(input())

    buy2.item_name = item_name
    buy2.item_price = item_price
    buy2.item_quantity = item_quantity

    print(buy.item_info())

    print('TOTAL COST')
    print(buy.item_name,' ', buy.item_quantity, ' @ ', '$', buy.item_price, ' = $', buy.print_item_cost(), sep='' )
    print(buy2.item_name,' ', buy2.item_quantity, ' @ ', '$', buy2.item_price, ' = $', buy2.print_item_cost(), sep='')
    print()
    print('Total: $', buy.print_item_cost() + buy2.print_item_cost(), sep='')









