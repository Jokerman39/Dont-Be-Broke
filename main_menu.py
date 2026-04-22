# Name: Nick Hendrix
# Name of Function: Display Main Menu
# Name of Use Case: Display Main Menu

import loan_interest_calculator
import investment_profile
import future_value_calculator
import opportunity_cost_calculator
import target_date_savings_calculator
import inflation_erode_calculator
"""
Program Name: Dont Go Broke Investment Simulator
Course: ITM320
Description: Main menu for financial calculation application
Author(s): Team A+
"""
class MainMenu:

    @staticmethod # Static method to display the main menu options to the user
    def display_menu():
        print("\n=== Don't Go Broke Investment Simulator ===")
        print("1. Select Investment Profile")
        print("2. Future Value of Investments Calculator")
        print("3. Opportunity Cost Calculator")
        print("4. Target Date Savings Calculator")
        print("5. Loan Interest Calculator")
        print("6. Inflation Loss Calculator")
        print("7. Exit")

    @staticmethod # Static method to handle the delay before returning to the main menu after a calculation is completed
    def delay_menu():
        while True:
            exit_choice = input('Enter "Menu" to go back to Main Menu: \n')
            if exit_choice.lower() == "menu":
                print("Returning to Main Menu...")
                return
            else:
                print('Please type "Menu" to return to Main Menu: \n')

    @staticmethod # Static method to run the main menu loop, allowing the user to select different financial calculators and return to the main menu after each calculation
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
                target_date_savings_calculator.target_date_calculator()
                MainMenu.delay_menu()

            elif choice == "5":
                loan_interest_calculator.loan_interest_calculator()
                MainMenu.delay_menu()

            elif choice == "6":
                inflation_erode_calculator.inflation_loss_calculator()
                MainMenu.delay_menu()

            elif choice == "7":
                print("Exiting application. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")


    # ===== Placeholder Functions (Team Members Implement These) =====


if __name__ =="__main__":
    MainMenu.main_menu()
