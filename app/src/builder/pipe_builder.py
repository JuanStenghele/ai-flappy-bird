from src.obj.pipe import Pipe
from src.obj.obj_manager import ObjectManager
from src.obj.pygame_obj_manager import PygameObjectManager
from src.display.pipe_drawer import PipeDrawer


# Class in charge of building a pipe
class PipeBuilder:
    def __init__(self, obj_manager: ObjectManager, pg_obj_manager: PygameObjectManager) -> None:
        self.obj_manager = obj_manager
        self.pg_obj_manager = pg_obj_manager

    # Build a pipe
    def build(self, x: float) -> Pipe:
        pipe = Pipe(x)
        self.obj_manager.add_pipe(pipe)
        drawer = PipeDrawer(pipe)
        self.pg_obj_manager.add_pipe_drawer(drawer)
        return pipe
