# API Automation using Python
import requests
# base url
_ids = [1, 2, 3, 4, 5]
_base_url = "https://reqres.in"
_resource_url = "/api/users?page={}"
url_template = "{}{}".format(_base_url, _resource_url)
formatted_url = [url_template.format(i) for i in _ids]
# response = requests.get(formatted_url[1])
# responseJson = response.json()
# print(responseJson)
# def validate_http_response_code():
#     assert response.status_code == 200
#     print("Http status code is 200OK")
# def validate_page_number():
#     assert responseJson['page'] == _ids[1]
#     print("Current page number is: {}".format(_ids[1]))
# validate_http_response_code()
#
# validate_page_number()


