import random

from enum import Enum

from environ.resources.air import AirTypes

class ReproType(Enum):
    ASEXUAL = 1
    SEXUAL = 2
    ITS_COMPLICATED = 3

class Creature():
    reproduction_rate: float
    reproduction_type: ReproType
    food_consumption_rate: float
    air_consumption_rate: float
    air_production_rate: float
    air_in_type: AirTypes
    air_out_type: AirTypes

    x: int
    y: int

    def __init__(self):
        self.reproduction_rate = 1/365
        self.reproduction_type = ReproType.SEXUAL
        self.food_consumption_rate = 2250  # calories per day
        self.air_consumption_rate = 145  # gallons per day
        self.air_production_rate = 132  # gallons/day
        self.air_in_type = AirTypes.OXYGEN
        self.air_out_type = AirTypes.CARBON_DIOXIDE
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def update(self, world):
        # update self state


        # update world state
