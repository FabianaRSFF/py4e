fname = input("Enter the file name: ")
try:
	fhand = open(fname)
except Exception:
	print("File cannot be opened", fname)
	quit()


count = 0
for line in fhand:
	if line.startswith("fran"):
        count = count + 1

print("There were: ", count, "fran", fname)
