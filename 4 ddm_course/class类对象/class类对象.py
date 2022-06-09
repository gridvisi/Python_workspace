class DataTest:
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.d = {self.id: 1,
                  self.address: "192.168.1.1"
                  }

    def __getitem__(self, key):
        return "hello"


data = DataTest(1, "192.168.2.11")
print(data[2])


class Items:
  def __init__(self, values):
    self._values = list(values)

  def __len__(self):
    return len(self._values)

  def __getitem__(self, item):
    return self.__values.__getitem__(item)

values = ['apple','banana','carror']
item = Items(values)
#print(item.__getitem__())

# hello_world.py
def hello_world():
   print("Hello, world.")
#This function is called from a top level function like so:

# main.py
#from hello_world import hello_world

if __name__ == "__main__":
   hello_world()

# hello_world.py
config = {}
def hello_world():
    output_function = config["OUTPUT_FUNCTION"]
    output_function("Hello, world.")

#main.py
#import hello_world
#hello_world.config["OUTPUT_FUNCTION"] = print

#if __name__ == "__main__":
#    hello_world.hello_world()