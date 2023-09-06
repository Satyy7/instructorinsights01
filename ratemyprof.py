import requests
import re
import json

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


def extract_professor_data(content):
    # Try to capture everything between window.__RELAY_STORE__ = and the closing </script> tag
    match = re.search(
        r'window\.__RELAY_STORE__ = (.*?);\s*</script>', content, re.DOTALL)
    if not match:
        return []

    data_str = match.group(1)

    try:
        data = json.loads(data_str)
    except json.JSONDecodeError as e:
        # Trim the data string at the position where the parsing failed and retry
        trimmed_data_str = data_str[:e.pos]
        try:
            data = json.loads(trimmed_data_str)
        except json.JSONDecodeError:
            print("Failed to parse trimmed JSON data.")
            return []

    professors = []
    for key, value in data.items():
        if "firstName" in value and "lastName" in value:
            first_name = value["firstName"]
            last_name = value["lastName"]
            avg_rating = value.get("avgRating", "N/A")
            print(f"Name: {first_name} {last_name}, Rating: {avg_rating}")

            professors.append((first_name, last_name, avg_rating))

    return professors


def scrape_professors():
    search_url = f"{BASE_URL}/search/professors/4002?q=*"
    response = requests.get(search_url)
    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return

    extract_professor_data(response.text)


if __name__ == "__main__":
    search_and_print_header()
    scrape_professors()
