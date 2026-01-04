# Hotel Menu Billing System with GST Calculation
class HotelMenu:
    def __init__(self):
        # Menu items with prices more can be added
        self.menu = {
            1: ("Paneer Butter Masala", 250),
            2: ("Veg Fried Rice", 180),
            3: ("Chicken Biryani", 300),
            4: ("Tandoori Roti", 25),
            5: ("Cold Drink", 40),
            6: ("Gulab Jamun", 80),
            7: ("Masala Tea", 20),
            8: ("Chicken Curry", 150),
            9: ("Dal Makhani", 200),
            10: ("Naan", 30),
            11: ("Salad", 50),
            12: ("Ice Cream", 90),
            13: ("Mix Veg Curry", 220),
            14: ("Pasta", 270),
            15: ("Noddles", 160),
            16: ("Manchurian",120),
            17: ("Spring Rolls", 110),
            18: ("Plain Rice", 100)
        }
        self.order = []
# This function displays the hotel menu
    def display_menu(self):
        print("\n--- Hotel Menu ---")
        for item_no, (item_name, price) in self.menu.items():
            print(f"{item_no}. {item_name} - ₹{price}")
        print("------------------\n")
# This function takes the customer's order
    def take_order(self):
        while True:
            try:
                choice = int(input("Enter item number to order (0 to finish): "))
                if choice == 0:
                    break
                if choice in self.menu:
                    qty = int(input(f"Enter quantity for {self.menu[choice][0]}: "))
                    self.order.append((self.menu[choice][0], self.menu[choice][1], qty))
                    print(f"✅ Added {qty} x {self.menu[choice][0]} to order")
                else:
                    print("❌ Invalid choice, try again.")
            except ValueError:
                print("❌ Please enter a valid number.")
# This function generates the bill
    def generate_bill(self):
        print("\n--- Bill Receipt ---")
        subtotal = 0
        for item_name, price, qty in self.order:
            total_item_price = price * qty
            subtotal += total_item_price
            print(f"{item_name} x {qty} = ₹{total_item_price}")

        # GST Calculation
        sgst = subtotal * 0.09
        cgst = subtotal * 0.09
        grand_total = subtotal + sgst + cgst

        print("---------------------")
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"SGST (9%): ₹{sgst:.2f}")
        print(f"CGST (9%): ₹{cgst:.2f}")
        print(f"Grand Total: ₹{grand_total:.2f}")
        print("---------------------")
        print("🙏 Thank you for dining with us!\n")


# Example usage
if __name__ == "__main__":
    hotel = HotelMenu()
    hotel.display_menu()
    hotel.take_order()
    hotel.generate_bill()