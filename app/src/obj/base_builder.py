from src.obj.base import Base
from src.obj.obj_manager import ObjectManager
from src.obj.pygame_obj_manager import PygameObjectManager
from src.display.base_drawer import BaseDrawer


# Class in charge of building a base
class BaseBuilder:
    def __init__(self, obj_manager: ObjectManager, pg_obj_manager: PygameObjectManager) -> None:
        self.obj_manager = obj_manager
        self.pg_obj_manager = pg_obj_manager

    # Build a base
    def build(self, y: float) -> Base:
        base = Base(y)
        self.obj_manager.set_base(base)
        drawer = BaseDrawer(base)
        self.pg_obj_manager.set_base_drawer(drawer)
        return base
