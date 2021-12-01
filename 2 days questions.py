import requests
from datetime import datetime
from datetime import timedelta
from pprint import pprint
import time


class Stockover:

    def __init__(self):
        self.today = int(datetime.today().timestamp())
        self.two_days_before = int((datetime.now() - timedelta(days=2)).timestamp())

    def question_list(self, tag='Python'):
        question_list = []
        url_question = "https://api.stackexchange.com/2.3/questions"
        params_const = {"page": "20", "order": "desc", "sort": "activity", "site": "stackoverflow", "tagged": tag}
        params_var = {"fromdate": self.two_days_before, "todate": self.today}
        params = {**params_var, **params_const}
        response = requests.get(url_question, params=params)
        for item in response.json()['items']:
            question_list.append(item['title'])
        return question_list


if __name__ == '__main__':

    sctk = Stockover()
    pprint(sctk.question_list())
