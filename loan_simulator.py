# Name: Nick Hendrix
# Class Name: LoanSimulator
# Description: Component class for loan simulation logic

class LoanSimulator:
    """
    The 'Component' class.
    Handles the month-by-month math for the main calculator.
    """
    def run(self, principal, rate, years, monthly_payment, extra_payment=0):
        monthly_rate = rate / 12
        balance = principal
        total_interest = 0
        months = 0

        while balance > 0:
            interest = balance * monthly_rate
            principal_payment = monthly_payment - interest + extra_payment

            if principal_payment > balance:
                principal_payment = balance

            balance -= principal_payment
            total_interest += interest
            months += 1

        return months, total_interest
