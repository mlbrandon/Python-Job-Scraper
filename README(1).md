# Python Job Scraper (Learning Project)

A Python tool I built on Linux Mint to pull live job postings from public job APIs and filter them for cybersecurity internships. Built in one day as my first Python project, October 2026.

**Author:** Miles Brandon, Cybersecurity student at Old Dominion University (CompTIA Security+)

## What it does

- **scraper.py** pulls jobs from company boards on the **Greenhouse Job Board API** (public, read-only), then filters them:
  - keyword list (security, cyber, grc, it risk, it audit, intern)
  - exclude list (senior-level titles, engineering, finance-only roles)
  - U.S.-only switch (`us_only = True`)
  - tags each job as Hybrid / Remote / On-site and Summer / Fall / Winter / Spring by searching the full description ("Not listed" when the posting doesn't say)
- **usajobs.py** pulls federal student roles from the official **USAJOBS Search API** and filters titles for cyber, IT, audit, and compliance.

## Setup

```bash
mkdir ~/job-scraper && cd ~/job-scraper
python3 -m venv venv
source venv/bin/activate
pip install requests
```

For USAJOBS, request a free key at developer.usajobs.gov, copy `config.example.py` to `config.py`, fill in your key and the email you registered with, and lock it down:

```bash
cp config.example.py config.py
chmod 600 config.py
```

`config.py` holds secrets and is **never** committed to this repo.

## Why APIs instead of scraping LinkedIn or Handshake

Those sites prohibit automated scraping in their terms of service. APIs are the official, permitted way to get data: you request access, agree to the terms, and the provider decides what you receive. That's clear authorization.

## What I learned

- Linux terminal basics: paths, `mkdir`, `cd`, `ls -l`, `chmod 600`, exit codes (0 / 1 / 127)
- Python: variables, lists, loops, `if` / `continue` checkpoints, functions, f-strings
- Virtual environments and `pip`
- Calling REST APIs with headers and parameters; reading HTTP status codes (200 OK, 401 unauthorized)
- Debugging by reading Python tracebacks (line number, caret, error type)
- Handling secrets: keys kept out of code, file permissions set to owner-only
- Substring matching traps ("it risk" inside "credit risk", "uk" inside "Milwaukee") and how exclude lists fix them

## Limitations

- Greenhouse only covers companies whose board tokens I add by hand.
- USAJOBS student listings skew toward finance and accounting roles.
- Many GRC and SOC internships are posted on LinkedIn, Handshake, or Workday career sites, which have no public API. Those I still check by hand.

## Possible next step

An application tracker that reads my own Gmail through Google's official API and updates application status automatically from confirmation, interview, and rejection emails.
