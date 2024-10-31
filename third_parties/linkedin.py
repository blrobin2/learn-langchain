import os
import json
import requests
from dotenv import load_dotenv

from .profile import profile

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        data = profile()
    else:
        api_key = os.environ["PROXYCURL_API_KEY"]
        headers = {"Authorization": "Bearer " + api_key}
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"

        response = requests.get(
            api_endpoint, params={"url": linkedin_profile_url}, headers=headers
        )

        data = response

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", " ", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return json.dumps(data)


if __name__ == "__main__":
    res = scrape_linkedin_profile(
        "https://www.linkedin.com/in/bennie-robinson-48021331", mock=True
    )
    print(res)
