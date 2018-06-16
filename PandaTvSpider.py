# python3spider
from urllib.parse import urlencode
import requests
base_url = "https://www.panda.tv/live_lists?"

headers = {
	'Host': 'www.panda.tv',
	'Referer': 'https://www.panda.tv/all',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	'X-Requests-With': 'XMLhttpRequest',
}

def get_page(page):
	params = {
	'status': '2',
	'token': '',
	'pageno': page,
	'pagenum': '120',
	'order': 'top',
	'_': '1529156676586'
	}
	url = base_url + urlencode(params)
	try:
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return	response.json()
	except requests.ConnectionError as e:
		print("Error", e.args)

