import requests
from bs4 import BeautifulSoup
from app.logger import logger


def get_job_data(skill: str, pages: int = 1):
    job_list = []
    url= ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    try:
        for page in range(1, pages + 1):
            url = f"https://in.jooble.org/SearchResult?ukw={skill}&p={page}"
            resp = requests.get(url, headers=headers)
            logger.info(f"resp: {resp}\n{url}")
            soup = BeautifulSoup(resp.text, "html.parser")

            for div in soup.find_all("div", class_="WrapperVacancyDescription"):
                title = div.find("a", class_="link-position")
                company = div.find("span", class_="vacancy-serp__vacancy-company")
                logger.info(f"company: {company}")
                if title and company:
                    job_list.append({
                        "title": title.text.strip(),
                        "company": company.text.strip()
                    })

        logger.info(f"{job_list}\n{url}")
    except Exception as e:
        raise Exception(f"get_job_data: {e}")

    return job_list
