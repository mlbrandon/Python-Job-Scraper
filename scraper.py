import requests

board = "stripe"
us_only = True
url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs?content=true"

response = requests.get(url)
data = response.json()

jobs = data["jobs"]
print(f"Found {len(jobs)} jobs at {board}")

keywords = ["security", "cyber", "grc", "it risk", "it audit", "intern"]
exclude = ["credit", "fraud", "internal", "international", "sales", "engineer", "software", "financial", "senior", "manager", "director", "lead", "principal", "staff"]
foreign = ["canada", "toronto", "ireland", "dublin", "united kingdom", "london", "singapore", "bengaluru", "mumbai", "australia", "sydney", "japan", "tokyo", "germany", "berlin", "france", "paris", "mexico city", "brazil", "sao paulo", "netherlands", "amsterdam"]

def work_type(text):
    if "hybrid" in text:
        return "Hybrid"
    if "remote" in text:
        return "Remote"
    if "on-site" in text or "onsite" in text:
        return "On-site"
    return "Not listed"

def season(text):
    for s in ["summer", "fall", "winter", "spring"]:
        if s in text:
            return s.title()
    return "Not listed"

for job in jobs:
    title = job["title"].lower()
    location = job["location"]["name"].lower()
    text = (title + " " + location + " " + job["content"]).lower()

    if not any(word in title for word in keywords):
        continue
    if any(word in title for word in exclude):
        continue
    if us_only and any(place in location for place in foreign):
        continue

    print(job["title"], "|", job["location"]["name"], "|", work_type(text), "|", season(text))



