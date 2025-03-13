
from interface_controller import Interface_controller
from interface_model import Interface_model

Control = Interface_controller()
Control.init_config()
Control.setup_states(Interface_model())
Control.main_loop()