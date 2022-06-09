'''
https://brilliant.org/daily-problems/who-is-the-fastest-sprinter/

In this race, Plum and Matteo both wreck and don't finish all five laps.



Plum finished 3 \frac123
2
1
​
  laps in 66 minutes.
Matteo finished 11 less lap than Plum in 66 minutes.
Frog finished 55 laps in 99 minutes.
MP finished 55 laps 11 minute faster than Frog.\\[-0.7em]
Who ran their laps the fastest?
'''

print(*sorted([(name, f"{laps/time:.3f}")
      for name, laps, time
      in [("Plum", 3.5, 6), ("Matteo", 2.5, 6), ("Frog", 5, 9), ("MP", 5, 8)]],
      key=lambda x: x[1], reverse=True))

