import urllib.error
import urllib.parse
import urllib.request  # noqa E401

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
"""for line in fhand:
    print(line.decode().strip())"""


counts: dict[str, int] = {}
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
