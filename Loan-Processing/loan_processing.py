# This program contains functions for processing a loan
import Meta_Data
loan_criteria = Meta_Data.metadata()


# INPUT
cust_name = input("Enter customer name: ")
req_loan = int(input("Enter requested loan amount: "))
credit_score = int(input("Enter credit score: "))


# Look up meta data based on customer info
for criteria_dict in loan_criteria:
    if req_loan <= criteria_dict["loan"] and criteria_dict["cs_start"] <= credit_score <= criteria_dict["cs_end"]:
        print(f'Approved loan = ${criteria_dict["loan"]}\nInterest rate = {criteria_dict["interest_rate"]}%\nLoan Duration = {criteria_dict["duration"]} months')
        break
else:
    print("Loan not approved")












