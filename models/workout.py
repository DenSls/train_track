from typing import List
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from models.workout_exercise import WorkoutExercise


class Workout(Base):
    __tablename__ = 'workouts'

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('users.id',)
    )
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    # Связи.
    exercise_associations: Mapped[List["WorkoutExercise"]] = relationship(
        "WorkoutExercise",
        back_populates='workout',
    )
