__author__ = "Collin" #change this to your name
__original_author__ = "Collin" #please don't change this
# my page: http://collin.cf/index.html

#libraries
import requests
import os



#if you're new to Python or requests, customize this line only
url = "https://google.com" 



#PLEASE EDIT BELOW THIS LINE WITH CAUTION

# Getting response from url
print("> getting respond...")
response = requests.get(url)

if "200" in str(response):
	print(f"> got {response} in {response.elapsed}")
else:
	print("> got no successful response")
#defined new created path
path = 'output/'

#if path doesn't exists, create it
isExist = os.path.exists(path)
if not isExist:
	os.makedirs(path)
	print("> output directory created [output]")
else:
	print("> output directory already exists [output]")

#write response
print("> writing response content to file...")
with open ("output/content_html.txt", "w") as f:
	f.write(str(response.content))
print("> writing response type to file...")
with open ("output/response_type.txt", "w") as f:
	f.write(str(response))
print("> writing response header to file...")
with open ("output/header.txt", "w") as f:
	f.write(str(response.headers))
print("> writing response time to file...")
with open ("output/rtime.txt", "w") as f:
	f.write(str(response.elapsed))
print("> writing response encoding to file...")
with open ("output/encoding.txt", "w") as f:
	f.write(str(response.encoding))
print("> writing if response is a redirect to file...")
with open ("output/redirect.txt", "w") as f:
	f.write(str(response.is_redirect))

print("> done")
#done

isExistant = os.path.isfile("readme.txt")
if isExistant == True:
	with open ("readme.txt", "w") as f:
		f.write(f"Latest Rezpond you got: {url}\n\nThanks for using Rezpond\ncollin.cf")
else:
	with open ("readme.txt", "w") as f:
		f.write(f"You just got your first Rezpond from {url}\n\nThanks for using Rezpond\ncollin.cf")
