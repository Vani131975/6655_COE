import streamlit as st

class Bank:
    def __init__(self):
        if 'acc_balance' not in st.session_state:
            st.session_state.acc_balance = 1000
        if 'attempt_count' not in st.session_state:
            st.session_state.attempt_count = 0

    def validate(self):
        if st.session_state.attempt_count >= 3:
            st.error("Maximum attempts reached card blocked")
            return
        st.title("ABC Bank")
        if 'pin_verified' not in st.session_state or not st.session_state.pin_verified:
            pin = st.text_input("Enter your PIN", type="password")

            if st.button("Submit PIN"):
                if pin == "1234":
                    st.session_state.pin_verified = True
                    self.viewOptions()
                else:
                    st.session_state.attempt_count += 1
                    st.error(f"Invalid PIN. Attempt {st.session_state.attempt_count} of 3")
        else:
            self.viewOptions()

    def viewOptions(self):
        deposit_amount = st.number_input("Enter the deposit amount:", min_value=100, max_value=50000, step=100)
        if st.button("deposit amount"):
            if 100 <= deposit_amount <= 50000:
                st.session_state.acc_balance += deposit_amount
                st.success(f'Amount Deposited successfully. The account balance is {st.session_state.acc_balance}')
            else:
                st.error("Deposit amount must be between 100 and 50000 and a multiple of 100.")

        withdraw_amount = st.number_input("Enter the withdraw amount:", min_value=100, max_value=20000, step=100)
        if st.button("Withdraw amount"):
            if 100 <= withdraw_amount <= 20000 and withdraw_amount % 100 == 0:
                if withdraw_amount <= st.session_state.acc_balance and st.session_state.acc_balance >= 500:
                    st.session_state.acc_balance -= withdraw_amount
                    st.success(f'The account balance after withdrawal is {st.session_state.acc_balance}')
                else:
                    st.error("Insufficient balance or withdrawal amount exceeds limit.")
            else:
                st.error("Withdrawal amount must be a multiple of 100 and between 100 and 20k")

        if st.button("Show Balance"):
            st.success(f'Your current balance is {st.session_state.acc_balance}')

        if st.button("Exit"):
            st.session_state.pin_verified = False
            st.info("Exiting..")

obj = Bank()
obj.validate()
