import requests
from unittest import TestCase

class MyTest(TestCase):
    def test_urlSettings(self):
        request= requests.get(UrlSettings('310o').userSolvedUrl)
        self.assertEqual(request.status_code,200)
        

class UrlSettings(object):
    def __init__(self,userName):
        self.api_server = 'https://solved.ac/api'
        self.userName = userName
        self.userSolvedUrl = self.api_server+'/v3/search/problem?query=solved_by:'+self.userName
dic = {}
url = UrlSettings('310o').userSolvedUrl
data = requests.get(url).json()


for j in data['items']:
    dic[j['problemId']]=j['titleKo']
    
for i in dic.items():
    print(i)