from typing import Annotated
from pydantic import BaseModel, Field


# Definiere ein Modell für ein Intervall
class Interval(BaseModel):
    start: Annotated[int, Field(ge=0)]  # Start muss eine nicht-negative Ganzzahl sein
    end: Annotated[
        int, Field(ge=0)
    ]  # End muss ebenfalls eine nicht-negative Ganzzahl sein

    # Sicherstellen, dass das Ende nicht vor dem Start liegt
    def __init__(self, **data):
        super().__init__(**data)
        if self.start > self.end:
            raise ValueError(
                f"Endpunkt {self.end} darf nicht kleiner sein als Startpunkt {self.start}."
            )
