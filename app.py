import streamlit as st

# Your BankApplication Class
class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return f"Transaction Successful. Collected {amount}"
        else:
            return "Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit Successful. Total Balance: {self.balance}"

    def update_mobile(self, new_number):
        self.mobile_number = new_number
        return f"Mobile number updated: {self.mobile_number}"

    def check_balance(self):
        return f"Total Account Balance: {self.balance}"


# Streamlit UI
st.title("🏦 SBI Bank Application")

# Session storage
if "account" not in st.session_state:
    st.session_state.account = None

menu = ["Create Account", "Deposit", "Withdraw", "Update Mobile", "Check Balance"]
choice = st.sidebar.selectbox("Select Option", menu)

# Create Account
if choice == "Create Account":
    st.header("Create New Account")

    name = st.text_input("Enter Name")
    account_number = st.text_input("Account Number")
    age = st.number_input("Age", min_value=18)
    mobile = st.text_input("Mobile Number")
    balance = st.number_input("Initial Balance", min_value=0)

    if st.button("Create Account"):
        st.session_state.account = BankApplication(name, account_number, age, mobile, balance)
        st.success("Account Created Successfully!")

# Deposit
elif choice == "Deposit":
    st.header("Deposit Money")

    if st.session_state.account:
        amount = st.number_input("Enter Amount")

        if st.button("Deposit"):
            result = st.session_state.account.deposit(amount)
            st.success(result)
    else:
        st.warning("Create an account first")

# Withdraw
elif choice == "Withdraw":
    st.header("Withdraw Money")

    if st.session_state.account:
        amount = st.number_input("Enter Amount")

        if st.button("Withdraw"):
            result = st.session_state.account.withdraw(amount)
            st.success(result)
    else:
        st.warning("Create an account first")

# Update Mobile
elif choice == "Update Mobile":
    st.header("Update Mobile Number")

    if st.session_state.account:
        new_mobile = st.text_input("New Mobile Number")

        if st.button("Update"):
            result = st.session_state.account.update_mobile(new_mobile)
            st.success(result)
    else:
        st.warning("Create an account first")

# Check Balance
elif choice == "Check Balance":
    st.header("Account Balance")

    if st.session_state.account:
        result = st.session_state.account.check_balance()
        st.info(result)
    else:
        st.warning("Create an account first")