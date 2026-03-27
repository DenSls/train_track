from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

if TYPE_CHECKING:
    from models.workout import Workout
    from models.exercise import Exercise


class WorkoutExercise(Base):
    __tablename__ = 'workout_exercise_association'

    workout_id: Mapped[int] = mapped_column(ForeignKey("workouts.id"))
    exercise_id: Mapped[int] = mapped_column(ForeignKey("exercises.id"))

    # Связи.
    exercise: Mapped["Exercise"] = relationship(
        "Exercise",
        back_populates='workout_associations',
    )
    workout: Mapped["Workout"] = relationship(
        "Workout",
        back_populates='exercise_associations',
    )

    sets: Mapped[int] = mapped_column(Integer)
    reps: Mapped[int] = mapped_column(Integer)
    weight: Mapped[float] = mapped_column(Float)
