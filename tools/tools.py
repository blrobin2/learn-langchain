import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str):
    """Searches for LinkedIn or Twitter Profile Page."""
    load_dotenv(override=True)

    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res
