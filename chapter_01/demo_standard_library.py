import sys
import os
import datetime
import time
import html

print(sys.platform)
print(sys.version)
print(os.getcwd())
print(os.environ)
print(os.getenv('APPDATA'))
print(datetime.date.today())
print(datetime.date.today().year)
print(datetime.date.today().month)
print(datetime.date.today().day)
print(time.strftime("%I:%M"))
print(time.strftime("%A %p"))
print(html.escape("This HTML fragment contains a <script>body</script> tag"))
print(html.unescape("I &hearts; Python's &lt;standard library&gt;"))
