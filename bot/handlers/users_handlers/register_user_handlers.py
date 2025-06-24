from .default_handlers import register_default_handlers
from .random_muscle_handlers import register_random_muscle_handlers
from .muscles_movement_handlers import register_muscles_movement_handlers


def register_user_handlers(dp):
    register_default_handlers(dp)
    register_random_muscle_handlers(dp)
    register_muscles_movement_handlers(dp)
