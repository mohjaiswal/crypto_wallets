# Cryptocurrency Wallet

################################################################################
# Assume the perspective of a KryptoJobs2Go customer in order to do the following:

# * Generate a new Ethereum account instance by using mnemonic seed phrase.

# * Fetch and display the account balance associated with the Ethereum account address.

# * Calculate the total value of an Ethereum transaction, including the gas estimate, that pays a KryptoJobs2Go candidate for their work.

# * Digitally sign a transaction that pays a KryptoJobs2Go candidate, and send this transaction to the Ganache blockchain.

# * Review the transaction hash code associated with the validated blockchain transaction.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
################################################################################
# Step 1:
# Import Ethereum Transaction Functions into the KryptoJobs2Go Application

# In this section, import several functions from the `crypto_wallet.py` script into the file `krypto_jobs.py`, which contains code for Fintech
# Finder’s customer interface, in order to add wallet operations to the application. For this section, will assume the perspective of a Fintech Finder customer 
# (i.e., provide  Ethereum wallet and account information to the application).

# Complete the following steps:

# 1. Review the code contained in the `crypto_wallet.py` script file. Note that the Ethereum transaction functions built - `wallet`, `wallet.derive_acount`, 
# `get_balance`, `fromWei`, `estimateGas`, `sendRawTransaction` have been incorporated into Python functions that allow to automate the process of accessing them.

# 2. Add the mnemonic seed phrase (provided by Ganache) to the starter code’s `ut.env` file.

# 3. Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

# 4. Within the Streamlit sidebar section of code, create a variable named `account`. Set this variable equal to a call on the `generate_account` function.
# This function will create the KryptoJobs2Go customer’s HD wallet and Ethereum account.

# 5. Within this same section of the `krypto_jobs.py` file, define a new `st.sidebar.write` function that will display the balance of the customer’s account. 
# Inside this function, call the `get_balance` function and pass the Ethereum `account.address`.

################################################################################
# Step 1 - Part 3:
# Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

# From `crypto_wallet.py import the functions generate_account, get_balance, and send_transaction
from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################
# KryptoJobs2Go Candidate Information

# Database of KryptoJobs2Go candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": [
        "Lane",
        "0xE0Dd9dAE24Cc731CaA68f34eDC74db6CDEbaDDA5",
        "4.3",
        0.20,
        "Images/lane.jpeg",
    ],
    "Ash": [
        "Ash",
        "0xb894f4F29DEe6a876D66839e5dC90781684a74CE",
        "5.0",
        0.33,
        "Images/ash.jpeg",
    ],
    "Jo": [
        "Jo",
        "0x07C595B808cD5899D24Db699B43f5D9ca9B245eC",
        "4.7",
        0.19,
        "Images/jo.jpeg",
    ],
    "Kendall": [
        "Kendall",
        "0x89e69E44bE75088F8FAabEb6ecA8302131A50EE9",
        "4.1",
        0.16,
        "Images/kendall.jpeg",
    ],
}

# A list of the KryptoJobs2Go candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]


def get_people():
    """Display the database of KryptoJobs2Go candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("KryptoJobs2Go Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")


################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# KryptoJobs2Go!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the `generate_account` function. This function will create the KryptoJobs2Go 
# customer’s HD wallet and Ethereum account.

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Step 1 - Part 5:
# Define a new `st.sidebar.write` function that will display the balance of the customer’s account. Inside this function, call the `get_balance` function 
# and pass the Ethereum `account.address`.

# Call `get_balance` function and pass it the Ganache server address and customer account address
# Write the returned ether balance to the sidebar
ether = get_balance(w3, account.address)

# Disply the balance of ether in the account
st.sidebar.markdown("## KryptoJobs2Go Balance of Ether")
st.sidebar.markdown(ether)
st.sidebar.markdown("---------")


##########################################

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox("Select a Person", people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the KryptoJobs2Go candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the KryptoJobs2Go candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the KryptoJobs2Go candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the KryptoJobs2Go candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

################################################################################
# Step 2: Sign and Execute a Payment Transaction

# Complete the following steps:

# 1. KryptoJobs2Go customers will select a fintech professional from the application interface’s drop-down menu, and then input the amount of time for 
# which they’ll hire the worker. 
# Code the application so that once a customer completes these steps, the application will calculate the amount that the worker will be paid in ether. 
# To do so, complete the following steps:

# * Write the equation that calculates the candidate’s wage. This equation should assess the candidate’s hourly rate from the candidate database 
# (`candidate_database[person][3]`) 
# and then multiply this hourly rate by the value of the `hours` variable. Save this calculation’s output as a variable named `wage`.

# * Write the `wage` variable to the Streamlit sidebar by using `st.sidebar.write`.

# 2. Now that the application can calculate a candidate’s wage, write the code that will allow the KryptoJobs2Go as the customer to send an Ethereum 
# blockchain transaction that pays the hired candidate.
# To accomplish this, locate the code that reads `if st.sidebar.button("Send Transaction")`. 
# Add logic to this `if` statement that sends the appropriate information to the `send_transaction` function (which is imported from the `crypto_wallet` script file).
# Inside the `if` statement, add the following functionality:

# * Call the `send_transaction()` function and pass it three parameters:
# - The Ethereum `account` information. (Remember that this `account` instance was created when the `generate_account` function was called.)
#  From the `account` instance, the application will be able to access the `account.address` information that is needed to populate the `from` data attribute 
# in the raw transaction.
# - The `candidate_address` (which will be created and identified in the sidebar when a customer selects a candidate). This will populate the `to` data attribute 
# in the raw transaction.
# - The `wage` value. This will be passed to the `toWei` function to determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns as a variable named `transaction_hash`, and have it display on the application’s web interface.

##########################################
# Step 2 - Part 1:
# * Write the equation that calculates the candidate’s wage. This equation should assess the candidate’s hourly rate from the candidate database 
# (`candidate_database[person][3]`) and 
# then multiply this hourly rate by the value of the `hours` variable. Save this calculation’s output as a variable named `wage`.
# * Write the `wage` variable to the Streamlit sidebar by using `st.sidebar.write`.

# Calculate total `wage` for the candidate by multiplying the candidate’s hourly rate from the candidate database (`candidate_database[person][3]`) by the value of
# the `hours` variable 
wage = candidate_database[person][3] * hours

# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(wage)

##########################################
# Step 2 - Part 2:
# * Call the `send_transaction` function and pass it three parameters: 
# - The Ethereum `account` information. (Remember that this `account` instance was created when the `generate_account` function was called.)
#  From the `account` instance, the application will be able to access the `account.address` information that is needed to populate the `from` data attribute 
#  in the raw transaction.
# - The `candidate_address` (which will be created and identified in the sidebar when a customer selects a candidate). This will populate the `to` data attribute 
# in the raw transaction.
# - The `wage` value. This will be passed to the `toWei` function to determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns as a variable named `transaction_hash`, and have it display on the application’s web interface.


if st.sidebar.button("Send Transaction"):

    # Call the `send_transaction` function and pass 4 parameters:
    # Ganache server address, `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`    
    transaction_hash = send_transaction(w3, account, candidate_address, wage)
    
    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate the successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes KryptoJobs2Go candidates to the Streamlit page
get_people()

################################################################################
# Step 3: Inspect the Transaction

# Send a test transaction by using the application’s web interface, and then look up the resulting transaction hash in Ganache.