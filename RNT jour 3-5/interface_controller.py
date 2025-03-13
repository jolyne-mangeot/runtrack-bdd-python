import pygame as pg
import random

class Interface_controller:
    """
        Control class manages game states, settings, and event loops.
        It extends Settings and initializes essential configurations for the game.
    """
    @classmethod
    def init_config(cls):
        """
            Initialize configuration settings such as screen resolution, 
            Pygame display, and clock.
        """
        cls.done : bool = False
        cls.width, cls.height = (640,480)
        cls.screen = pg.display.set_mode(
            (cls.width, cls.height)
        )
        cls.clock = pg.time.Clock()

    def setup_states(self, interface_state):
        """
            recover state dictionary and initialize first state
            based on given parameters ("title_menu" and such)
        """
        self.state : object = interface_state
        self.state.startup()
    
    def update(self):
        """
            check for state done status to either quit the script loop
            or initialize a new state with flip_state
        """
        if self.state.quit:
            self.done = True
        self.screen.fill((255,255,255))
        self.state.update()
    
    def event_loop(self):
        """
            main loop for pygame events which initializes the current state's
            event loop as well
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.KEYDOWN:
                if pg.key.name(event.key) in ["escape"]:
                    back_scene = self.state.interface_scenes_objects[self.state.scene].back
                    if back_scene != "quit":
                        self.state.scene = back_scene
                    else:
                        self.done = True
                self.state.interface_scenes_events[self.state.scene](event)
                self.state.interface_scenes_objects[self.state.scene].get_event_options(event)
    
    def main_loop(self):
        """
            access all essential methods to run game loop based on clock ticks
            with event_loop, which launches on the control class scope before
            the current state one, update for each class level as well before
            updating the pygame display
        """
        while not self.done:
            self.delta_time =\
                self.clock.tick(30) / 1000
            self.event_loop()
            self.update()
            pg.display.update()
        pg.quit()
    
    def get_event_main_interface(self, event):
        if pg.key.name(event.key) in ["return"]:
            next_scene = self.interface_scenes_objects[self.scene].next_list[self.interface_scenes_objects[self.scene].selected_index]
            if next_scene != "quit":
                self.scene = next_scene
            else:
                self.done = True

    def get_event_gestion_interface(self, event):
        self.gestion_interface.get_event_horizontal(event)