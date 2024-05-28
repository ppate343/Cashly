import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from datetime import datetime
from openpyxl import Workbook

# Function to scrape data from the license page
def scrape_license_page(license_number):
    url = f"https://mbsweblist.fsco.gov.on.ca/ShowLicence.aspx?{license_number}~"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        if (license_number != None):

        #add errorchecking for data (if does not exists, append empty string)
        # Extracting data from the html of the table
            agent_name = soup.find("span", id="MainPlaceHolder_Content4_cragbkrname").text.strip()
            license_number = soup.find("span", id="MainPlaceHolder_Content4_craglicence").text.strip()
            brokerage_name = soup.find("span", id="MainPlaceHolder_Content4_crbkrgname").text.strip()
            license_class = soup.find("span", id="MainPlaceHolder_Content4_crlicclass").text.strip()
            status = soup.find("span", id="MainPlaceHolder_Content4_crstatus").text.strip()
            issue_date_str = soup.find("span", id="MainPlaceHolder_Content4_crissuedate").text.strip()
            expiry_date_str = soup.find("span", id="MainPlaceHolder_Content4_cragexpiry").text.strip()

            print(expiry_date_str)
        
        # converting to date // not need
        #issue_date = datetime.strptime(issue_date_str, "%B %d, %Y")
        #expiry_date = datetime.strptime(expiry_date_str, "%B %d, %Y")
        
            # Returning the data
            return {
                "Agent Name": agent_name,
                "License Number": license_number,
                "Brokerage": brokerage_name,
                "License Class": license_class,
                "Status": status,
                "Issue Date": issue_date_str,
                "Expiry Date": expiry_date_str
        }
    else:
        print(f"Failed to fetch data for license number {license_number}.")
        return None

# Function to check if license is valid (cleaned up in excel)
'''def is_valid_license(status, expiry_date):
    if status != "Expired" and expiry_date > datetime.now():
        return True
    return False'''

# Main function
def main():
    # initial license # + back numbers to incremement
    year = 'M24000'
    num = '001'
   # initial_license_number = "M24000001"
    entries = 300
    

    # ;ength of the numerical part of the license number
    num_length = len(num)

    # list to store data
    data_list = []


    
    for i in range(entries):
       # print(str(int(num)))
        
        # Incrementing the number and formatting it with leading zeros
        new_num = str(int(num) + i).zfill(num_length)
        new_license_number = year + new_num
        
        #print(new_license_number)
        # Scrape data from the license page
        license_data = scrape_license_page(new_license_number)
        
        #if there is data returned, append to list 
        if license_data:
            #print(license_data)
            # Check if license is valid
            #if is_valid_license(license_data["Status"], license_data["Expiry Date"]):
                # Append data to the list

            data_list.append(license_data)
        else:
            print(f"Skipping license number {new_license_number}.")
    
    # Create a DataFrame from the list
    #df = pd.DataFrame(data_list)
    
    # Save the DataFrame to an Excel file
    #df.to_excel("license_data.xlsx", index=False)
    
    #Creating csv file from list 
    with open('agents.csv', 'w', newline='', encoding='utf-8') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)

        #adding headers to csv file
        header = ["Agent Name", "License Number","Brokerage", "License Class","Status","Issue Date", "Expiry Date",]
        wr.writerow(header)

        #routing data to headers from returned data object
        for item in data_list: 
            name = item.get('Agent Name', 'N/A')
            license_num = item.get('License Number', 'N/A')
            brokerage = item.get("Brokerage", 'N/A')
            license_class = item.get('License Class', 'N/A')
            status = item.get('Status', 'N/A')
            issue_date = item.get('Issue Date', 'N/A')
            expiry_date = item.get('Expiry Date', 'N/A')
            wr.writerow([name, license_num, brokerage, license_class, status, issue_date, expiry_date])

# Call the main function
if __name__ == "__main__":
    main()
