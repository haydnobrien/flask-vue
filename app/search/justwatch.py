import json
from .search import Search


BASE_URL = "https://apis.justwatch.com/content/titles/en_AU/popular"
PROVIDERS = ["nfx", "stn", "prv", "sbs", "ivw"]


class JustWatch(Search):
    """
    JustWatch class for looking up tv show and movies titles.
    """

    @staticmethod
    def search_query(url: str = BASE_URL, query: str = ""):
        params = {
            'body': json.dumps({
                'providers': ["nfx", "stn", "prv", "sbs", "ivw"],
                'query': query
            })
        }
        return Search.search_query(url=BASE_URL, params=params)
