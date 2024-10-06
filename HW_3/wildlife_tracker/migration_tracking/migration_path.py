from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    def __init__(self, current_date: str, current_location: str, destination: Habitat, species: str, start_date: str, start_location: Habitat, duration: Optional[int] = None) -> None:
        self.current_date = current_date
        self.current_location = current_location
        self.destination = destination
        self.species = species
        self.start_date = start_date
        self.start_location = start_location
        self.duration = duration