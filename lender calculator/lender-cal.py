
#check private or commercial 
#for private #check residential 1st , 2nd or HELOC 
#check LTV first 
#if FICO is unknown -> check LTV 
#if FICO exists -> filter for fico, then check LTV
 
#LTV options -> 50, 55, 60, 65, 70, 75, 80, 85
#FICO options -> <550, 550 - 600, 600 - 650, 650-680, >680

#display options: Lender name, interest rate, fee



#fill these values with drop down menu in cashly

#private lender variables: loan_type, residential type 
loan_type = 'private'
residential_type = 'first'
appraisal_amount= 100,000
#commercial lender variables 
commercial_type = 'first'
fico = 580
ltv = 0.80
lender_name = 'extend'
num = 13


#call this function when they click the calculate button 
def calculate(loan_type):
    if loan_type=='private':
        return private_lender(residential_type, fico, ltv, appraisal_amount)
    elif loan_type=='commercial': 
        return commercial_lender(commercial_type, fico, ltv, appraisal_amount )
        


#function to calculate private lender suggestion 
def private_lender(type, fico, ltv): 
    match type: 
        case 'first': 
            #locate rows in df that in column 'LENDER NAME', 'LTV', 'FICO; 'Residential_first_Interest', Residential_first_fee
            #check LTV first (most important), filter rows that have ltv == to specific num (not a range) ,there are a couple outliers -> OZ capital (70% refi) , Regiis MIC (80% w/ fees)
            #check for FICO, filter rows by column 'FICO' , return rows in df that have a fico == range or do value (?? fix datasheet )
            #create new df with filterd columns & rows: lender name, residential_first_interest, residential_lender_fee, mortgage amount (this column is created by multiplying appraisal amount by ltv%)
            #add new column that shows approx. monthly mortgage payments which is created by (interest rate * mortgage amount)/ 12.
            # new column in df mortgage amount = (appraisal val * ltv %) 
            #return df with columns: Lender Name, LTV, FICO, Residential_first_interest, Residential_lender_fee, Approx Mortgage Recievable, Approx Monthly Payments 
            return 'recommendation'
        case 'second': 
            #locate rows in df that in column 'LENDER NAME', 'LTV', 'FICO; 'Residential_Second_Interest', Residential_Second_fee
            #mortgage amount = (appraisal val * ltv % ) - existing mortgage
            return 'print(df_recommendation)'
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


                


