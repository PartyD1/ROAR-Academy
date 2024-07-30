path = "/Users/ParthDoshi/Documents/ROAR Academy/Github/ROAR-Academy/WeekTwoExercizes/"


f = open(path+"demofile.txt", "w")
f.write("Fiat Lux")
f.close()
f = open(path+"demofile.txt", "a")
f.write("\nLet there be light")
f.close()
