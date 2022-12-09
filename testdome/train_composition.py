# A TrainComposition is built by attaching and detaching wagons from the left and the right sides, efficiently with respect to time used.
#
# For example, if we start by attaching wagon 7 from the left followed by attaching wagon 13, again from the left, we get a composition of two wagons (13 and 7 from left to right). Now the first wagon that can be detached from the right is 7 and the first that can be detached from the left is 13.

from collections import deque

class TrainComposition:

    def __init__(self):
        self.wagons = deque()

    def attach_wagon_from_left(self, wagonId):
        """
        :param wagonId: (int) The number of the wagon to attach to the left
        """
        self.wagons.insert(0,wagonId)

    def attach_wagon_from_right(self, wagonId):
        """
        :param wagonId: (int) The number of the wagon to attach to the right
        """
        self.wagons.append(wagonId)

    def detach_wagon_from_left(self):
        """
        :returns: (int) The number of the wagon detached from left
        """
        return self.wagons.popleft() if self.wagons else None

    def detach_wagon_from_right(self):
        """
        :returns: (int) The number of the wagon detached from right
        """
        return self.wagons.pop() if self.wagons else None

if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    print(train.detach_wagon_from_left())
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right()) # should print 7
    print(train.detach_wagon_from_left()) # should print 13