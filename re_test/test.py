# re is the regular expression library
import re

pattern = r"test"
words = "aaatestcomand"

match = re.match(pattern,words)
print(match)

search = re.search(pattern,words)
print(search)
