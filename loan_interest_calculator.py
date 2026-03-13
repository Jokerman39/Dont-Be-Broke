# Name: Nick Hendrix
# File: loan_interest_calculator.py
# Description: Main calculator class using Composition and Inheritance

from financialcalculator_class import FinancialCalculator
# Import the component class from its separate file
from loan_simulator import LoanSimulator

class LoanInterestCalculator(FinancialCalculator):
    """
    The 'Owner' class.
    Inherits from FinancialCalculator.
    COMPOSITION: Uses LoanSimulator to perform calculations.
    """
    def __init__(self, principal, rate, years):
        super().__init__(principal, rate, years)
        
        # COMPOSITION: Create an instance of the class from the other file
        self.simulator = LoanSimulator()

    def calculate_monthly_payment(self):
        """Standard amortization formula."""
        monthly_rate = self.rate / 12
        total_payments = self.years * 12
        if monthly_rate == 0:
            return self.principal / total_payments

        payment = (
            self.principal *
            (monthly_rate * (1 + monthly_rate) ** total_payments) /
            ((1 + monthly_rate) ** total_payments - 1)
        )
        return payment

    def run_full_analysis(self, extra_payment=0):
        """Coordinates the math and display logic."""
        monthly_payment = self.calculate_monthly_payment()

        # DELEGATION: Asking the internal simulator object to do the work
        std_months, std_interest = self.simulator.run(
            self.principal, self.rate, self.years, monthly_payment, 0
        )
        ext_months, ext_interest = self.simulator.run(
            self.principal, self.rate, self.years, monthly_payment, extra_payment
        )

        print("\n--- Loan Analysis Results ---")
        self.display_summary()
        print(f"Monthly Payment: ${monthly_payment:,.2f}")
        print(f"Total Interest (Standard): ${std_interest:,.2f}")
        
        if extra_payment > 0:
            print(f"Total Interest (With Extra): ${ext_interest:,.2f}")
            print(f"Interest Saved: ${std_interest - ext_interest:,.2f}")

# ---------------------------------------------------------
# ENTRY POINT FOR MAIN MENU
# ---------------------------------------------------------
def loan_interest_calculator():
    """Function called by MainMenu.py."""
    try:
        p = float(input("Enter loan amount: "))
        r = float(input("Enter rate (%): ")) / 100
        y = int(input("Enter years: "))
        ex = float(input("Extra payment: "))

        app = LoanInterestCalculator(p, r, y)
        app.run_full_analysis(extra_payment=ex)

    except ValueError:
        print("Error: Please enter numbers only.")
 