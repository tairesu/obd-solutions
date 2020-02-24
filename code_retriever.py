# Code Retriever
from bs4 import BeautifulSoup
import urllib.request

def is_obdii(code):
	requirements = {
		'first_digit': ["p","b","c","u"],
		'second_digit': [str(num) for num in range(3)],
		'third_digit': [str(num) for num in range(10)]
	}
	is_code = True
	for count,character in enumerate(code[0:3]):
		if character.lower() in list(requirements.values())[count]:
			continue
		else:
			is_code = False
			print("Invalid " + list(requirements.keys())[count])
			break

	return is_code
			
def retrieve_info(code):
	info = {}
	if is_obdii(code):
		site_link = "https://www.obd-codes.com/"
		full_site_link = site_link + code
		headers = {}
		headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0"
		request = urllib.request.Request(full_site_link, headers=headers)

		with urllib.request.urlopen(request) as response:
			html = response.read()

		soup = BeautifulSoup(html,'html.parser')
		#name = soup.find('title').string

		print(name)
		

def main():
	retrieve_info("p0231")

if __name__ == '__main__':
	main()
#code = input("Enter DTC Code: ") #Input for now, parameter later
#full_site_link = site_link + code


