# Ken Holm
# Purpose:  The Bike class
# Class declaration

class Bike:
    # Private properties
    __numberOfGears: int = 1
    __currentGear: int = 3
    __numberOfWheels: int = 3
    __brakeType: str = "hand"

    # Class instantiator
    def __init__(self, numberOfGears: int = 1, numberOfWheels: int = 2, brakeType: str = "hand") -> None:
        # Set all our properties
        self.setNumberOfGears(numberOfGears)
        self.setNumberOfWheels(numberOfWheels)
        self.setBrakeType(brakeType)

        self.setCurrentGear(1)

    # Getter for the __numberOfGears property
    def getNumberOfGears(self) -> int:
        return self.__numberOfGears

    # Setter for the __numberOfGears property
    #  Valid values are integers from 1 to 15
    def setNumberOfGears(self, numberOfGears: int) -> None:
        try:
            # Is the argument an integer?
            if int(numberOfGears):
                pass

        except Exception as e:
            raise TypeError(f"{numberOfGears} is not an integer: {e}")

        # It is an integer, is it between 1 and 15?
        if 0 < numberOfGears < 16:
            self.__numberOfGears = numberOfGears
        else:
            raise ValueError(f"{numberOfGears} is not between 1 and 15")

    # Getter for the __currentGear property
    def getCurrentGear(self) -> int:
        return self.__currentGear

    # Setter for the __currentGear property
    #  Valid values are integers from 1 to 15
    def setCurrentGear(self, currentGear: int) -> None:
        try:
            # Is the argument an integer?
            if int(currentGear):
                pass

        except Exception as e:
            raise TypeError(f"{currentGear} is not an integer: {e}")

        # It is an integer, is it between 1 and self.__numberOfGears?
        if 0 < currentGear <= self.__numberOfGears:
            self.__currentGear = currentGear
        else:
            raise ValueError(f"{currentGear} is not between 1 and {self.__numberOfGears}")

    # Getter for the __numberOfWheels property
    def getNumberOfWheels(self) -> int:
        return self.__numberOfWheels

    # Setter for the __numberOfWheels property
    #  Valid values are integers from 1 to 4
    def setNumberOfWheels(self, numberOfWheels: int) -> None:
        try:
            # Is the argument an integer?
            if int(numberOfWheels):
                pass

        except Exception as e:
            raise TypeError(f"{numberOfWheels} is not an integer: {e}")

        # It is an integer, is it between 1 and 4?
        if 0 < numberOfWheels <= 5:
            self.__numberOfWheels = numberOfWheels
        else:
            raise ValueError(f"{numberOfWheels} is not between 1 and 4")

    # Getter for the __brakeType property
    def getBrakeType(self) -> str:
        return self.__brakeType

    # Setter for the __brakeType property
    #  Valid values are integers from 1 to 15
    def setBrakeType(self, brakeType: str) -> None:
        try:
            # Is the argument an integer?
            if str(brakeType):
                pass

        except Exception as e:
            raise TypeError(f"{brakeType} is not an string: {e}")

        # It is a string, is it either "hand" or "foot"?
        if brakeType == "hand" or brakeType == "foot":
            self.__brakeType = brakeType
        else:
            raise ValueError(f"{brakeType} is neither 'hand' nor 'foot'")

    # Increase the gear
    #  Do not allow gear to be over the __numberOfGears
    def increaseGear(self) -> None:
        if self.getCurrentGear() < self.__numberOfGears:
            self.setCurrentGear(self.getCurrentGear() + 1)

    # Decrease the gear
    #  Do not allow gear to be below 1
    def decreaseGear(self) -> None:
        if self.getCurrentGear() > 1:
            self.setCurrentGear(self.getCurrentGear() - 1)
