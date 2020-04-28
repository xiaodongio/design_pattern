from abc import ABCMeta, abstractmethod

class Context(metaclass=ABCMeta):

    def __init__(self):
        self.__states = []
        self.__cur_state = None
        self.__state_info = 0

    def addState(self, state):
        if (state is None):
            return False
        if (self.__cur_state is None):
            print("init state : ", state.getName())
        else:
            print("state from ", self.__cur_state.getName(), "change to ", state.getName())
        self.__cur_state = state
        self.addState(state)
        return True

    def getState(self):
        return self.__cur_state

    def _setStateInfo(self, state_info):
        self.__state_info = state_info
        for state in self.__states:
            if(state.isMatch(state_info)):
                self.changeState(state)

    def _getStateInfo(self):
        return self.__state_info



class State:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def isMatch(self, state_info):
        return False

    @abstractmethod
    def behavior(self, context):
        pass