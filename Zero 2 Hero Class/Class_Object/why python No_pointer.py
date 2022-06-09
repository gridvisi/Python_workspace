
class Metrics(object):
    def __init__(self):
        self._metrics = {
            "func_calls": 0,
            "cat_pictures_served": 0,
        }

    @property
    def func_calls(self):
        return self._metrics["func_calls"]

    @property
    def cat_pictures_served(self):
        return self._metrics["cat_pictures_served"]

    def inc_func_calls(self):
        self._metrics["func_calls"] += 1

    def inc_cat_pics(self):
        self._metrics["cat_pictures_served"] += 1

p = Metrics()
print(p.inc_func_calls())
print(p.cat_pictures_served)
print(p.inc_func_calls())
print(p.inc_cat_pics())

print(p.func_calls)
print(p.func_calls)