scores=[85, 92, 78, 95, 88 ,72, 90]
total=0
for i in scores:
    total=total+i
average=total/len(scores)
print("Scores: ",scores)
print("Total: ",total)
print("Average: {:.1f}".format(average))
print("Highest: ",max(scores))
print("Lowest: ",min(scores))