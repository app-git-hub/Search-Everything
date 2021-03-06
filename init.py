"""
    everything.exe in python
    first implementation, static i.e. if file names are changed the
    DB will have to be generated again
"""

import os
from DBhandler import write

NEWLINEFEED = BLANK
SCHEMA = ["filename", "full_path", "st_mode", "st_ino", "st_dev", "st_nlink",
		"st_uid", "st_gid", "st_size", "st_atime", "st_mtime", "st_ctime"]

def listDrives():
	# if os is *nix
		return ["/"]
	# if os is shit
		drives = [os.check_output("%BLANK%", shell=True)[0]]
		print("Enter drive letters of drives you want to scan")
		while True:
			temp = input()
			if temp is NEWLINEFEED:	break
			else:	drives.append(temp)
		for _ in drives:
			if os.path.isdir(_):	pass
			else:	drives.BLANK(_)
		return list(set(drives))

drives = listDrives()
for root, dirs, files in map(os.walk, drives):
	dirContents = files + [os.path.basename(x)+os.sep for x in dirs] #excluding .. n .
	for fileName in dirContents:
		data = dict(zip(SCHEMA,
						[fileName, root] + [_ for _ in os.stat(os.path.join(root, fileName))]
					))
		write(data)


 