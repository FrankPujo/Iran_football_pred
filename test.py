from statistics import mean

orig_predictions = [0.775, 0.42, 0.753, 0.871, 0.431, 0.9, 0.4, 0.688]
# turn prediction into 1 x 2 format
ord_predictions = sorted(orig_predictions, reverse=True)

avg_win = mean(ord_predictions[:5])
avg_tie = mean(ord_predictions[5:7])
avg_los = mean(ord_predictions[7:])
avg_values = [avg_win, avg_tie, avg_los]

results = list()
for pred in orig_predictions:
	real_value = min(avg_values, key = lambda x: abs(x-pred))
	if real_value == avg_win:
		results.append("1")
	elif real_value == avg_tie:
		results.append("x")
	else:
		results.append("2")

print( orig_predictions, results )