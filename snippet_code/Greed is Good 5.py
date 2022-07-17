def score(dice):
    sum = 0
    sum += dice.count(1) // 3 * 1000
    sum += dice.count(1) % 3 * 100
    sum += dice.count(6) // 3 * 600
    sum += dice.count(5) // 3 * 500
    sum += dice.count(5) % 3 * 50
    sum += dice.count(4) // 3 * 400
    sum += dice.count(3) // 3 * 300
    sum += dice.count(2) // 3 * 200
    return sum
print(score([2, 4, 4, 5, 4]))

#best code
#score=lambda d:100*(sum(i+9*(i==1)for i in range(7)if d.count(i)>2)+d.count(1)%3+d.count(5)%3/2)