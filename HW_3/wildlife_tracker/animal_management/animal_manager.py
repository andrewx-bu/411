from typing import Any, Optional
from animal import Animal

# WORKS
class AnimalManager:
    def __init__(self) -> None:
        animals: dict[int, Animal] = {}

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        pass

    def register_animal(Animal) -> None:
        pass

    def remove_animal(animal_id: int) -> None:
        pass

    def get_animal_details(animal_id) -> dict[str, Any]:
        pass

    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass