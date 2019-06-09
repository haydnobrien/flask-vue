import json
from .search import Search

"""
https://apis.justwatch.com/content/titles/en_AU/popular?body=%7B%22age_certifications%22:null,%22content_types%22:null,%22genres%22:null,%22languages%22:null,%22max_price%22:null,%22min_price%22:null,%22monetization_types%22:%5B%22flatrate%22,%22rent%22,%22buy%22,%22ads%22,%22free%22%5D,%22page%22:1,%22page_size%22:30,%22presentation_types%22:null,%22providers%22:%5B%22nfx%22,%22stn%22,%22prv%22,%22sbs%22,%22ivw%22%5D,%22release_year_from%22:null,%22release_year_until%22:null,%22scoring_filter_types%22:%7B%22tomato:meter%22:%7B%22min_scoring_value%22:90,%22max_scoring_value%22:0%7D%7D,%22timeline_type%22:null%7D
body: {"age_certifications":null,"content_types":null,"genres":null,"languages":null,"max_price":null,"min_price":null,"monetization_types":["flatrate","rent","buy","ads","free"],"page":1,"page_size":30,"presentation_types":null,"providers":["nfx","stn","prv","sbs","ivw"],"release_year_from":null,"release_year_until":null,"scoring_filter_types":{"tomato:meter":{"min_scoring_value":90,"max_scoring_value":0}},"timeline_type":null}

a = {"age_certifications": null, "content_types": null, "genres": null, "languages": null, "max_price": null,
     "min_price": null, "monetization_types": ["flatrate", "rent", "buy", "ads", "free"], "page": 1, "page_size": 30,
     "presentation_types": null, "providers": ["nfx", "stn", "prv", "sbs", "ivw"], "release_year_from": null,
     "release_year_until": null,
     "scoring_filter_types": {"tomato:meter": {"min_scoring_value": 90, "max_scoring_value": 0}}, "timeline_type": null}
"""

BASE_URL = "https://apis.justwatch.com/content/titles/en_AU/popular"
PROVIDERS = ["nfx", "stn", "prv", "sbs", "ivw"]


class JustWatch(Search):

    @staticmethod
    def search_query(url: str = BASE_URL, query: str = ""):
        params = {
            'body': json.dumps({
                'providers': ["nfx", "stn", "prv", "sbs", "ivw"],
                'query': query
            })
        }
        return Search.search_query(url=BASE_URL, params=params)
