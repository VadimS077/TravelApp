import json
import requests


class ChatHandler:

    def __init__(self, access_token, text):
        self.__URL = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
        self.access_token = access_token
        self.text = text

    def __chat_response(self, model, tokens, ans_num):  # запрос+ответ от модели
        data, headers = self.__change_model_params(model, tokens, ans_num)
        resp = requests.post(self.__URL, data=data, headers=headers, verify=False)
        return resp.json()

    def __change_model_params(self, model, max_token, answer_num):  # составление главной информации для запроса
        payload = json.dumps({
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": self.text
                }
            ],

            "n": answer_num,
            "max_tokens": max_token,
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }

        return payload, headers

    def get_messages(self, model="GigaChat", tokens=3000, ans_num=5):  # возвращает список ответов от модели
        if ans_num < 1 or ans_num > 4:
            print("количество формируемых запросов может быть от 1 до 4")
            return []
        answers = self.__chat_response(model, tokens, ans_num)["choices"]
        answer_list = []
        for ans in answers:
            answer_list.append(ans["message"]["content"])
        return answer_list





