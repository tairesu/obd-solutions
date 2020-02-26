# Code Retriever
from bs4 import BeautifulSoup
import urllib.request
import requests

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
	if is_obdii(code):
		full_site_link = "https://www.obd-codes.com/" + code
		response = requests.get(full_site_link)
		response_text = response.text
		soup = BeautifulSoup(response_text,'html.parser')
		info = {
			'name':soup.find('h1').string
		}
		print(info['name'])

def main():
	code = input("Enter Code: ")
	retrieve_info(code)

if __name__ == '__main__':
	main()
#code = input("Enter DTC Code: ") #Input for now, parameter later
#full_site_link = site_link + code


