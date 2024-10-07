from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    def __init__(self, destination: Habitat, species: str, start_location: Habitat, duration: Optional[int] = None) -> None:
        self.destination = destination
        self.species = species
        self.start_location = start_location
        self.duration = duration