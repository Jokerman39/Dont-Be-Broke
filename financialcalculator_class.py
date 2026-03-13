# Name: Nick Hendrix
# Name of Class FinancialCalulator:
# Common class to assign common attributes of financial investments (principal, interest/earnings rate, time in yrs of loan/investment)

class FinancialCalculator:
    """

    Base class for all financial calculators.
    Stores common financial attributes.
    """

    def __init__(self, principal, rate, years):
        self.principal = principal        # Original loan amount
        self.rate = rate                  # Annual interest rate (decimal form)
        self.years = years                # Loan duration in years

    def display_summary(self):
        """Displays basic loan information."""
        print(f"Principal: ${self.principal:,.2f}")
        print(f"Interest Rate: {self.rate * 100:.2f}%")
        print(f"Loan Term: {self.years} years")