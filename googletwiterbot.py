from TwitterAPI import TwitterAPI
import urllib
import time
import random
questions = ['who','where','when','what','why','how']
api = TwitterAPI("BAdDj2rEARI3zJSSHwxx9TGdw", "MaODwRgWZXiqZmb8Wx3xAhB9zfE0QtJMfOTr2vjYyYvKD51a4K", "766666113526669312-ylIahLXRotQTCRMIoQyGgh96y4O4R9a", "0H9ZD6wd9Cc6565s3jrFNqMWcvPvLmAXHje2cZPJOEV9Y")
while True:
	r = api.request('search/tweets', {'q':questions[random.randint(0,5)]})
	for item in r.get_iterator():
		try:
			api.request('statuses/update',{'authenticity_token':'1d2ae98076b612332e73df454ebf4b1909529b09','in_reply_to_status_id':item['id'], 'status':'@' + item['user']['screen_name'] + ' lmgtfy.com/?'+urllib.urlencode({'q':item['text']})})
			print "https://twitter.com/"+item['user']['screen_name']+"/status/"+str(item['id'])
		except UnicodeEncodeError:
			print "@"+item['user']['screen_name']+" needs to stop using emojis!"
	time.sleep(10)