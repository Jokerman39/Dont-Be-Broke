# Name: Nick Hendrix
# Name of Function: future_value_calculator
# Name of Use Case: Calculate future investments

from financialcalculator_class import FinancialCalculator

class FutureValueCalculator(FinancialCalculator):
    """
    Calculates future value of an investment.
    Supports lump sum and optional monthly contributions.
    """

    def __init__(self, principal, rate, years, monthly_contribution=0):
        super().__init__(principal, rate, years)
        self.monthly_contribution = monthly_contribution

    # ----------------------------------------
    # Lump Sum Growth
    # ----------------------------------------
    def calculate_lump_sum(self):
        """
        FV = P(1 + r)^t
        """
        return self.principal * (1 + self.rate) ** self.years

    # ----------------------------------------
    # Growth With Monthly Contributions
    # ----------------------------------------
    def calculate_with_contributions(self):
        """
        Calculates future value including monthly contributions.
        """

        monthly_rate = self.rate / 12
        total_months = self.years * 12

        # Future value of initial principal
        lump_growth = self.principal * (1 + self.rate) ** self.years

        if monthly_rate == 0:
            contribution_growth = self.monthly_contribution * total_months
        else:
            contribution_growth = (
                self.monthly_contribution *
                (((1 + monthly_rate) ** total_months - 1) / monthly_rate)
            )

        return lump_growth + contribution_growth
    
def future_value_calculator():
    print("\n=== Future Value of Investment Calculator ===")

    try:
        principal = float(input("Enter initial investment amount: "))
        rate = float(input("Enter expected annual return (as %): ")) / 100
        years = int(input("Enter number of years invested: "))
        monthly = float(input("Enter monthly contribution (0 if none): "))

        # Create calculator object
        investment = FutureValueCalculator(principal, rate, years, monthly)

        # Perform calculations
        lump_sum_value = investment.calculate_lump_sum()
        total_value = investment.calculate_with_contributions()

        print("\n--- Investment Summary ---")
        print(f"Initial Investment: ${principal:,.2f}")
        print(f"Annual Return: {rate * 100:.2f}%")
        print(f"Years Invested: {years}")
        print(f"Monthly Contribution: ${monthly:,.2f}")

        print(f"\nFuture Value (Lump Sum Only): ${lump_sum_value:,.2f}")
        print(f"Future Value (With Contributions): ${total_value:,.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")