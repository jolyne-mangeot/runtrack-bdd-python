
class Interface_viewer:
    pass

    def draw_main_interface(self):
        self.main_interface.draw_options()
    
    def draw_gestion_interface(self):
        self.gestion_interface.draw_horizontal_options()
        self.product_list.draw_list_options()