import re
from sys import argv
fileregex = re.compile(r'.*/(.*\.tgz)')
finding = fileregex.search(argv[1])
match = finding.group(1)
print(match)