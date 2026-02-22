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
        """
        Constructor
        :param daily_extra: Extra daily spending in dollars
        :param years: Time frame in years
        :param annual_return: Expected annual return rate in percent
        """
        self.daily_extra = daily_extra
        self.years = years
        self.annual_return = annual_return

    def calculate_wasted_amount(self) -> float:
        """
        Method: calculate_wasted_amount
        Description: Uses compound interest formula to calculate lost investment growth
                     Formula: FV = P * ((1 + r/n)^(n*t) - 1) / (r/n)
                     where P = daily contribution, r = annual return rate, n = compounding per year
        :return: Total wasted amount in dollars
        """
        P = self.daily_extra
        r = self.annual_return / 100
        t = self.years
        n = 365  # daily compounding

        # Future Value of a series formula (daily contributions)
        fv = P * (((1 + r/n)**(n*t) - 1) / (r/n))
        return fv


def opportunity_cost_calculator():
    """
    Function: opportunity_cost_calculator
    Description: Prompts user input and displays the wasted potential investment growth
    """
    print("\n=== Daily Overspending Opportunity Cost Calculator ===")
    try:
        daily_extra = float(input("Enter how much extra you spend per day: $"))
        years = int(input("Enter the number of years you want to calculate: "))
        annual_return = float(input("Enter expected annual return percentage (e.g., 7 for 7%): "))

        calculator = OpportunityCostCalculator(daily_extra, years, annual_return)
        wasted_amount = calculator.calculate_wasted_amount()

        print(f"\nIf you invested that money instead, you could have: ${wasted_amount:,.2f} in {years} years!")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for daily spending, years, and return rate.")