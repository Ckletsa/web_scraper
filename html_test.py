import requests
from bs4 import BeautifulSoup
import time
import bs4

   
def loading_bar_animation():
    from  colorama import init, Fore, Style
    import sys
    import time
    import colorama
    total_progress = 100  # Total progress value (e.g., 100%)
    bar_width = 50  # Width of the loading bar in characters

    for progress in range(total_progress + 1):
        completed_width = bar_width * progress // total_progress

        sys.stdout.write("\r[")
        for i in range(bar_width):
            if i < completed_width:
                sys.stdout.write(Style.BRIGHT + Fore.GREEN +"=")
            else:
                sys.stdout.write(" ")
        sys.stdout.write("] {}%".format(progress))
        sys.stdout.flush()

        # Add a small delay to control the speed of the animation
        time.sleep(0.005)

    print()  # Move to the next line after the loading bar is complete

def all_scholarships():   
    from lxml import html
    import requests

    start_page = 1
    end_page = 10
    start_point = 1
    end_point = 9

    for page_number in range(start_page, end_page+1):
        page_number + 1
        # Send an HTTP GET request
        url = f'https://www.scholars4dev.com/page/{page_number}/'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            tree = html.fromstring(response.content)
            # Define the XPath expression to select the elements you want on the page
            # Modify this expression based on the actual structure of the page
            if page_number == 1:
                xpath_expression ="/html/body/div[3]/div[1]/div[1]/div[2]/div/div[1]/div[1]"
                elements = tree.xpath(xpath_expression)
                
                if elements:
                    # Loop through the selected elements
                    for element in elements:
                        content = element.text_content().strip()
                        # Print the extracted content for each element
                        print(content)
                        
                       
                
            else:
                for number in range(start_point, end_point+1):
                    xpath_expression = f'/html/body/div[3]/div[1]/div[1]/div/div/div[{number}]/div[1]'
                    
                    elements = tree.xpath(xpath_expression)
                    
                    if elements:
                        # Loop through the selected elements
                        for element in elements:
                            content = element.text_content().strip()
                            # Print the extracted content for each element
                            print(content)
                            
                   
                        
                        
                else:
                    print(f"No matching elements found on page {page_number}")
        else:
            print(f"Failed to retrieve page {page_number}. Status code: {response.status_code}")



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
    
    








def web_find(degree_type):
    web_dictionary = {}
    #zweb_list = []
    websites = ["https://www.scholars4dev.com/",
       "https://www.scholars4dev.com/page/2/",
       "https://www.scholars4dev.com/page/3/",
       "https://www.scholars4dev.com/page/4/",
       "https://www.scholars4dev.com/page/5/",
       "https://www.scholars4dev.com/page/6/",
       "https://www.scholars4dev.com/page/7/",
       "https://www.scholars4dev.com/page/8/",
       "https://www.scholars4dev.com/page/9/",
       "https://www.scholars4dev.com/page/10/",
       "https://www.scholars4dev.com/page/11/",
       ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    for url in websites:
      
    # Send an HTTP GET request to the scholarship page
        response = requests.get(url, headers=headers)

    # Retry up to 3 times if the request fails
        # retry_count = 0
        # while retry_count < 3:
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(soup)

            # Extract scholarship details (adjust based on page structure)
            scholarship_list = soup.find_all('div', class_='entry clearfix')
           

            if not scholarship_list:
                print("No scholarships found.")
                break
            else:
                
                for scholarship in scholarship_list:
                    scholarship_name = scholarship.find('h2').text
                    university = scholarship.find('em').text
                    
                    

                    # Check if the element exists before trying to access it
                    

                    deadline_element = scholarship.find('strong', string='Deadline:')
                    if deadline_element:
                        deadline = deadline_element.next_sibling 
                    # else:
                    #     deadline = "Not specified"

                    location_element = scholarship.find('strong', string="Deadline:")
                    if location_element:
                        location1 = location_element.next_sibling
                        location2 = location1.next_sibling
                        location = location2.next_sibling
                        
                        
                    # else:
                    #     print("Not specified")
                        

                    date_element = scholarship.find('strong', string="Deadline:")
                    
                    if date_element:
                        date1 = date_element.next_sibling
                        date2 = date1.next_sibling
                        date3 = date2.next_sibling
                        date4= date3.next_sibling
                        date = date4.next_sibling
                        
                    embedded_page_url = scholarship.find('a')['href']  # Get the embedded scholarship page URL
                    eligibility = extract_eligibility(embedded_page_url)
                    
                    degree_tag = scholarship.find("em")
                    
                    
                    if degree_tag:
                        degree = str(degree_tag.next_sibling)
                        # print("degree: ",degree)
                        # print(type(degree))
                        # print("degree_type: ",degree_type)
                        # print(type(degree_type))
                        
                        if degree_type in degree:
                            web_list = [scholarship_name,university,deadline,location,eligibility,date]
                            print(web_list)
                            
                        else:
                            print("not found")

                        # if  degree == degree_type:
                        #     print (degree)
                        #     print(degree_tag)
                            
                        
                        # else:
                        #     print("Tool")        
                    
# key ="Masters/PhD Degrees"

# web_find(key, extract_eligibility)