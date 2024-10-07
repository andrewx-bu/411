from typing import Any, Optional
from animal import Animal

class AnimalManager:
    def __init__(self) -> None:
        self.animals: dict[int, Animal] = {}

    def get_animal_by_id(animal_id: int) -> Optional[Animal]:
        pass

    def get_animal_details(animal_id) -> dict[str, Any]:
        pass

    def register_animal(animal: Animal) -> None:
        pass

    def remove_animal(animal_id: int) -> None:
        pass

    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass