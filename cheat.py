import random
import urllib
import datetime
import string
#import time; no delay to speed up

total_trees = 0
try:
	while 1:
		time_today = datetime.datetime.today().strftime("%m/%d/%y")
		random_query = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(10,50)))
		response_ecosia = urllib.urlopen("https://www.ecosia.org/search?q={0}".format(random_query)).read().split("<span class=\"pill-text tree-counter-text js-treecount-text\">")[1].split("</span>")[0].replace(" ","").replace("\n","")
		response_ecosia = int(response_ecosia)
		if response_ecosia >= 1:
			total_trees += 1
			print("[{0}] total_record: {1}; search_query: {2}".format(time_today, total_trees, random_query))
		else:
			print("[{0}] increment freezes! you've added {1} trees to be planted.".format(time_today, total_trees))
		#time.sleep(1); no delay to speed up
except:
	with open("scores.log","a+") as scored:
		scored.write("{0}\n".format(total_trees))
	print("saved!!!! {0} total.".format(total_trees))
