
class Father():
    def __init__(self,name):
        self.name = name


    def selfDemo(self):
        print('I am Father, My name is %s_%s' % (self.name,self))


class Son1(Father):
    def selfDemo(self):
        print('I am Son1, My name is %s_%s' % (self.name,self))

class Son2(Father):

    def selfDemo(self):
        print('I am Son2, My name is %s_%s' % (self.name,self))

f1 = Father('Jack')
f2 = Father('Peter')
f1.selfDemo()
Father.selfDemo(f1)
f2.selfDemo()