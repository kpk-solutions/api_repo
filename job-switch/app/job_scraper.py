import requests
from bs4 import BeautifulSoup

def get_job_data(skill: str, pages: int):
    job_list = []
    # Code for scraping job data (from example URLs)
    for page in range(1, pages + 1):
        url = f"https://example.com/jobs?q={skill}&page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        job_items = soup.find_all('div', class_='job-item')
        for job in job_items:
            job_title = job.find('h2').text
            company = job.find('span', class_='company').text
            job_list.append({"title": job_title, "company": company})
    return job_list
