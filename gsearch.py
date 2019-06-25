#import requests
import bs4
import pycurl
import io
import certifi
import json

class Error(Exception):
	pass

class NetworkError(Error):
	pass

class DecodeError(Error):
	pass

def reverse_gimage(imagelink : str):
	try:
		redirURL = "https://images.google.com/searchbyimage?image_url=" + imagelink
		final = io.BytesIO()
		curling = pycurl.Curl()
		curling.setopt(curling.CAINFO, certifi.where())
		curling.setopt(curling.URL, redirURL)
		curling.setopt(curling.FOLLOWLOCATION, 1)
		curling.setopt(curling.USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
		curling.setopt(curling.WRITEFUNCTION, final.write)
		curling.perform()
		curling.close()
	except:
		raise NetworkError("couldn't get webpage from Google")
	try:
		soup = bs4.BeautifulSoup(final.getvalue().decode('UTF-8'), 'html.parser')
		rawoutput = soup.findAll('a', attrs={'class':'fKDtNb'})
		output = []
	except:
		raise DecodeError("failed to decode properly. improper or unexpected data was likely supplied. updating this module may fix this")
		for x in rawoutput:
			output.append(x.get_text())
		if output == "[]":
			#return("gosh darn\n\n" + str(soup)[50:] + "\n\n...etc., etc.")
			raise DecodeError("failed to decode properly. improper or unexpected data was likely supplied. updating this module may fix this")
		else:
			return(output)

def reverse_gimage_link(imagelink : str):
	return("https://images.google.com/searchbyimage?image_url=" + str(imagelink))

def get_autocomplete_entry(query : str):
	try:
		url = "http://suggestqueries.google.com/complete/search?client=firefox&q=" + query.replace('+', '%2B').replace(' ', '+')
		final = io.BytesIO()
		curling = pycurl.Curl()
		curling.setopt(curling.CAINFO, certifi.where())
		curling.setopt(curling.URL, url)
		curling.setopt(curling.FOLLOWLOCATION, 1)
		curling.setopt(curling.USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
		curling.setopt(curling.WRITEFUNCTION, final.write)
		curling.perform()
		curling.close()
	except:
		raise NetworkError("couldn't get webpage from Google")
	try:
		return(json.loads(final.getvalue().decode('UTF-8'))[1])
	except:
		raise DecodeError("failed to decode properly. improper or unexpected data was likely supplied. updating this module may fix this")
