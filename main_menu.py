# Name: Nick Hendrix
# Name of Function: Display Main Menu
# Name of Use Case: Display Main Menu

import loan_interest_calculator
import investment_profile
import future_value_calculator
import opportunity_cost_calculator

class MainMenu():
    def display_menu(): # The Main Menu to select different parts of the app
        print("\n=== Don't Go Broke Investment Simulator ===")
        print("1. Select Investment Profile (2-22-26 Prototype)")
        print("2. Future Value of Investments Calculator (3-12-26 Prototype)")
        print("3. Opportunity Cost Calculator (2-22-26 prototype)")
        print("4. Target Date Savings Calculator (empty)")
        print("5. Loan Interest Calculator (3-12-26 Prototype)")
        print("6. Inflation Loss Calculator (empty)")
        print("7. Exit")

    def delay_menu(): # This is just here to stop the system from going to the main menu immediately after a calculation is done, giving the user time to read the results before going back to the menu
        while True:
            exit_choice = input('\nEnter "Menu" to go back to Main Menu: \n')
            if exit_choice.lower() == "menu":
                print("Returning to Main Menu...")
                return
            else:
                print('Please type "Menu" to return to Main Menu:')


    def main_menu():
        while True:
            MainMenu.display_menu()
            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                investment_profile.run_investment_profile()
                MainMenu.delay_menu()
            elif choice == "2":
                future_value_calculator.future_value_calculator()
                MainMenu.delay_menu()
            elif choice == "3":
                opportunity_cost_calculator.opportunity_cost_calculator()
                MainMenu.delay_menu()
            elif choice == "4":
                MainMenu.target_date_savings_calculator()
                MainMenu.delay_menu()
            elif choice == "5":
                loan_interest_calculator.loan_interest_calculator()
                MainMenu.delay_menu()
            elif choice == "6":
                MainMenu.inflation_loss_calculator()
                MainMenu.delay_menu()
            elif choice == "7":
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")


    # ===== Placeholder Functions (Team Members Implement These) =====

    def select_risk_profile():
        print("Risk Tolerance Profile Selected (placeholder)")



    def target_date_savings_calculator():
        print("Target Date Savings Calculator (placeholder)")


    def inflation_loss_calculator():
        print("Inflation Loss Calculator (placeholder)")