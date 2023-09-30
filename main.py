import requests
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import csv



BASE_URL = "https://www.ratemyprofessors.com"


def extract_professor_count(content):
    match = re.search(r'"resultCount":(\d+)', content)
    if match:
        count = match.group(1)
        return f"{count} professors at Vanderbilt University"
    return None


def search_and_print_header():
    search_url = f"{BASE_URL}/search/professors/4002?q=*"
    response = requests.get(search_url)

    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return

    header_info = extract_professor_count(response.text)
    if header_info:
        print(header_info)
    else:
        print("Header information not found.")


def save_to_csv(professors):
    with open('professors.csv', mode = 'w', newline = '') as file:
        writer = csv.writer(file)

        writer.writerow(['Name','Rating','Rating Count','Department','Would Take Again %'])
        writer.writerows(professors)
        print("Saved to CSV")

def extract_professor_data(soup):
    professor_elements = soup.find_all(class_="TeacherCard__StyledTeacherCard-syjs0d-0")
    
    professors = []
    for element in professor_elements:
        name = element.find(class_="CardName__StyledCardName-sc-1gyrgim-0")
        rating = element.find(class_="CardNumRating__CardNumRatingNumber-sc-17t4b9u-2")
        ratings_count = element.find(class_ = "CardNumRating__CardNumRatingCount-sc-17t4b9u-3")
        department = element.find(class_="CardSchool__Department-sc-19lmz2k-0")
        would_take_again = element.find(class_="CardFeedback__CardFeedbackNumber-lq6nix-2")

        if name and rating and department and would_take_again and ratings_count:
            name = name.get_text(strip=True)
            rating = rating.get_text(strip=True)
            ratings_count = ratings_count.get_text(strip=True)
            department = department.get_text(strip=True)
            would_take_again = would_take_again.get_text(strip=True)
            # print(f"Name: {name}, Rating: {rating} Count: {ratings_count} , Department: {department}, Would take again %: {would_take_again}")
            professors.append((name, rating, ratings_count, department, would_take_again))
    save_to_csv(professors)





def scrape_professors():
    options = webdriver.ChromeOptions()

    prefs = {
        "profile.managed_default_content_settings.images": 2,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.ads": 2,
        "profile.managed_default_content_settings.stylesheet": 2,
        "profile.managed_default_content_settings.cookies": 2,
        "profile.managed_default_content_settings.javascript": 1,
        "profile.managed_default_content_settings.plugins": 1,
        "profile.managed_default_content_settings.popups": 2,
        "profile.managed_default_content_settings.geolocation": 2,
        "profile.managed_default_content_settings.media_stream": 2,
    }

    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)
    url = f"{BASE_URL}/search/professors/4002?q=*"
    driver.get(url)
    wait = WebDriverWait(driver, 2)
    try:
        ## Close the cookie modal on start
        close_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".CCPAModal__StyledCloseButton-sc-10x9kq-2")))
        close_button.click()
        print("Cookie modal closed")
    except Exception as e:
        print(
            f"Could not find Close button, or another error occurred: {str(e)}")
    i = 0
    sleep_time = 1
    while True:
        try:
            ## Press the show more button to load more professors
            show_more_button = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//button[text()='Show More']")))
            show_more_button.click()
            i += 1
            print(f'Pressed {i} times')
            if i % 100 == 0:
                sleep_time += 1
            # if i % 250 == 0:
            #     sleep_time += 1 
            time.sleep(sleep_time)

            
        except Exception as e:
            print("No more 'Show More' buttons, or another error occurred.")
            break

    soup = BeautifulSoup(driver.page_source, "html.parser")
    extract_professor_data(soup)
    driver.quit()

if __name__ == "__main__":
    search_and_print_header()
    scrape_professors()
