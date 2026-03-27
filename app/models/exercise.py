from typing import Optional, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.workout_exercise import WorkoutExercise


class Exercise(Base):
    __tablename__ = 'exercises'

    name: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )
    description: Mapped[Optional[str]] = mapped_column(
        String,
    )
    category: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )
    muscle_group: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    # Связи.
    workout_associations: Mapped[List["WorkoutExercise"]] = relationship(
        "WorkoutExercise",
        back_populates='exercise',
    )
