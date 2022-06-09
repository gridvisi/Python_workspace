__author__ = 'Administrator'

states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])
stations = {}
stations["kone"] = set(["id","nv","ut"])
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca","az"])
final_stations =set()

print(len(states_needed))

while states_needed:
    best_station = None
    stated_covered = set()
    for station,stated_for_station in stations.items():
        covered = states_needed & stated_for_station
        if len(covered) > len(stated_covered):
            best_station = station
            stated_covered = covered
    states_needed -= stated_covered
    final_stations.add(best_station)
print(final_stations)