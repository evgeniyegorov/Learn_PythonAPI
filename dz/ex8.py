import requests

longtime_job_url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(longtime_job_url, params={"token":"gMzoTMxoDMwACMz0iNw0SMyAjM"})

print(response.text)
