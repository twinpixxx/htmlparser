from bs4 import BeautifulSoup
import requests, fake_useragent


# User-Agent installation
userAgent = fake_useragent.UserAgent() 
user = userAgent.random
userInfo = {'User-Agent':str(user)}

print("Input your url")
url = input("http://")
page = requests.get("http://"+url.split()[0])
soup = BeautifulSoup(page.text, "html.parser")

# HTML Parse at all
if url.split()[0] == url.split()[-1]:
	with open("index.html", "w") as html:
		for tag in soup.findAll("html"):
			html.write(str(tag))
		print("parsing succeed, check index file")

#H TML Parse by tag
elif url.split()[1] == url.split()[-1]:
	with open("index.html", "w") as html:
		for tag in soup.findAll(url.split()[1]):
			html.write(str(tag))
		print("parsing succeed, check index file")

# HTML Parse info inside tag
else:
	if url.split()[2] == "inside":
		with open("index.html", "w") as html:
			for tag in soup.findAll(url.split()[1]):
				html.write(tag.text)
		print("parsing succeed, check index file")

# HTML Parse info inside attr
	else: 
		with open("index.html", "w") as html:
			for tag in soup.findAll(url.split()[1]):
				html.write(tag[url.split()[2]])