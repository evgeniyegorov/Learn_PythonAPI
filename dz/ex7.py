import requests

parameters = ["GET", "POST", "PUT", "DELETE", "HEAD"]

compare_query_type_url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

for i in range(len(parameters)):
    url1 = requests.get(compare_query_type_url, params={"method": parameters[i]})
    url2 = requests.post(compare_query_type_url, data={"method": parameters[i]})
    url3 = requests.put(compare_query_type_url, data={"method": parameters[i]})
    url4 = requests.delete(compare_query_type_url, data={"method": parameters[i]})
    url5 = requests.head(compare_query_type_url, data={"method": parameters[i]})
    print(' i = ',i, '    param = ' ,parameters[i],' | ',url1.text,' | ',url2.text,' | ',url3.text,' | ',url4.text,' | ',url5.status_code,' |')
