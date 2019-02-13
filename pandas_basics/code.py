# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include='object')
print (categorical_var)
numerical_var = bank.select_dtypes(include='number')
print (numerical_var)

# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'], axis=1)
print (banks.isnull().sum())

bank_mode = banks.mode()
print (bank_mode)

banks['Gender'].fillna(bank_mode['Gender'][0],inplace=True)
banks['Married'].fillna(bank_mode['Married'][0],inplace=True)
banks['Dependents'].fillna(bank_mode['Dependents'][0],inplace=True)
banks['Self_Employed'].fillna(bank_mode['Self_Employed'][0],inplace=True)
banks['LoanAmount'].fillna(bank_mode['LoanAmount'][0],inplace=True)
banks['Loan_Amount_Term'].fillna(bank_mode['Loan_Amount_Term'][0],inplace=True)
banks['Credit_History'].fillna(bank_mode['Credit_History'][0],inplace=True)
print (banks.isnull().sum())
#code ends here



# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],
                    values='LoanAmount')
#print (avg_loan_amount)


# code ends here



# --------------
# code starts here
loan_approved_se = len(banks[(banks['Self_Employed'] == 'Yes') & 
                        (banks['Loan_Status']== 'Y')])
loan_approved_nse = len(banks[(banks['Self_Employed'] == 'No') & 
                        (banks['Loan_Status']== 'Y')])
Loan_Status = 614
#print (loan_approved_se)
#print (loan_approved_nse)
percentage_se = (loan_approved_se/Loan_Status) * 100
percentage_nse = (loan_approved_nse/Loan_Status) * 100
#print (percentage_se)
#print (percentage_nse)
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x//12)
big_loan_term = len(loan_term[loan_term >= 25])
#print (big_loan_term)



# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]
#print (loan_groupby)
mean_values = loan_groupby.mean()
#print (mean_values)




# code ends here


