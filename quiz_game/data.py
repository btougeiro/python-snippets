import requests
import html

API_URL = "https://opentdb.com/api.php"


class QuestionData:

    def __init__(self):
        self.api_parameters = {"amount": 10, "type": "boolean"}
        self.response = requests.get(url=API_URL, params=self.api_parameters)
        self.response.raise_for_status()
        self.question_data = self.response.json()["results"]
        for data in self.question_data:
            data["question"] = html.unescape(data["question"])

    def get_question_data(self) -> list:
        return self.question_data

    def get_num_of_questions(self) -> int:
        return self.api_parameters["amount"]
