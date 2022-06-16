class ShoppingCart:
   
    def __init__(self):
        self.shopping_cart=[]
    
    def add(self):
        item = input("What item would you like to add to your shopping cart?")
        self.shopping_cart.append(item)

    def delete(self):
         item = input("What item would you like to delete from your shopping cart?")
         self.shopping_cart.remove(item)

    def view(self):
        print("This is your current shopping list.")
        print(self.shopping_cart)

    def quit(self):
        print("Thank you for shopping today! Your final shopping list is below. You will now exit the program.")
        print(self.shopping_cart)

    def choice(self):
        done=False
        while not done:
            decision = input("What would you like to do next? add, delete, view, quit ").lower()
            if decision == "add":
                self.add()
            elif decision == "delete":
                self.delete()
            elif decision == "view":
                self.view()
            elif decision == "quit":
                self.quit()
                done=True
            else:
                print("This isn't an option. Please try again!")



cart1=ShoppingCart()
cart1.choice()


            
             