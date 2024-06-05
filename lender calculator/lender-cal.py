
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




def private_lender(type):

    if type=='first': 
        recommendation = lender_name + num
        #check first residential loan nums
        return recommendation
    elif type=='second':
        #check second residential loan numbers 
        recommendation= lender_name + num
        return recommendation
    elif type=='HELOC': 
        #check HELOC loan numbers 
        return recommendation
        

def commercial_lender(type): 

    if type=='first': 
        recommendation = lender_name + num
        #check first residential loan nums
        return recommendation
    
    elif type=='second':
        #check second residential loan numbers 
        recommendation= lender_name + num
        return recommendation

    elif type=='Construction': 
        #check HELOC loan numbers 
        return recommendation




#call this function when they click the calculate button 
def calculate(loan_type):
    match loan_type:
        case 'private':

            return private_lender(residential_type)
        case 'commercial':

            return commercial_lender(commercial_type)

                


