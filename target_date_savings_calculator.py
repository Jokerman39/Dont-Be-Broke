"""
Course: ITM320
Use Case: Target Date Savings Rate Calculator
Author: Mateo Meconi
Description: Given a future savings goal, a target date, and an expected annual return,
this tool calculates how much you need to save periodically (monthly/weekly/daily)
to reach your goal — accounting for compound interest.
"""

from datetime import date, datetime
import math


class SavingsCalculator:
    """
    Encapsulates all logic for the Target Date Savings Rate Calculator.

    Attributes:
        goal            (float) : The future dollar amount you want to reach.
        target_date     (date)  : The date by which you want to reach the goal.
        current_savings (float) : How much you've already saved today.
        annual_rate     (float) : Expected annual return rate as a percentage.
        months          (float) : Months between today and target_date (computed).
        monthly_pmt     (float) : Required monthly contribution (computed).
    """

    # ──────────────────────────────────────────────
    # Construction & setup
    # ──────────────────────────────────────────────

    def __init__(
        self,
        goal: float,
        target_date: date,
        current_savings: float = 0.0,
        annual_rate: float = 0.0,
    ) -> None:
        self.goal            = goal
        self.target_date     = target_date
        self.current_savings = current_savings
        self.annual_rate     = annual_rate

        # Derived fields — computed once on init
        self.months      = self._months_until(target_date)
        self.monthly_pmt = self._calc_monthly_contribution()

    # ──────────────────────────────────────────────
    # Core calculations (private)
    # ──────────────────────────────────────────────

    @staticmethod
    def _months_until(target_date: date) -> float:
        """Return the number of months between today and target_date."""
        delta_days = (target_date - date.today()).days
        if delta_days <= 0:
            raise ValueError("Target date must be in the future.")
        return delta_days / 30.4375          # average days per month

    def _calc_monthly_contribution(self) -> float:
        """
        Return the fixed monthly contribution needed to reach the goal.

        Uses the Future Value of an Ordinary Annuity formula:
            FV  = PMT * [((1+r)^n - 1) / r]  +  PV * (1+r)^n

        Solving for PMT:
            PMT = (FV - PV*(1+r)^n) / [((1+r)^n - 1) / r]

        Where:
            FV  = goal (future value target)
            PV  = current_savings (present value already saved)
            r   = monthly interest rate
            n   = number of months
        """
        r = self.annual_rate / 12 / 100      # monthly rate as decimal
        n = self.months
        growth_factor = (1 + r) ** n

        fv_current = self.current_savings * growth_factor
        remaining  = self.goal - fv_current

        if remaining <= 0:
            return 0.0                       # already on track!
        if r == 0:
            return remaining / n             # no interest — simple division

        return remaining / ((growth_factor - 1) / r)

    def update_rate(self, new_annual_rate: float) -> None:
        """Recalculate with a new annual return rate."""
        self.annual_rate = new_annual_rate
        self.monthly_pmt = self._calc_monthly_contribution()

    # ──────────────────────────────────────────────
    # Display helpers (private)
    # ──────────────────────────────────────────────

    @staticmethod
    def _fmt(amount: float) -> str:
        return f"${amount:,.2f}"

    def print_summary(self) -> None:
        """Print a formatted summary of the savings plan."""
        years  = self.months / 12
        weekly = self.monthly_pmt * 12 / 52
        daily  = self.monthly_pmt * 12 / 365

        total_contributions = self.current_savings + self.monthly_pmt * self.months
        interest_earned     = self.goal - total_contributions

        print("\n" + "=" * 52)
        print("        TARGET DATE SAVINGS RATE CALCULATOR")
        print("=" * 52)
        print(f"  Savings Goal          : {self._fmt(self.goal)}")
        print(f"  Target Date           : {self.target_date.strftime('%B %d, %Y')}")
        print(f"  Time Remaining        : {years:.1f} years ({self.months:.0f} months)")
        print(f"  Current Savings       : {self._fmt(self.current_savings)}")
        print(f"  Expected Annual Return: {self.annual_rate:.2f}%")
        print("-" * 52)
        print(f"  Required Monthly Save : {self._fmt(self.monthly_pmt)}")
        print(f"  Required Weekly Save  : {self._fmt(weekly)}")
        print(f"  Required Daily Save   : {self._fmt(daily)}")
        print("-" * 52)
        print(f"  Total You'll Deposit  : {self._fmt(total_contributions)}")
        print(f"  Interest Earned       : {self._fmt(interest_earned)}")
        print(f"  Final Balance         : {self._fmt(self.goal)}")
        print("=" * 52 + "\n")

    def print_yearly_breakdown(self) -> None:
        """Print a year-by-year balance growth table."""
        r            = self.annual_rate / 12 / 100
        balance      = self.current_savings
        total_months = int(math.ceil(self.months))

        print("  Year-by-Year Breakdown")
        print(f"  {'Year':>4}  {'Balance':>14}  {'Deposited':>12}  {'Interest':>12}")
        print("  " + "-" * 46)

        year_num = 0
        for m in range(1, total_months + 1):
            balance = balance * (1 + r) + self.monthly_pmt
            if m % 12 == 0 or m == total_months:
                year_num += 1
                deposited = self.current_savings + self.monthly_pmt * m
                interest  = balance - deposited
                print(
                    f"  {year_num:>4}  {self._fmt(balance):>14}  "
                    f"{self._fmt(deposited):>12}  {self._fmt(interest):>12}"
                )
        print()


