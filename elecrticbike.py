from bike import Bike


class ElectricBike(Bike):
    # Private properties
    __charge = 99

    # Class instantiator
    # NOTE: I am not requiring brake type here.
    def __init__(self, numberOfGears: int = 0, numberOfWheels: int = 2):
        # Set all our properties
        self.setnumberofgears(numberOfGears)
        self.setnumberofwheels(numberOfWheels)
        self.setbraketype("electric")

        self.setcurrentgear(1)

    # Getter for the __charge property
    def getcharge(self):
        return self.__charge

    # Setter for the __charge property
    #  Valid values are integers from 0 to 100
    def setcharge(self, charge: int) -> None:
        try:
            # Is the argument an integer?
            if int(charge):
                pass

        except Exception as e:
            raise TypeError(f"{charge} is not an integer: {e}")

        # It is an integer, is it between 0 and 100?
        if -1 < charge < 101:
            self.__charge = charge
        else:
            raise ValueError(f"{charge} is not between 0 and 100")

    # Getter for the __brakeType property
    def getbraketype(self) -> str:
        return self.__brakeType

    # Setter for the __brakeType property
    #  Valid values are integers from 0 to 15
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
