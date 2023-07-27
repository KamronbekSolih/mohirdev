from urllib.request import urlopen, Request

url = 'http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html'

request = Request(url)

response = urlopen(request)

response = response.read()

response = list(response)
file = open("number_pi.txt", "w+")
for character in response:
  if type(character) == int:
      file.write(str(character))
  else:
      continue

