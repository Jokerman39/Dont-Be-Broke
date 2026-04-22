"""
Program Name: Inflation Erode Calculator
Course: ITM320
Use Case: Inflation Loss Calculator
Author: Mark Palsulich
Description: Calculates the loss in principal due to inflation over a set time frame.
"""
# Name: Mark
# Name of Function: Display Main Menu
# Name of Use Case: Display Main Menu

class WealthData:
    def __init__(self, initial_amount, inflation_rate, years):
        self.initial_amount = float(initial_amount)
        self.inflation_rate = float(inflation_rate)
        self.years = int(years)


class InflationErosionCalculator:
    def __init__(self, data_object):
        self.data = data_object 

    def calculate_purchasing_power(self):
        rate_decimal = self.data.inflation_rate / 100
        
        try:
            # If the calculation gets too massive, it will trigger an OverflowError
            future_power = self.data.initial_amount / ((1 + rate_decimal) ** self.data.years)
            return future_power
        except OverflowError:
            # If the denominator is astronomically large, purchasing power is effectively zero.
            return 0.0

    def display_report(self):
        eroded_value = self.calculate_purchasing_power()
        total_loss = self.data.initial_amount - eroded_value

        print("\n--- Inflation Erosion Results ---")
        print(f"Starting Wealth: ${self.data.initial_amount:,.2f}")
        print(f"Inflation Rate:  {self.data.inflation_rate}% per year")
        print(f"Timeframe:       {self.data.years} years")
        print("---------------------------------")
        print(f"Future Purchasing Power: ${eroded_value:,.2f}")
        print(f"Total Value Lost to Inflation: ${total_loss:,.2f}")
        print("---------------------------------\n")


def inflation_loss_calculator():
    # Master loop keeps the calculator running until the user types "menu"
    while True:
        print("\n=== Inflation Loss Calculator ===")
        
        # 1. Validate Initial Amount (1 to 9,999,999)
        while True:
            amount_input = input("Enter your current cash amount ($): ")
            amount_input = amount_input.replace(" ", "").replace(",", "").replace("$", "")
            
            try:
                amount = float(amount_input)
                if amount < 1 or amount > 9999999:
                    print("Error: Amount must be between $1 and $9,999,999. Please try again.")
                else:
                    break
            except ValueError:
                print("Error: Please enter a valid number (e.g., 10000 or 10,000).")

        # 2. Validate Inflation Rate (0 to 999)
        while True:
            rate_input = input("Enter the expected average inflation rate (e.g., 3 for 3%): ")
            rate_input = rate_input.replace(" ", "").replace("%", "")
            
            try:
                rate = float(rate_input)
                if rate < 0 or rate > 999:
                    print("Error: Inflation rate must be between 0% and 999%. Please try again.")
                else:
                    break
            except ValueError:
                print("Error: Please enter a valid number (e.g., 3 or 3.5).")

        # 3. Validate Years (0 to 999)
        while True:
            years_input = input("Enter the number of years: ")
            years_input = years_input.replace(" ", "")
            
            try:
                years = int(years_input)
                if years < 0 or years > 999:
                    print("Error: Timeframe must be between 0 and 999 years. Please try again.")
                else:
                    break
            except ValueError:
                print("Error: Please enter a valid whole number for years.")

        # Pass the cleaned and validated data into the objects
        user_wealth = WealthData(amount, rate, years)
        calculator = InflationErosionCalculator(user_wealth)
        calculator.display_report()

        # 4. Try Again or Return to Menu
        while True:
            retry_choice = input('Would you like to calculate another scenario? (Type "Yes" to try again, or "Menu" to return): ').strip().lower()
            
            if retry_choice == "yes":
                break 
            elif retry_choice == "menu":
                print("Returning to Main Menu...")
                return 
            else:
                print('Invalid input. Please type "Yes" or "Menu".')

if __name__ == "__main__":
    inflation_loss_calculator()
