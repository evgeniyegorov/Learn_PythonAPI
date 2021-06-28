import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
print("Количество редиректов = " + str(len(response.history)))
print("Конечный URL: " + response.history[len(response.history)-1].url)


