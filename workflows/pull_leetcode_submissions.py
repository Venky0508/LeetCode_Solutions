import requests
from bs4 import BeautifulSoup
import json
import time

# Your LeetCode username and password (If scraping requires login)
LEETCODE_USERNAME = 'vnair_25'  # Replace with your LeetCode username
LEETCODE_PASSWORD = 'Venkatesh@0508'  # Replace with your LeetCode password

# Session object to persist cookies and headers
session = requests.Session()

# URL for LeetCode submissions page (replace with actual URL if necessary)
LEETCODE_SUBMISSIONS_URL = f'https://leetcode.com/submissions/detail/'

# Login URL for LeetCode (assuming login is required)
LOGIN_URL = 'https://leetcode.com/accounts/login/'

# LeetCode login headers (optional, depending on scraping method)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def login_to_leetcode(username, password):
    """
    Log into LeetCode to retrieve submissions.
    (This is only needed if LeetCode requires authentication for fetching submissions)
    """
    login_payload = {
        'login': username,
        'password': password,
    }

    response = session.post(LOGIN_URL, headers=HEADERS, data=login_payload)

    if response.status_code == 200:
        print("Logged in successfully!")
    else:
        print(f"Login failed with status code {response.status_code}")
        raise Exception('Login failed')

def fetch_submissions():
    """
    Fetch LeetCode submissions from the user's submissions page
    """

    # Visit the submissions page (or use API, if available)
    response = session.get(LEETCODE_SUBMISSIONS_URL, headers=HEADERS)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Extract submission details using BeautifulSoup
        # You will need to inspect the page structure to know what tags to look for
        submissions = []

        # Assuming submissions are stored in a specific div or table
        for submission in soup.find_all('div', class_='submission-class-name'):  # Replace with actual tag/class
            submission_data = {
                'problem_title': submission.find('a', class_='problem-link').get_text(),
                'status': submission.find('span', class_='status-class').get_text(),
                'date': submission.find('span', class_='date-class').get_text(),
                'code': submission.find('pre').get_text(),  # Assuming code is in <pre> tag
            }
            submissions.append(submission_data)
        
        return submissions
    else:
        raise Exception(f"Failed to fetch submissions, status code {response.status_code}")

def save_submissions_to_file(submissions):
    """
    Save the fetched submissions to a file (e.g., JSON format).
    """
    with open('submissions.json', 'w') as f:
        json.dump(submissions, f, indent=4)

def main():
    # Log in to LeetCode if needed
    login_to_leetcode(LEETCODE_USERNAME, LEETCODE_PASSWORD)

    # Fetch the submissions
    submissions = fetch_submissions()

    # Save the submissions to a file
    save_submissions_to_file(submissions)

if __name__ == "__main__":
    main()
