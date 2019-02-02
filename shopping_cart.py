from IPython.display import clear_output

class Cart():
    def __init__(self, cart=[]):
        self.cart = cart

    def addItem(self):
        clear_output()
        new_item = input('What would you like to add to your shopping cart? ')
        new_item = new_item.title()
        self.cart.append(new_item)

    def removeItem(self):
        clear_output()
        self.showCart()
        item_to_remove = input('What would you like to remove from your shopping cart? ')
        item_to_remove = item_to_remove.title()

        if item_to_remove not in self.cart:
            print('That item is not in your shopping cart.')
        else:
            self.cart.remove(item_to_remove)

    def showCart(self):
        clear_output()
        print('*** Shopping Cart *** \n_____________________\n\n' + '\n'.join(self.cart))


user_cart = Cart()

while True:

        request = input('To add to cart, type ADD. To remove from cart, type REMOVE. To see what is in your cart, type CART. To quit, type QUIT. ')
        if request.lower() == 'add':
            user_cart.addItem()
        elif request.lower() == 'remove':
            user_cart.removeItem()
        elif request.lower() == 'cart':
            user_cart.showCart()
        elif request.lower() == 'quit':
            user_cart.showCart()
            break
        else:
            request = input('Please enter a valid command. Press ENTER to return to main menu. ')
