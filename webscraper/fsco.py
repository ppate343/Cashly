import requests
from bs4 import BeautifulSoup
import csv


# Function to scrape data from the license page
def scrape_license_page(license_number):
    url = f"https://mbsweblist.fsco.gov.on.ca/ShowLicence.aspx?{license_number}~"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')


        #add errorchecking for data (if does not exists, append empty string)
        # Extracting data from the html of the table

        if (soup.find("span", id="MainPlaceHolder_Content4_cragbkrname") != None):

            if(soup.find("span", id="MainPlaceHolder_Content4_crstatus").text.strip() != 'Expired'):

                agent_name = soup.find("span", id="MainPlaceHolder_Content4_cragbkrname").text.strip()
                license_number = soup.find("span", id="MainPlaceHolder_Content4_craglicence").text.strip()
                brokerage_name = soup.find("span", id="MainPlaceHolder_Content4_crbkrgname").text.strip()
                license_class = soup.find("span", id="MainPlaceHolder_Content4_crlicclass").text.strip()
                status = soup.find("span", id="MainPlaceHolder_Content4_crstatus").text.strip()
                issue_date_str = soup.find("span", id="MainPlaceHolder_Content4_crissuedate").text.strip()
                expiry_date_str = soup.find("span", id="MainPlaceHolder_Content4_cragexpiry").text.strip()

                print(agent_name + ' : ' , status )
        
        
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
    year = 'M22001'
    num = '001'
   # initial_license_number = "M24000001"
    entries = 200
    

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
            data_list.append(license_data)
        else:
            print(f"Skipping license number {new_license_number}.")

    
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
