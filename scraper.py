from  colorama import init, Fore, Style
#from tabula import tabulate
from html_test import all_scholarships, loading_bar_animation,web_find
#from web_scrape import web_find
import requests
from bs4 import BeautifulSoup
import time
import bs4

 
    
def extract_eligibility(page_url):
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
    response = requests.get(page_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        eligibility_heading = soup.find('strong', string='Eligibility:')
        if eligibility_heading:
            eligibility_paragraph = eligibility_heading.find_next('p')
            eligibility_text = eligibility_paragraph.get_text(strip=True)
            return eligibility_text
        else:
            return "Eligibility information not found."
    else:
        return "Page request failed."
    
init(autoreset=True)

# user interface 

proceed ='yes'
while proceed == "yes":
        
    print(Style.BRIGHT + Fore.RED + "       Scholarship Search Tool")
    print("1.Available Degrees")
    print("2.Seach for scholarship")
    print("3.Up coming IT events")
    print("4.Exit program")
    
    user_input = int(input("Enter your choice: "))
    
    if user_input == 1:
        loading_bar_animation()
        all_scholarships()
    if user_input == 2:
        print(Style.BRIGHT + Fore.BLUE +"OPTIONS")
        print("1.Undergraduate degree")
        print("1. Master's degrees")
        print("1. PhD degrees")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            degree_type = "Undergraduate"
            web_find(degree_type)
            
        elif choice == 2: 
            degree_type = "Masters Degree"
            web_find(degree_type)
        elif choice == 3:
            degree_type = "PhD"
            web_find(degree_type)
            
            
            
    elif user_input == 4:
        exit()
                    
           
           
    #     if choice == 2:
    #          headers = ["Scholarship Name", "University", "Degree Type","Location","Deadline","Eligibility"]  

    #         table = tabulate (, headers,tablefmt ="grid")
    #         print(tabulate(scholarship_list, headers   ))  
    # if proceed !="yes":
        
    #     break