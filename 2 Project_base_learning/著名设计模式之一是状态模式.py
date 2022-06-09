
#灯泡状态图  # if we get wrong input

class LightBulb:
    _state = 'OFF'  # 初始化关灯initial state of bulb

    def onOff(self, switch):
        if switch == 'ON':
            self._state = 'ON'
        elif switch == 'OFF':
            self._state = 'OFF'
        else: # if we get wrong input
            continue

#状态模式的UML类图
# 1) 找到一个包含状态依赖代码的现有类，或者创建一个合适的上下文类。
# 它应该包括对特定状态的引用，以及在不同状态间切换的方法。
from __future__ import annotations
from abc import ABC, abstractmethod

'''
2) 为所有具体状态创建一个通用的State接口。状态接口指定了所有具体状态必须实现的所有方法，
以及对Context对象的反向引用。状态可以通过使用这个反向引用将Context改变为另一个状态。

'''
class Context:

    _state = None

    def __init__(self, state: State) -> None:
        self.setState(state)

    def setState(self, state: State):

        print(f"Context: Transitioning to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def doSomething(self):
        self._state.doSomething()


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def doSomething(self) -> None:
        pass



class ConcreteStateA(State):
    def doSomething(self) -> None:
        print("The context is in the state of ConcreteStateA.")
        print("ConcreteStateA now changes the state of the context.")
        self.context.setState(ConcreteStateB())


class ConcreteStateB(State):
    def doSomething(self) -> None:
        print("The context is in the state of ConcreteStateB.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.setState(ConcreteStateA())



#4) You can now initiate your application with an initial state and execute the methods.

# sample application
app = Context(ConcreteStateA())
app.doSomething()    # this method is executed as in state 1
app.doSomething()    # this method is executed as in state 2
'''

#Context: Transitioning to ConcreteStateA
The context is in the state of ConcreteStateA.
ConcreteStateA now changes the state of the context.
Context: Transitioning to ConcreteStateB
The context is in the state of ConcreteStateB.
ConcreteStateB wants to change the state of the context.
Context: Transitioning to ConcreteStateA
'''

'''
Example
Let's create a simple state machine that represents a real-world scenario. 
Consider an elevator system with buttons in the elevator cabin that allow you 
to go up or down. Consider that this lift only travels between two floors to 

keep things simple. There are primarily two possible states for the elevator: 
1st floor and 2nd floor. The input from the two buttons determines the transition 
between states. The elevator performs different actions based on its state.

The following code is the implementation of the elevator example. 
Follow along with the comments for more descriptions about each method.
'''
from __future__ import annotations
from abc import ABC, abstractmethod

# The Elevator class is the context. It should be initiated with a default state.
class Elevator:

    _state = None

    def __init__(self, state: State) -> None:
        self.setElevator(state)

    # method to change the state of the object
    def setElevator(self, state: State):

        self._state = state
        self._state.elevator = self

    def presentState(self):
        print(f"Elevator is in {type(self._state).__name__}")

    # the methods for executing the elevator functionality. These depends on the current state of the object.
    def pushDownBtn(self):
        self._state.pushDownBtn()

    def pushUpBtn(self):
        self._state.pushUpBtn()

    # if both the buttons are pushed at a time, nothing should happen
    def pushUpAndDownBtns(self) -> None:
        print("Oops.. you should press one button at a time")

    # if no button was pushed, it should just wait open for guests
    def noBtnPushed(self) -> None:
        print("Press any button. Up or Down")


# The common state interface for all the states
class State(ABC):
    @property
    def elevator(self) -> Elevator:
        return self._elevator

    @elevator.setter
    def elevator(self, elevator: Elevator) -> None:
        self._elevator = elevator

    @abstractmethod
    def pushDownBtn(self) -> None:
        pass

    @abstractmethod
    def pushUpBtn(self) -> None:
        pass


# The concrete states
# We have two states of the elevator: when it is on the First floor and the Second floor
class firstFloor(State):

    # If the down button is pushed when it is already on the first floor, nothing should happen
    def pushDownBtn(self) -> None:
        print("Already in the bottom floor")

    # if up button is pushed, move upwards then it changes its state to second floor.
    def pushUpBtn(self) -> None:
        print("Elevator moving upward one floor.")
        self.elevator.setElevator(secondFloor())


class secondFloor(State):

    # if down button is pushed it should move one floor down and open the door
    def pushDownBtn(self) -> None:
        print("Elevator moving down a floor...")
        self.elevator.setElevator(firstFloor())

    # if up button is pushed nothing should happen
    def pushUpBtn(self) -> None:
        print("Already in the top floor")


if __name__ == "__main__":
    # The client code.

    myElevator = Elevator(firstFloor())
    myElevator.presentState()

    # Up button is pushed
    myElevator.pushUpBtn()

    myElevator.presentState()

'''
总结

在这篇文章中，你学会了如何在 Python 编程中使用状态模式来设计状态机。在不使用较大的条件块来
实现特定状态的行为的情况下，状态模式使开发过程变得简单了许多。你还可以添加不依赖其他状态的新
状态，使你的应用程序更加灵活。状态模式与策略模式非常相似，后者根据用户的选择改变策略。
​
主要的区别在于，具体的状态是知道其他状态的，而策略则不知道。为什么我们说状态意识到其他状态呢？
因为每个状态都要知道它们应该移动到哪个状态。例如，一楼的状态知道他们应该换到二楼的状态。与策略
模式的另一个重要区别是，在策略模式中，是客户，为Context提供不同的策略，而在状态模式中，状态转
换是由Context或State自己管理的。试着在你的软件中使用状态模式，使开发过程更加顺利地进行。
'''