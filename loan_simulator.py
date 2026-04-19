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
        max_months = years * 12

        while balance > 0 and months < max_months: # While the loan is not fully paid off it will continue to calculate the interest and principal payment for each month
            interest = balance * monthly_rate
            principal_payment = monthly_payment - interest + extra_payment

            if principal_payment > balance: # If the principal payment exceeds the remaining balance, adjust it to pay off the loan
                interest = balance * monthly_rate
                principal_payment = balance

            balance -= principal_payment # Reduce the balance by the principal payment
            total_interest += interest
            months += 1

        return months, total_interest
