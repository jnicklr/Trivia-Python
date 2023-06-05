from urllib.request import urlopen
import json 
import random

response = urlopen("https://opentdb.com/api.php?amount=50&difficulty=easy&type=boolean").read().decode('utf8')
data = json.loads(response)
