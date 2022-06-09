def find_children(santas_list, children):
    return sorted(set(santas_list)&set(children),reverse=False)
print(find_children(["jASon", "JAsoN", "JaSON", "jasON"],["JasoN", "jASOn", "JAsoN", "jASon", "JASON"]))