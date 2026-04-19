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
        self.monthly_contribution = self._validate_monthly(monthly_contribution)
    
    # Validation for monthly contribution
    def _validate_monthly(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Monthly contribution must be a number.")
        
        if value > 9999:  # Arbitrary upper limit to catch unrealistic inputs
            raise ValueError("Monthly contribution must be less than 10,000.")

        if value < 0:
            raise ValueError("Monthly contribution cannot be negative.")

        return value

    # ----------------------------------------
    # Lump Sum Growth
    # ----------------------------------------
    def calculate_lump_sum(self):
        """
        FV = P(1 + r)^t
        """
        return self.principal * (1 + self.rate/12) ** (self.years * 12)

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
        try:
            lump_growth = self.principal * (1 + monthly_rate) ** total_months
        except OverflowError:
            raise ValueError("Total investment value is too large.")

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
        principal = input("Enter initial investment amount (< $10,000,000): ")
        rate = input("Enter expected annual return (as %) (< 1000): ")
        years = input("Enter number of years invested: (< 100): ")
        monthly = input("Enter monthly contribution (0 if none) (< 10,000): ")

        # Create calculator object
        investment = FutureValueCalculator(principal, rate, years, monthly)

        # Perform calculations
        lump_sum_value = investment.calculate_lump_sum()
        total_value = investment.calculate_with_contributions()

        print("\n--- Investment Summary ---")
        print(f"Initial Investment: ${investment.principal:,.2f}")
        print(f"Annual Return: {investment.rate * 100:.2f}%")
        print(f"Years Invested: {investment.years}")
        print(f"Monthly Contribution: ${investment.monthly_contribution:,.2f}")

        print(f"\nFuture Value (Lump Sum Only): ${lump_sum_value:,.2f}")
        print(f"Future Value (With Contributions): ${total_value:,.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
        print("Please restart the calculator and enter valid inputs.")