import requests

"""
Search base class
"""

TIMEOUT = 6
ALLOW_REDIRECTS = True


class Search(object):

    @staticmethod
    def search_query(url: str, params: dict) -> dict:
        try:
            resp = requests.get(url=url,
                                params=params,
                                timeout=TIMEOUT,
                                allow_redirects=ALLOW_REDIRECTS)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.HTTPError as err:
            return dict({
                'error': err.response.status_code,
                'msg': err.response.text
            })
