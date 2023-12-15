import glob
import os

filetypes = ["jpg", "jpeg", "png"]

files = []
for ft in filetypes:
    files.extend(glob.glob("data-females/*." + ft))
files.sort()

count=0
for f in files:
    if not os.path.isfile(f + ".txt"):
        os.remove(f)
        count= count + 1
        #print("Removing ", f)



print(count)
