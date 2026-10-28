import requests
from config import USAJOBS_KEY, USAJOBS_EMAIL

url = "https://data.usajobs.gov/api/search"
headers = {
    "Host": "data.usajobs.gov",
    "User-Agent": USAJOBS_EMAIL,
    "Authorization-Key": USAJOBS_KEY,
}
params = {"HiringPath": "student", "ResultsPerPage": 50}

response = requests.get(url, headers=headers, params=params)
print("Status:", response.status_code)

data = response.json()
items = data["SearchResult"]["SearchResultItems"]
print(f"Found {len(items)} jobs on USAJOBS")

for item in items:
    job = item["MatchedObjectDescriptor"]
    print(job["PositionTitle"], "|", job["PositionLocationDisplay"], "|", job["OrganizationName"])
