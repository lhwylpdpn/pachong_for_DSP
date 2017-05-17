import urllib 
import urllib2 

def test():
	url = 'https://ad.toutiao.com/overture/data/advertiser/ad/' 
	user_agent = 'ces' 

	values = {'name' : 'Michael Foord', 
	          'location' : 'pythontab', 
	          'language' : 'Python' } 
	headers = { 'User-Agent' : user_agent } 
	data = urllib.urlencode(values) 
	req = urllib2.Request(url, data, headers) 
	response = urllib2.urlopen(req) 
	the_page = response.read()
	print(the_page)

if __name__ == '__main__':
	test()