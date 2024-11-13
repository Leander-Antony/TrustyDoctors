import requests
from bs4 import BeautifulSoup
import csv

def extract_doctor_info(url):
    
    response = requests.get(url)
    
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        
        doctor_blocks = soup.find_all('div', class_='dr-dscpn')

        
        doctors_info = []

        
        for block in doctor_blocks:
           
            name = block.find('h3', class_='cursor-pointer').get_text(strip=True)

            
            spec_group = block.find('div', class_='spec-group')
            if spec_group:
                specialization = spec_group.find('p').get_text(strip=True).split('|')[0].strip()
                experience = spec_group.find('p').get_text(strip=True).split('|')[1].strip()
            else:
                specialization = "Not found"
                experience = "Not found"

            
            doctors_info.append({
                'Name': name,
                'Specialization': specialization,
                'Experience': experience
            })

        return doctors_info
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def save_to_csv(doctors_info, filename='doctors_info.csv'):
    
    fieldnames = ['Name', 'Specialization', 'Experience']

    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        
        writer.writeheader()

       
        for doctor in doctors_info:
            writer.writerow(doctor)

    print(f"Data successfully saved to {filename}")


url = 'https://www.askapollo.com/physical-appointment?page=1'  


doctors_info = extract_doctor_info(url)


if doctors_info:
    save_to_csv(doctors_info)
