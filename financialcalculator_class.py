# Name: Nick Hendrix
# Name of Class FinancialCalulator:
# Common class to assign common attributes of financial investments (principal, interest/earnings rate, time in yrs of loan/investment)

class FinancialCalculator:
    """

    Base class for all financial calculators.
    Stores common financial attributes.
    """

    def __init__(self, principal, rate, years):
        self.principal = self._validate_principal(principal)
        self.rate = self._validate_rate(rate)
        self.years = self._validate_years(years)

    # --- Validation Methods ---

    def _validate_principal(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Principal must be a number.")
        
        if value > 9999999 :  # Arbitrary upper limit to catch unrealistic inputs
            raise ValueError("Principal must be less than 10,000,000.")

        if value <= 0:
            raise ValueError("Principal must be greater than 0.")

        return value

    def _validate_rate(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Interest rate must be a number.")

        # Allow user to enter 7 instead of 0.07
        if value > 0 and value < 1000:  # Arbitrary upper limit to catch unrealistic rates
            value = value / 100
        else: 
            raise ValueError("Interest rate must be a positive number less than 1000%.")

        if value < 0:
            raise ValueError("Interest rate must be greater than 0.")

        return value

    def _validate_years(self, value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Years must be an integer.")
        
        if value > 99:  # Arbitrary upper limit to catch unrealistic inputs
            raise ValueError("Years must be less than 100.")

        if value <= 0:
            raise ValueError("Years must be greater than 0.")

        return value

    def display_summary(self):
        """Displays basic loan information."""
        print(f"Principal: ${self.principal:,.2f}")
        print(f"Interest Rate: {self.rate * 100:.2f}%")
        print(f"Loan Term: {self.years} years")