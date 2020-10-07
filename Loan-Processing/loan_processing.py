# This program contains functions for processing a loan
import Meta_Data


def process_loan():
# Get customer information
    cust_name = input("Enter customer name: ")
    req_loan = int(input("Enter requested loan amount (<= $30,000): "))
    credit_score = int(input("Enter credit score (<400 pts): "))
# Look up meta data based on customer information
    for criteria_dict in Meta_Data.metadata():
        if req_loan <= criteria_dict["loan"] and criteria_dict["cs_start"] <= credit_score <= criteria_dict["cs_end"]:
            print(f'Approved loan = ${criteria_dict["loan"]}\nInterest rate = {criteria_dict["interest_rate"]}%\nLoan Duration = {criteria_dict["duration"]} months')
            break
    else:
        print("Loan not approved")











