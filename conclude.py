with open("scores.log") as f_score:
	summed_score = 0
	for x in f_score.read().split("\n"):
		if x.isdigit():
			summed_score+=int(x)

with open("scores.log","w+") as f_score:
	f_score.write("{0}\n".format(summed_score))

print("summed score: {0}".format(summed_score))
print("total trees: {0}".format(summed_score//45))
