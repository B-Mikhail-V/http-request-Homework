import requests
from datetime import datetime
from datetime import timedelta
from pprint import pprint

question_list = []
# today = datetime.date(datetime.today())
today = int(datetime.today().timestamp())
two_days_before = int((datetime.now() - timedelta(days=1)).timestamp())
# upload_url = "https://api.stackexchange.com/2.3/questions?page=20&fromdate=1635724800&todate=1638230400&order=desc&sort=activity&tagged=Python&site=stackoverflow"
upload_url = "https://api.stackexchange.com/2.3/questions?fromdate=" + str(two_days_before) + "&todate=" + str(today) + "&order=desc&sort=activity&tagged=Python&site=stackoverflow"
response = requests.get(upload_url)
for item in response.json()['items']:
    question_list.append(item['title'])
pprint(question_list)
print(len(question_list))

print(type(two_days_before))
pprint(upload_url)
pprint(two_days_before)

