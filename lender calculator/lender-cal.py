
#check private or commercial 
#for private #check residential 1st , 2nd or HELOC 
#if FICO is unknown -> check LTV 
#if FICO exists -> filter for fico, then check LTV
 
#LTV options -> 50, 55, 60, 65, 70, 75, 80, 85
#FICO options -> <550, 550 - 600, 600 - 650, 650-680, >680

#display options: Lender name, interest rate, fee



#fill these values with drop down menu in cashly
loan_type = 'private'
residential_type = 'first'
commercial_type = 'first'
fico = 580
ltv = 0.80
lender_name = 'extend'
num = 13


#call this function when they click the calculate button 
def calculate(loan_type):
    match loan_type:
        case 'private':

            return private_lender(residential_type)
        case 'commercial':

            return commercial_lender(commercial_type)
        


#function to calculate private lender suggestion 
def private_lender(type): 
    match type: 
        case 'first': 
            return 'recommendation'
        case 'second': 
            return 'recommendation'
        case 'HELOC': 
            return 'recommendation'

        
#function to calculate commercial lender suggestion 
def commercial_lender(type): 
    match type: 
        case 'first': 
            return 'recommendation'
        case 'second': 
            return 'recommendation'
        case 'construction': 
            return 'recommendation'
        


#function to filter for credit score then LTV


def calculate(type, fico, ltv, area):
    #check if commercial or private 
    #check fico greater than or ltv greater than etc..
    # area where?
    #print results 
    return 'lender name, interest rate, fee' 


                


