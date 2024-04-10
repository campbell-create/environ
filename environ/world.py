from enum import Enum
from typing import List

from environ.resources.air import AirTypes
from environ.creatures.base_creature import Creature
from environ.creatures.plant import Plant


class Season(Enum):
    SPRING = 45  # also functions as the days of the year that the seasons turn
    SUMMER = 136
    FALL = 181
    WINTER = 226


class World():

    def __init__(self):
        self.season = Season.SPRING
        self.day = 45  # beginning of spring
        self.generate_resources()

        self.creatures: List[Creature] = []
        self.generate_creatures()

    def generate_resources(self):
        self.airs = {
            air: random.randint(10e1000, 10e10000) for air in AirTypes
        }

    def generate_creatures(self):
        self.creatures.append(Plant())
        self.creatures.append(Creature())

    def update(self):  # update 1x/day
        for creature in self.creatures:
            creature.update(self)  # provide self as state

    def print(self):
        ra = [[0]*10]*10
        for creature in self.creatures:


    def run(self):
        command = input()
        while command != "q":
            self.update()
            self.print()
