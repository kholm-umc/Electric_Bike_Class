# Ken Holm
# Purpose:  The Bike class
# Class declaration


class Bike:
    # Private properties
    __numberOfGears = 1
    __currentGear = 3
    __numberOfWheels = 3
    __brakeType = "hand"

    # Class instantiator
    def __init__(self, numberOfGears: int = 1, numberOfWheels: int = 2, brakeType: str = "hand"):
        # Set all our properties
        self.setnumberofgears(numberOfGears)
        self.setnumberofwheels(numberOfWheels)
        self.setbraketype(brakeType)

        self.setcurrentgear(1)

    # Getter for the __numberOfGears property
    def getnumberofgears(self):
        return self.__numberOfGears

    # Setter for the __numberOfGears property
    #  Valid values are integers from 1 to 15
    def setnumberofgears(self, numberOfGears: int) -> None:
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
    def getcurrentgear(self) -> int:
        return self.__currentGear

    # Setter for the __currentGear property
    #  Valid values are integers from 1 to 15
    def setcurrentgear(self, currentGear: int) -> None:
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
    def getnumberofwheels(self) -> int:
        return self.__numberOfWheels

    # Setter for the __numberOfWheels property
    #  Valid values are integers from 1 to 4
    def setnumberofwheels(self, numberOfWheels: int) -> None:
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
    def getbraketype(self) -> str:
        return self.__brakeType

    # Setter for the __brakeType property
    #  Valid values are integers from 1 to 15
    def setbraketype(self, brakeType: str) -> None:
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
    def increasegear(self) -> None:
        if self.getcurrentgear() < self.__numberOfGears:
            self.setcurrentgear(self.getcurrentgear() + 1)

    # Decrease the gear
    #  Do not allow gear to be below 1
    def decreasegear(self) -> None:
        if self.getcurrentgear() > 1:
            self.setcurrentgear(self.getcurrentgear() - 1)


class ElectricBike(Bike):
    # Private properties
    #__brakeType = "electric"
    __charge    = 100

    # Class instantiator
    # NOTE: I am not requiring brake type here.
    def __init__(self, numberOfGears: int = 1, numberOfWheels: int = 2):
        # Set all our properties
        self.setnumberofgears(numberOfGears)
        self.setnumberofwheels(numberOfWheels)
        self.setbraketype("electric")

        self.setcurrentgear(1)

    # Getter for the __charge property
    def getcharge(self):
        return self.__charge

    # Setter for the __charge property
    #  Valid values are integers from 1 to 100
    def setcharge(self, charge: int) -> None:
        try:
            # Is the argument an integer?
            if int(charge):
                pass

        except Exception as e:
            raise TypeError(f"{charge} is not an integer: {e}")

        # It is an integer, is it between 1 and 100?
        if 0 < charge < 101:
            self.__charge = charge
        else:
            raise ValueError(f"{charge} is not between 1 and 100")

    # Getter for the __brakeType property
    def getbraketype(self) -> str:
        return self.__brakeType

    # Setter for the __brakeType property
    #  Valid values are integers from 1 to 15
    def setbraketype(self, brakeType: str) -> None:
        try:
            # Is the argument an integer?
            if str(brakeType):
                pass

        except Exception as e:
            raise TypeError(f"{brakeType} is not an string: {e}")

        # It is a string, is must be 'electric'
        if brakeType == "electric":
            self.__brakeType = brakeType
        else:
            raise ValueError(f"{brakeType} is not 'electric'")
