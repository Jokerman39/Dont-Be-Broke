# Name: Mateo Meconi
# Name of Function: calculate_growth
# Name of Use Case: Create Investment Profile


class InvestmentProfile:

    def __init__(self, name, age, initial_investment, current_investment,
                 marital_status, risk_tolerance):
        self.name = name
        self.age = age
        self.initial_investment = initial_investment
        self.current_investment = current_investment
        self.marital_status = marital_status
        self.risk_tolerance = risk_tolerance

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

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_valid_choice(prompt, valid_options):
    while True:
        value = input(prompt).strip()
        if value in valid_options:
            return value
        else:
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")


# -----------------------------
# PROFILE CREATION FUNCTION
# -----------------------------

def create_profile():
    
    name = input("Enter client name: ").strip()
    age = get_valid_int("Enter client age: ")
    initial_investment = get_valid_float("Enter initial investment amount: ")
    current_investment = get_valid_float("Enter current investment amount: ")
    marital_status = get_valid_choice(
        "Enter marital status (Single/Spouse): ",
        ["Single", "Spouse"]
    )
    risk_tolerance = get_valid_choice(
        "Enter risk tolerance (Low/Medium/High): ",
        ["Low", "Medium", "High"]
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

def run_investment_profile():
    """
    This is the ONE function you will import and call in main.py.
    It creates the profile and calculates growth.
    """
    client = create_profile()
    calculate_growth_result = client.calculate_growth()
    print(calculate_growth_result)
    print()