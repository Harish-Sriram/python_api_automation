# API Automation using Python
import requests
# base url
_ids = [1, 2, 3, 4, 5]
_base_url = "https://reqres.in"
_resource_url = "/api/users?page={}"
url_template = "{}{}".format(_base_url, _resource_url)
formatted_url = [url_template.format(i) for i in _ids]
for j in range(0, 5):
    response = requests.get(formatted_url[j])
    response_json = response.json()
    print(response_json)
    assert response.status_code == 200
    print("Http status code is 200OK")
    assert response_json['page'] == _ids[j]
    print("Current page number is: {}".format(_ids[j]))