# ──────────────────────────────────────────────
# Input helpers (module-level utilities)
# ──────────────────────────────────────────────

def get_float(prompt: str, min_val: float = 0.0, max_val: float | None = None) -> float:
    while True:
        try:
            value = float(input(prompt).replace(",", "").replace("$", ""))
            if value < min_val:
                print(f"  ⚠  Please enter a value >= {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"  ⚠  Please enter a value <= {max_val}.")
                continue
            return value
        except ValueError:
            print("  ⚠  Invalid input — please enter a number.")


def get_goal(prompt: str) -> float:
    return get_float(prompt, min_val=1.0, max_val=1000000000)  # Max $1 billion


def get_current_savings(prompt: str) -> float:
    return get_float(prompt, min_val=0.0, max_val=1000000000)  # Max $1 billion


def get_annual_rate(prompt: str) -> float:
    return get_float(prompt, min_val=0.0, max_val=50.0)  # Max 50% return


def get_date(prompt: str) -> date:
    while True:
        raw = input(prompt).strip()
        parsed = None
        for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%m-%d-%Y"):
            try:
                parsed = datetime.strptime(raw, fmt).date()
                break
            except ValueError:
                continue
        if parsed is None:
            print("  ⚠  Use YYYY-MM-DD or MM/DD/YYYY format.")
            continue
        if parsed <= date.today():
            print("  ⚠  Date must be in the future.")
            continue
        return parsed


# ──────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────

def target_date_calculator():
    print("\n╔══════════════════════════════════════════════════╗")
    print("║     TARGET DATE SAVINGS RATE CALCULATOR          ║")
    print("╚══════════════════════════════════════════════════╝")
    print("  Calculate exactly how much to save each month,")
    print("  week, or day to hit your financial goal.\n")

    goal            = get_goal("  💰 Savings goal ($):              ")
    target_date     = get_date ("  📅 Target date (YYYY-MM-DD):      ")
    current_savings = get_current_savings("  🏦 Current savings ($):           ")
    annual_rate     = get_annual_rate("  📈 Expected annual return (%):    ")

    # Instantiate the main class — all math happens here
    calc = SavingsCalculator(goal, target_date, current_savings, annual_rate)
    calc.print_summary()

    while True:
        show_table = input("  Show year-by-year breakdown? (y/n): ").strip().lower()
        if show_table == "y":
            calc.print_yearly_breakdown()
            break
        elif show_table == "n":
            break
        else:
            print("  ⚠  Not a valid response. Please enter 'y' or 'n'.")

    # Optional: re-run with a different rate using the same calc instance
    while True:
        another = input("  Try a different annual return rate? (y/n): ").strip().lower()
        if another == "y":
            new_rate = get_annual_rate("  📈 New annual return (%): ")
            calc.update_rate(new_rate)
            calc.print_summary()
        elif another == "n":
            break
        else:
            print("  ⚠  Not a valid response. Please enter 'y' or 'n'.")

    print("  ✅ Good luck with your savings journey!\n")
