# Name: Mark
# Name of Function: Display Main Menu
# Name of Use Case: Display Main Menu
"""
Program Name: Dont Go Broke Investment Simulator
Module: Inflation Loss Calculator
"""

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
        future_power = self.data.initial_amount / ((1 + rate_decimal) ** self.data.years)
        return future_power

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
    print("\n=== Inflation Loss Calculator ===")
    
    try:
        amount_input = input("Enter your current cash amount ($): ")
        rate_input = input("Enter the expected average inflation rate (e.g., 3 for 3%): ")
        years_input = input("Enter the number of years: ")
        
        user_wealth = WealthData(amount_input, rate_input, years_input)
        calculator = InflationErosionCalculator(user_wealth)
        calculator.display_report()
        
    except ValueError:
        print("\nError: Please enter valid numbers only.")


if __name__ == "__main__":
    inflation_loss_calculator()