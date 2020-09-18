# Ken Holm
# Purpose: Demonstrate how to use a subclass
#  we created from a superclass

# Importing ElectricBike instead of Bike
# from bike import Bike
from electricbike import ElectricBike

try:
    # Instantiate our new ElectricBike
    #  Number of gears: 5
    #  Number of wheels: 3
    #  Brake type: electric

    # I must create an instance of an ElectricBike, not a Bike
    myBike = ElectricBike(5, 3)

    # Print our some bike info
    print("Our new bike")
    print(f"Gears: {myBike.getNumberOfGears()}")
    print(f"Number of Wheels: {myBike.getNumberOfWheels()}")
    print(f"Brake Type: {myBike.getBrakeType()}")
    print(f"Current Gear: {myBike.getCurrentGear()}")
    print(f"Current Charge: {myBike.getCharge()}")
    input("Continue")
    print()

    # Set our current gear to 3
    print("Setting the current gear to 3")
    myBike.setCurrentGear(3)
    print(f"Current Gear: {myBike.getCurrentGear()}")
    input("Continue")
    print()

    # Increase the gear (to 4)
    print("Increasing the current gear")
    myBike.increaseGear()
    print(f"Current Gear: {myBike.getCurrentGear()}")
    input("Continue")
    print()

    # Increase the gear, again (to the max: 5)
    print("Increasing the current gear, again")
    myBike.increaseGear()
    print(f"Current Gear: {myBike.getCurrentGear()}")
    input("Continue")
    print()

    # Increase the gear, once more, past the max
    print("Trying to go past the max gear")
    myBike.increaseGear()
    print(f"Current Gear: {myBike.getCurrentGear()}")
    print("NOTE: We do not allow that to happen")
    input("Continue")
    print()

    # Prepare to go below the minimum gear
    print("Resetting our gear to 2")
    myBike.setCurrentGear(2)
    print(f"Current Gear: {myBike.getCurrentGear()}")
    input("Continue")
    print()

    # Decrease the gear (to 1)
    print("Decreasing our current gear")
    myBike.decreaseGear()
    print(f"Current Gear: {myBike.getCurrentGear()}")
    input("Continue")
    print()

    # Try to bypass the minimum gear
    print("Trying to decrease our current gear below 1")
    myBike.decreaseGear()
    print(f"Current Gear: {myBike.getCurrentGear()}")
    print("NOTE: We do not allow that to happen")
    input("Continue")
    print()

    # Set the brake type to "electric"
    print("Trying to set the brake type to 'hand'")
    myBike.setBrakeType("hand")
    print(f"The brake type is now: {myBike.getBrakeType()}")
    print()

except Exception as e:
    print(f"Error message: {e}")
