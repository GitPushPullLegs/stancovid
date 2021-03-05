# Stanislaus County Covid-19 Dashboard Unofficial API

An unofficial API to pull data from the Stanislaus County Covid-19 Dashboard. [Visit the official dashboard here](https://experience.arcgis.com/experience/c29aa0c6a84844ceab6601da4b124c0b/).


Since this isn't an official API it's subject to break at any time, do not use this in any official capacity.

## Installation
`pip install git+https://github.com/GitPushPullLegs/stancovid.git`

## Quickstart
***General Data***
```python
from stancovid import Client

client = Client()

result = client.get_latest_data()
print(result)

# or disaggregated by zipcode.

result = client.get_by_zipcode()
print(result)
```