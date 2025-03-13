import pygame as pg

class List_menu_model():
    def __init__(self, screen, width, height, options, next_list, back):
        self.screen = screen
        self.from_left, self.from_top = (width/2, height/2)
        self.spacer = width/6

        self.deselected_color = (0,0,0)
        self.selected_color = (0,255,0)

        self.options = options
        self.next_list = next_list
        self.back = back
        self.selected_index = 0

        pg.font.init()
        self.deselected_font = pg.font.SysFont("Arial", 32)
        self.selected_font = pg.font.SysFont("Arial", 32, True)

        self.pre_render()

    def pre_render(self):
        """
            Pre-renders the options in three states :
            deselected, and selected.
        """
        self.rendered = {"deselected":[], "selected":[]}

        for option in self.options:
            deselected_render = self.deselected_font.render(
                option, True, self.deselected_color
            )
            deselected_rect = deselected_render.get_rect()
            selected_render = self.selected_font.render(
                option, True, self.selected_color
            )
            selected_rect = selected_render.get_rect()
            self.rendered["deselected"].append(
                (deselected_render, deselected_rect)
            )
            self.rendered["selected"].append(
                (selected_render, selected_rect)
            )
    
    def draw_options(self):
        """
            for all launch_menu states, enumerate buttons and places them before
            checking for selected index button to place it on the same position
        """
        for index, option in enumerate(self.rendered["deselected"]):
            option[1].center = (self.from_left, self.from_top + index*self.spacer)
            if index == self.selected_index:
                selected_render = self.rendered["selected"][index]
                selected_render[1].midbottom = option[1].midbottom
                self.screen.blit(selected_render[0], selected_render[1])
            else:
                self.screen.blit(option[0],option[1])
    
    def get_event_options(self, event):
        """
            Processes vertical movement (up and down) in the menu based on key events.
        """
        if event.type == pg.KEYDOWN:
            if pg.key.name(event.key) in ["z","up"]:
                self.change_selected_option(-1)
                while self.options[self.selected_index] == "":
                    self.change_selected_option(-1)
            elif pg.key.name(event.key) in ["s","down"]:
                self.change_selected_option(1)
                while self.options[self.selected_index] == "":
                    self.change_selected_option(1)
    
    def change_selected_option(self, operant):
        """
            for keyboard behaviour, change based on operant the selected
            option : single direction for now (up or down)
        """
        self.selected_index += operant
        max_indicator = len(self.rendered["deselected"]) - 1
        if self.selected_index < 0:
            self.selected_index = max_indicator
        elif self.selected_index > max_indicator:
            self.selected_index = 0