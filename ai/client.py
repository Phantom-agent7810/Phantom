import requests


class HTTPClient:
    def post(self, url: str, headers: dict, json: dict):
        response = requests.post(
            url=url,
            headers=headers,
            json=json,
            timeout=30,
        )

        print("\n========== HTTP DEBUG ==========")
        print("Request URL :", response.request.url)
        print("Status Code :", response.status_code)
        print("Response Body:")
        print(response.text)
        print("================================\n")

        response.raise_for_status()
        return response.json()
