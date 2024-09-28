def make_purchase(self, quantity):
        try:
            if quantity <= 0:
                raise ValueError("Quantity can't be less than 1.")
            if quantity > self.amount:
                raise ValueError(f"out of stock. Only {self.amount} items.")
            
            total_price = self.get_price(quantity)
            if total_price:
                self.amount -= quantity
                print(f"purchase successfull. Total price: {total_price}")
                print(f"Remaining stock: {self.amount} items")
        
        except ValueError as e:
            print("Purchase failed:", e)
        except Exception as e:
            print("error: " ,e)