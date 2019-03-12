# Remember to make your own file with api_keys - DO NOT PUBLISH YOUR API KEYS
import api_keys

url = "https://github.com/datsoftlyngby/dat4sem2019spring-python-materials"
headers = {"Authorization": "token {}".format(api_keys.GITHUB_API_KEY)}