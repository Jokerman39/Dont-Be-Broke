import loan_interest_calculator
"""
Program Name: TimeValue Investment Simulator
Course: ITM320
Description: Main menu for financial calculation application
Author(s): Team Name
"""

def display_menu():
    print("\n=== TimeValue Investment Simulator ===")
    print("1. Select Risk Tolerance Profile")
    print("2. Future Value of Investments Calculator")
    print("3. Opportunity Cost Calculator")
    print("4. Target Date Savings Calculator")
    print("5. Loan Interest Calculator")
    print("6. Inflation Loss Calculator")
    print("7. Exit")

def delay_menu():
    while True:
        exit_choice = input('Enter "Menu" to go back to Main Menu: \n')
        if exit_choice.lower() == "menu":
            print("Returning to Main Menu...")
            return
        else:
            print('Please type "Menu" to return to Main Menu: \n')


def main_menu():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            select_risk_profile()
            delay_menu()
        elif choice == "2":
            future_value_calculator()
            delay_menu()
        elif choice == "3":
            opportunity_cost_calculator()
            delay_menu()
        elif choice == "4":
            target_date_savings_calculator()
            delay_menu()
        elif choice == "5":
            loan_interest_calculator.loan_interest_calculator()
            delay_menu()
        elif choice == "6":
            inflation_loss_calculator()
            delay_menu()
        elif choice == "7":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# ===== Placeholder Functions (Team Members Implement These) =====

def select_risk_profile():
    print("Risk Tolerance Profile Selected (placeholder)")


def future_value_calculator():
    print("Future Value Calculator (placeholder)")


def opportunity_cost_calculator():
    print("Opportunity Cost Calculator (placeholder)")


def target_date_savings_calculator():
    print("Target Date Savings Calculator (placeholder)")


def inflation_loss_calculator():
    print("Inflation Loss Calculator (placeholder)")

if __name__ =="__main__":
    main_menu()