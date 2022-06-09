def sum_of_a_beach(beach):
    beach_low = beach.lower()
    return beach_low.count("sand")+beach_low.count("water")+beach_low.count("sun")+beach_low.count("fish")
Find The Parity Outlier

print(sum_of_a_beach("sunsunsunsun"))