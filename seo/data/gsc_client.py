import requests


class GSCClient:

    def __init__(self, access_token, site_url):

        self.token = access_token
        self.site_url = site_url
        self.base = "https://www.googleapis.com/webmasters/v3"

    def query(self, start_date, end_date):

        url = f"{self.base}/sites/{self.site_url}/searchAnalytics/query"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        payload = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["query", "page"]
        }

        r = requests.post(url, json=payload, headers=headers)
        return r.json()