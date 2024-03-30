import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from fpdf import FPDF

# Function to generate PDF from user data
def generate_pdf(user_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"CV for {user_data['name']}", ln=True, align='C')
    # Add more user data to PDF
    pdf.output("generated_cv.pdf")

# Function to log into Canva and generate CV
def generate_cv(email, password, user_data):
    # Initialize Selenium WebDriver
    service = Service('path/to/chromedriver')  # Set the path to your ChromeDriver executable
    driver = webdriver.Chrome(service=service)

    # Open Canva login page
    driver.get("https://www.canva.com/login")
    time.sleep(2)

    # Fill in login details and submit
    driver.find_element_by_id("login-email-input").send_keys(email)
    driver.find_element_by_id("login-password-input").send_keys(password)
    driver.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(5)  # Wait for login process

    # Navigate to CV templates page (example URL)
    driver.get("https://www.canva.com/templates/resumes/")
    time.sleep(5)

    # Get all available CV templates
    templates = driver.find_elements_by_css_selector(".js-search-media-item")
    num_templates = len(templates)

    # Randomly select a CV template
    random_template = random.randint(0, num_templates - 1)
    templates[random_template].click()
    time.sleep(3)

    # Fill in basic input fields (example)
    driver.find_element_by_id("input-field-name").send_keys(user_data['name'])
    driver.find_element_by_id("input-field-email").send_keys(user_data['email'])

    # Generate CV button click (example)
    driver.find_element_by_css_selector(".design-menu .design-menu-primary-button").click()
    time.sleep(10)  # Wait for CV generation

    # Close the driver and generate PDF from user data
    driver.quit()
    generate_pdf(user_data)

if __name__ == "__main__":
    # Example usage
    email = "sipho@jikelastudios.org"
    password = "Jikela Studios 2023"

    # Customize user data with required input fields
    user_data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'experience': [
            {'position': 'Senior Developer', 'years': 5},
            {'position': 'Project Manager', 'years': 3}
        ],
        'skills': ['Python', 'JavaScript', 'Project Management', 'Database Management']
    }

    generate_cv(email, password, user_data)
