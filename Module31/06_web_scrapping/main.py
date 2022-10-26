import re
import requests


my_rec = requests.get('http://www.columbia.edu/~fdc/sample.html').text
site_subtitle = re.findall(r'<h3.*?>(.*?)</h3>', my_rec)
print(site_subtitle)
