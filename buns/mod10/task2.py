import requests
import re

html_code = (requests.get('http://www.columbia.edu/~fdc/sample.html')).text

h3 = re.findall(r'<h3 id=".*?">(.*?)</h3>', html_code)

print(h3)