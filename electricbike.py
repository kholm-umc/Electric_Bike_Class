# Ken Holm
# Purpose:  The ElectricBike class, a subclass of the Bike class
# Class declaration

from bike import Bike

class ElectricBike(Bike):
    # Private properties
    __charge: int = 99
    __maxCharge: int = 100

    # Class instantiator
    # NOTE: I am not asking for brake type here.
    def __init__(self, numberOfGears: int = 0, numberOfWheels: int = 2) -> None:
        # Set all our properties
        self.setNumberOfGears(numberOfGears)
        self.setNumberOfWheels(numberOfWheels)
        self.setBrakeType("electric")

        self.setCurrentGear(1)

    # Getter for the __charge property
    def getCharge(self) -> int:
        return self.__charge

    # Setter for the __charge property
    #  Valid values are integers from 0 to 100
    def setCharge(self, charge: int) -> None:
        try:
            # Is the argument an integer?
            if int(charge):
                pass

        except Exception as e:
            print(f"Warning: {charge} is not a valid integer")

        # It is an integer, is it between 0 and 100?
        if -1 < charge < self.__maxCharge:
            self.__charge = charge
        else:
            print(f"WARNING: {charge} appears to be less than 1 or greater than {self.__maxCharge}")

    # Getter for the __brakeType property
    def getBrakeType(self) -> str:
        return self.__brakeType

    # Setter for the __brakeType property
    #  Valid values are integers from 0 to 15
    def setBrakeType(self, brakeType: str) -> None:
        try:
            # Is the argument an integer?
            if str(brakeType):
                pass

        except Exception as e:
            print(f"WARNING: You must supply a brake type")

        # It is a string, is must be 'electric'
        if brakeType == "electric":
            self.__brakeType = brakeType
        else:
            print(f"WARNING: A brake type of {brakeType} is not allowed")
