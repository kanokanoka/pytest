import urllib.parse
import pycurl

def get():
	curl = pycurl.Curl()
	curl.setopt(pycurl.URL, 'http://127.0.0.1:3000')
	curl.setopt(pycurl.CUSTOMREQUEST, 'GET')
	curl.perform()

def post():
	curl = pycurl.Curl()
	curl.setopt(pycurl.URL, 'http://127.0.0.1:3000')
	field_data = urllib.parse.urlencode({'key':'value'})
	curl.setopt(pycurl.POSTFIELDS, field_data)
	curl.perform()

get()
post()
