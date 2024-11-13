import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "https://www.kauveryhospital.com/centers-of-excellence-and-specialties/"


categories = [
    "anesthesiology",
    "critical-care",
    "dental",
    "dermatology",
    "ophthalmology",
    "endocrinology",
    "ent",
    "general-surgery",
    "laboratory-services",
    "obstetrics",
    "psychiatry",
    "pulmonology",
    "rheumatology",
    "lung-centre",
    "general-medicine",
    "diabetology",
    "orthopaedics",
    "spine-surgery",
    "gastroenterology",
    "liver-disease-transplantation-and-hepatobiliary-surgery",
    "geriatrics",
    "nephrology-and-urology-science",
    "vascular-surgery",
    "paediatrics-and-neonatology",
    "infectious-diseases",
    "plastic-surgery",
    "breast-clinic"
]

def scrape_doctors(category):
    url = f"{base_url}{category}/"
    response = requests.get(url)
 
    print(f"Fetching {url}... Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print(f"Failed to retrieve {url}. Skipping...")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    doctor_elements = soup.find_all('a', href=True)
    
    doctors_data = []

    for doctor in doctor_elements:
        
        doctor_name_tag = doctor.find('div', class_='doctorname')
        
        if doctor_name_tag:
            doctor_name = doctor_name_tag.get_text(strip=True)
            if doctor_name:  
                doctors_data.append([doctor_name, category.replace('-', ' ').title()])
    
    return doctors_data

def main():
    all_doctors = []

    
    for category in categories:
        print(f"Scraping doctors in {category}...")
        doctors_data = scrape_doctors(category)
        all_doctors.extend(doctors_data)
        time.sleep(1)  

    
    with open('doctors_info2.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Doctor Name", "Category"])
        writer.writerows(all_doctors)
    
    print("Scraping completed. Data saved to 'doctors_info.csv'.")

if __name__ == "__main__":
    main()
