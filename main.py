import facebook,requests,re
import os,random,time
from keep_alive import keep_alive
keep_alive()
access_token = os.environ['api_key']
api = os.environ['api']
def add_post(content):
	try:
		graph = facebook.GraphAPI(access_token)
		graph.put_object("me","feed",message=content)
	except Exception as e:
		print(e)
def get_hadith(num):
	try:
		req = requests.get(api+num).json()["data"]
		return ("হাদিস:- "+req["description"]+"\n\n"+req["explanation"]+"\n\n- "+req["book"]["title"]+" Muslim Bangla App").replace("<br>","\n")
	except Exception as e:
		print(e)
i = 0
while True:
	if i == 5:
		time.sleep(60*15)
		i = 0
	else:
		add_post(get_hadith(str(random.choice(range(1,65832)))))
		i +=1
