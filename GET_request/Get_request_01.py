# API Automation using Python
import requests
# base url
_ids = [1, 2, 3, 4, 5]
for i in range (0, _ids.__len__(),):
    _base_url = "https://reqres.in"
    _resource_url = "/api/users?page={}"
    url_template = "{}{}".format(_base_url, _resource_url)
    formatted_url = [url_template.format(i) for i in _ids]
    response = requests.get(formatted_url[i])
    responseJson = response.json()
    print(responseJson)

