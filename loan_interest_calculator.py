# Name: Nick Hendrix
# Name of Function: loan_interest_calculator
# Name of Use Case: Calculate Loan Cost
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

class LoanInterestCalculator(FinancialCalculator):
    """
    Loan calculator that computes:
    - Monthly payment
    - Total interest
    - Impact of extra monthly payments
    """

    def __init__(self, principal, rate, years):
        super().__init__(principal, rate, years)

    # ----------------------------------------
    # Standard Monthly Payment Calculation
    # ----------------------------------------
    def calculate_monthly_payment(self):
        """
        Uses amortization formula:
        M = P * [ r(1+r)^n ] / [ (1+r)^n - 1 ]
        """

        monthly_rate = self.rate / 12
        total_payments = self.years * 12

        # If interest rate is 0%, avoid division formula
        if monthly_rate == 0:
            return self.principal / total_payments

        payment = (
            self.principal *
            (monthly_rate * (1 + monthly_rate) ** total_payments) /
            ((1 + monthly_rate) ** total_payments - 1)
        )

        return payment

    # ----------------------------------------
    # Simulate Loan with Optional Extra Payment
    # ----------------------------------------
    def simulate_loan(self, extra_payment=0):
        """
        Simulates paying the loan month-by-month.
        Returns:
        - months needed to pay off loan
        - total interest paid
        """

        monthly_rate = self.rate / 12
        balance = self.principal
        monthly_payment = self.calculate_monthly_payment()
        total_interest = 0
        months = 0

        # Continue until loan is fully paid
        while balance > 0:
            interest = balance * monthly_rate
            principal_payment = monthly_payment - interest + extra_payment

            # Prevent overpaying in final month
            if principal_payment > balance:
                principal_payment = balance

            balance -= principal_payment
            total_interest += interest
            months += 1

        return months, total_interest 

def loan_interest_calculator():
    while True: # Starts the loop to check and make sure integers are used.
        print("\n=== Loan Interest Calculator ===")

        try:
            # Gather user input
            principal = float(input("Enter loan amount: "))
            rate = float(input("Enter annual interest rate (as %): ")) / 100
            years = int(input("Enter loan term in years: "))
            extra_payment = float(input("Enter extra monthly payment (0 if none): "))

            # Create Loan Calculator object
            loan = LoanInterestCalculator(principal, rate, years)

            # Calculate standard loan results
            standard_monthly = loan.calculate_monthly_payment()
            standard_months, standard_interest = loan.simulate_loan(0)

            # Calculate loan with extra payments
            extra_months, extra_interest = loan.simulate_loan(extra_payment)

            # Convert months to years for readability
            standard_years = standard_months / 12
            extra_years = extra_months / 12

            # Display Results
            print("\n--- Standard Loan ---")
            loan.display_summary()
            print(f"Monthly Payment: ${standard_monthly:,.2f}")
            print(f"Time to Pay Off: {standard_months} months ({standard_years:.2f} years)")
            print(f"Total Interest Paid: ${standard_interest:,.2f}")

            print("\n--- With Extra Payments ---")
            print(f"Extra Monthly Payment: ${extra_payment:,.2f}")
            print(f"New Payoff Time: {extra_months} months ({extra_years:.2f} years)")
            print(f"New Total Interest Paid: ${extra_interest:,.2f}")

            # Show savings
            months_saved = standard_months - extra_months
            interest_saved = standard_interest - extra_interest

            print("\n--- Savings ---")
            print(f"Time Saved: {months_saved} months")
            print(f"Interest Saved: ${interest_saved:,.2f}", end="\n\n")

        except ValueError: # if string is entered prints an exception and starts the menu over again
            print("Invalid input. Please enter numeric values only.")
        
        else:
            break # if integers were input earlier breaks the loop 