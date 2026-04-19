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

        try:
            payment = (
                self.principal *
                (monthly_rate * (1 + monthly_rate) ** total_payments) /
                ((1 + monthly_rate) ** total_payments - 1)
                )
            return payment
        except OverflowError:
            raise ValueError("Calculated monthly payment is too large.")

    def run_full_analysis(self, extra_payment=0):
        """Coordinates the math and display logic."""
        monthly_payment = self.calculate_monthly_payment()
        extra_payment = self._validate_extra(extra_payment)

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
        print(f"Total Months: {std_months}\n")
        
        if extra_payment > 0:
            print(f"Total Interest (With Extra): ${ext_interest:,.2f}")
            print(f"Interest Saved: ${std_interest - ext_interest:,.2f}")
            print(f"Months with Extra Payment: {ext_months}")
            print(f"Months saved: {std_months - ext_months}")
        
    # --- Validation for extra payment input ---
    def _validate_extra(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Extra payment must be a number.")
        
        if value >= self.principal:  # Extra payment should not exceed the principal
            raise ValueError("Extra payment must be less than the loan amount.")

        if value < 0:
            raise ValueError("Extra payment cannot be negative.")

        return value

# ---------------------------------------------------------
# ENTRY POINT FOR MAIN MENU
# ---------------------------------------------------------
def loan_interest_calculator():
    """Function called by MainMenu.py."""
    try:
        p = input("Enter loan amount: (< $10,000,000) ")
        r = input("Enter rate (%): (< 1000) ")
        y = input("Enter years: (< 100) ")
        ex = input("Extra payment: (< $10,000,000) ")

        app = LoanInterestCalculator(p, r, y)
        app.run_full_analysis(extra_payment=ex)

    except ValueError as e:
        print(f"Error: {e}")
        print("Please restart the calculator and enter valid inputs.")
 