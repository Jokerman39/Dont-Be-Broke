"""
Course: ITM320
Use Case: Create Investment Profile
Author: Mateo Meconi
Description: Given a name, age, initial investment amount, current investment amount,
marital status, and risk tolerance, this tool creates an investment profile for the user
based on their inputs.
"""

class InvestmentProfile:
    # Initializes the class with all of the attributes needed for a new object.
    def __init__(self, name, age, initial_investment, current_investment,
                 marital_status, risk_tolerance):
        self.name = name
        self.age = age
        self.initial_investment = initial_investment
        self.current_investment = current_investment
        self.marital_status = marital_status
        self.risk_tolerance = risk_tolerance
    # Calculates the net change between the initial and current investment and tells the
    # user what type of change has occured with their investments.
    def calculate_growth(self):
        growth = self.current_investment - self.initial_investment

        if growth > 0:
            status = "gained"
        elif growth < 0:
            status = "lost"
        else:
            status = "maintained"

        return f"Client {self.name} has {status} ${abs(growth):,.2f} since their initial deposit."


# -----------------------------
# INPUT VALIDATION HELPERS
# -----------------------------

# Analyzes input for name variable to make sure of valid name. Cannot include numbers or
# any characters not specified.
def get_valid_name(prompt):
    while True:
        value = input(prompt).strip()
        # Rejects blank input given by user.
        if not value:
            print("Name cannot be blank. Please enter a valid client name.")
            continue

        # Allow letters, spaces, hyphens, and apostrophes in names.
        if all(part.replace("-", "").replace("'", "").isalpha() for part in value.split()):
            return value

        print("Invalid name. Please enter only letters, spaces, hyphens, or apostrophes.")

# Makes sure that the input for age variable is within the realistic bounds (0-100 years old).
def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Cannot have a negative age, please input an age 0 or above.")
            elif value > 100:
                print("Please input a realistic age (100 or below).")
            else:
                return value
        # Prevents inputs that are anything but a whole number.
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Validates that the input is a non-negative number, that is no larger than 1 billion.
def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Cannot have a negative investment, please input a positive value.")
            elif value > 1000000000:
                print("Please input a realistic investment amount (1 billion or below).")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Makes sure that the input form user is one of the choices provided in the prompt.
def get_valid_choice(prompt, valid_options):
    while True:
        value = input(prompt).strip().lower()
        if value in valid_options:
            return value
        else:
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")


# -----------------------------
# PROFILE CREATION FUNCTION
# -----------------------------

# Calls each input validation helper to gather the user's name, age, inital investment,
# current investment, marital status, and risk tolerance.
def create_profile():
    
    name = get_valid_name("Enter client name: ")
    age = get_valid_int("Enter client age: ")
    initial_investment = get_valid_float("Enter initial investment amount: ")
    current_investment = get_valid_float("Enter current investment amount: ")
    marital_status = get_valid_choice(
        "Enter marital status (Single/Spouse): ",
        ["single", "spouse"]
    )
    risk_tolerance = get_valid_choice(
        "Enter risk tolerance (Low/Medium/High): ",
        ["low", "medium", "high"]
    )

    return InvestmentProfile(
        name,
        age,
        initial_investment,
        current_investment,
        marital_status,
        risk_tolerance
    )


# -----------------------------
# SINGLE RUN FUNCTION
# -----------------------------

# This is the entry point for creating a new investment profile for user. Used as the
# connection between the profile creation and the main menu.
def run_investment_profile():
    """
    This is the ONE function you will import and call in main.py.
    It creates the profile and calculates growth.
    """
    client = create_profile()
    calculate_growth_result = client.calculate_growth()
    print(calculate_growth_result)
    print()
