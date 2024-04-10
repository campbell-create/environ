import random
from enum import Enum

from environ.creatures.base_creature import Creature
from environ.world import World, Season

class Stage(Enum):
    FLOWERING = 1
    FRUITING = 2
    DORMANT = 3



class Plant(Creature):
    def __init__(self):
        self.reproduction_rate = 100/365
        self.reproduction_type = ReproType.SEXUAL
        self.food_consumption_rate = 0  # eventually need to add soil requirements
        self.air_consumption_rate = 3140/365  # gallons/day
        self.air_production_rate = 1320  # gallons/day
        self.air_in_type = AirTypes.CARBON_DIOXIDE
        self.air_out_type = AirTypes.OXYGEN
        self.production = 0
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def update(self, world: World):
        # update self state
        if world.season == Season.SPRING:
            self.state = Stage.FLOWERING
        if world.season == Season.SUMMER:
            self.state = Stage.FRUITING
            self.production = 4  # pounds / day
        if world.season == Season.FALL:
            self.state = Stage.FRUITING
            self.production = 8  # pounds / day
        else:
            self.state = Stage.DORMANT

        if self.state == Stage.FRUITING:
            self.food_amount += self.production

        # update world state
        kwargs = {
            self.air_in_type: -self.air_consumption_rate,
            self.air_out_type: self.air_production_rate,
        }

        world.update_atmo(**kwargs)
    
    def get_eaten(self, amount):
        self.food_amount -= amount
        if self.food_amount < 0:
            unfed = self.food_amount
            self.food_amount = 0
            return unfed
        return 0
