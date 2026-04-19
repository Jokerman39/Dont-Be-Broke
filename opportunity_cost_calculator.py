"""
Program Name: Daily Overspending Opportunity Cost Calculator
Course: ITM320
Use Case: Opportunity Cost Calculator
Author: Mark Palsulich
Description: Calculates the lost potential investment gains from daily extra spending
             based on annual return over a set time frame.
"""

class OpportunityCostCalculator:
    """
    Class: OpportunityCostCalculator
    Description: Computes opportunity cost for money spent instead of invested
    """

    def __init__(self, daily_extra: float, years: int, annual_return: float):
        self.daily_extra = daily_extra
        self.years = years
        self.annual_return = annual_return

    def calculate_wasted_amount(self) -> float:
        P = self.daily_extra
        r = self.annual_return / 100
        t = self.years
        n = 365  # daily compounding

        # PREVENT CRASH: If the rate is 0%, the standard formula divides by zero and crashes.
        # If rate is 0, they just save the cash with no interest.
        if r == 0:
            return P * n * t

        try:
            # Future Value of a series formula (daily contributions)
            fv = P * (((1 + r/n)**(n*t) - 1) / (r/n))
            return fv
        except OverflowError:
            # If the numbers get too big for Python memory, return -1 as a warning flag
            return -1.0


def opportunity_cost_calculator():
    # Master loop keeps the calculator running until the user types "menu"
    while True:
        print("\n=== Daily Overspending Opportunity Cost Calculator ===")
        
        # 1. Validate Daily Spend (0 to 9,999,999)
        while True:
            daily_input = input("Enter how much extra you spend per day ($): ")
            daily_input = daily_input.replace(" ", "").replace(",", "").replace("$", "")
            
            try:
                daily_extra = float(daily_input)
                if daily_extra < 0 or daily_extra > 9999999:
                    print("Error: Amount must be between $0 and $9,999,999. Please try again.")
                else:
                    break
            except ValueError:
                print("Error: Please enter a valid number (e.g., 5 or 5.50).")

        # 2. Validate Years (0 to 999)
        while True:
            years_input = input("Enter the number of years you want to calculate: ")
            years_input = years_input.replace(" ", "")
            
            try:
                years = int(years_input)
                if years < 0 or years > 999:
                    print("Error: Timeframe must be between 0 and 999 years. Please try again.")
                else:
                    break
            except ValueError:
                print("Error: Please enter a valid whole number for years.")

        # 3. Validate Annual Return (0 to 999)
        while True:
            rate_input = input("Enter expected annual return percentage (e.g., 7 for 7%): ")
            rate_input = rate_input.replace(" ", "").replace("%", "")
            
            try:
                annual_return = float(rate_input)
                if annual_return < 0 or annual_return > 999:
                    print("Error: Return rate must be between 0% and 999%. Please try again.")
                else:
                    break
            except ValueError:
                print("Error: Please enter a valid number (e.g., 7 or 7.5).")

        # Run calculations
        calculator = OpportunityCostCalculator(daily_extra, years, annual_return)
        wasted_amount = calculator.calculate_wasted_amount()

        # Display cleanly formatted results
        print("\n--- Opportunity Cost Results ---")
        print(f"Daily Overspending: ${daily_extra:,.2f} per day")
        print(f"Timeframe:          {years} years")
        print(f"Investment Return:  {annual_return}% per year")
        print("--------------------------------")
        
        if wasted_amount == -1.0:
            print("Potential Wealth Lost: An astronomically large number (Overflow limit reached).")
        else:
            print(f"Potential Wealth Lost: ${wasted_amount:,.2f}")
            
        print("--------------------------------\n")
        
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
    opportunity_cost_calculator()
