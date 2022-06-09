# Hey Quora! Long time no answer!
import time
import datetime

prime = int(input("Enter a number: "))
start_time = time.monotonic()
# Starts the timer
n = 2
while prime % n != 0:
    n += 1
if prime == n:
    print("Prime number!")
else:
    print(prime / n, "×", n, "=", prime)

end_time = time.monotonic()
# Stops timer ^
print(datetime.timedelta(seconds=end_time - start_time))