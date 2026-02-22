# Name: Mateo Meconi
# Name of Function: calculate_growth
# Name of Use Case: Create Investment Profile
class InvestmentProfile:

    
    def __init__(self, name, age, initial_investment, current_investment, 
                 marital_status, risk_tolerance):
        # Attributes
        self.name = name
        self.age = age
        self.initial_investment = initial_investment
        self.current_investment = current_investment
        self.marital_status = marital_status  # Expected: 'Spouse' or 'Single'
        self.risk_tolerance = risk_tolerance  # Expected: 'Low', 'Medium', 'High'
        
    def calculate_growth(self):
        """
        Calculates the total growth or loss of the investment since inception.
        """
        growth = self.current_investment - self.initial_investment
        
        # A little logic to provide a witty summary
        if growth > 0:
            status = "gained"
        elif growth < 0:
            status = "lost"
        else:
            status = "maintained"
            
        return f"Client {self.name} has {status} ${abs(growth)} since their initial deposit."

# Example of how to instantiate the class:
client_01 = InvestmentProfile(
    name="Alex Sterling",
    age=34,
    initial_investment=50000,
    current_investment=62500,
    marital_status="Single",
    risk_tolerance="High",
)

print(client_01.calculate_growth())