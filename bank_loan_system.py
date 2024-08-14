import random

class Customer:
    def __init__(self, name, age, income, credit_score):
        self.name = name
        self.age = age
        self.income = income
        self.credit_score = credit_score

class LoanApplication:
    def __init__(self, customer, loan_amount, loan_term):
        self.customer = customer
        self.loan_amount = loan_amount
        self.loan_term = loan_term
        self.approved = False
        self.interest_rate = None

class Bank:
    def __init__(self, name):
        self.name = name
        self.applications = []

    def apply_for_loan(self, customer, loan_amount, loan_term):
        application = LoanApplication(customer, loan_amount, loan_term)
        self.applications.append(application)
        return application

    def process_applications(self):
        for app in self.applications:
            self._evaluate_application(app)

    def _evaluate_application(self, application):
        customer = application.customer
        score = 0
        print(f"\nEvaluating application for {customer.name}:")

        # Age score
        if 25 <= customer.age <= 60:
            score += 20
            print(f"Age score: +20 (Age: {customer.age})")
        else:
            print(f"Age score: +0 (Age: {customer.age})")

        # Income score
        income_score = min(customer.income // 10000, 30)
        score += income_score
        print(f"Income score: +{income_score} (Income: R{customer.income})")

        # Credit score
        if customer.credit_score >= 700:
            score += 30
            print(f"Credit score: +30 (Score: {customer.credit_score})")
        elif customer.credit_score >= 600:
            score += 20
            print(f"Credit score: +20 (Score: {customer.credit_score})")
        elif customer.credit_score >= 500:
            score += 10
            print(f"Credit score: +10 (Score: {customer.credit_score})")
        else:
            print(f"Credit score: +0 (Score: {customer.credit_score})")

        # Loan amount vs income
        if application.loan_amount <= customer.income * 2:
            score += 20
            print(f"Loan amount score: +20 (Loan: R{application.loan_amount}, Income: R{customer.income})")
        elif application.loan_amount <= customer.income * 3:
            score += 10
            print(f"Loan amount score: +10 (Loan: R{application.loan_amount}, Income: R{customer.income})")
        else:
            print(f"Loan amount score: +0 (Loan: R{application.loan_amount}, Income: R{customer.income})")

        print(f"Total score: {score}")

        # Approve if score is 60 or higher (lowered from 70)
        if score >= 60:
            application.approved = True
            application.interest_rate = 5 + random.uniform(0, 5)
            print("Application APPROVED")
        else:
            print("Application DENIED")

# Example usage
if __name__ == "__main__":
    bank = Bank("Frazer Bank")
    print(f"Welcome to {bank.name}!")
    print("Processing loan applications...\n")

    # Create some customers
    customer1 = Customer("Alice", 30, 60000, 720)
    customer2 = Customer("Bob", 45, 80000, 650)
    customer3 = Customer("Charlie", 22, 30000, 600)

    # Apply for loans
    app1 = bank.apply_for_loan(customer1, 150000, 30)
    app2 = bank.apply_for_loan(customer2, 200000, 15)
    app3 = bank.apply_for_loan(customer3, 50000, 10)

    # Process applications
    bank.process_applications()

    # Print results
    print("\nFinal Results:")
    for i, app in enumerate(bank.applications, 1):
        print(f"\nApplication {i}:")
        print(f"Customer: {app.customer.name}")
        print(f"Age: {app.customer.age}")
        print(f"Income: R{app.customer.income}")
        print(f"Credit Score: {app.customer.credit_score}")
        print(f"Loan Amount: R{app.loan_amount}")
        print(f"Loan Term: {app.loan_term} years")
        print(f"Approved: {app.approved}")
        if app.approved:
            print(f"Interest Rate: {app.interest_rate:.2f}%")

    print("\nAll applications processed.")