import mysql.connector

from interface_controller import Interface_controller
from interface_views import Interface_viewer
from list_menu_model import List_menu_model

class Interface_model(
    Interface_controller,
    Interface_viewer):
    def __init__(self):
        self.init_interface_scenes_objects()
        self.init_interface_scenes()
        self.scene = "main_interface"
        self.quit = False
    
    def startup(self):
        pass

    def update(self):
        self.interface_scenes_draw[self.scene]()
        # self.interface_scenes_objects[self.scene].draw_options()

    def init_interface_scenes_objects(self):
        self.main_interface : object = List_menu_model(
            self.screen,
            self.width, self.height,
            ["Gestion", "Quitter"], "quit",
            ["gestion_interface", "quit"],
        )
        self.gestion_interface : object = List_menu_model(
            self.screen,
            self.width, self.height*1.5,
            ["Ajout", "Modification", "Suppression"], "main_interface",
            ["add_product_interface", "alter_product_interface", "delete_product_interface"]
        )
        self.product_list : object = List_menu_model(
            self.screen,
            self.width, self.height,
            self.recover_product_list(), "quit"
        )

    def init_interface_scenes(self):
        self.interface_scenes_draw : dict = {
            "main_interface" : self.draw_main_interface,
            "gestion_interface" : self.draw_gestion_interface,
        }
        self.interface_scenes_events : dict = {
            "main_interface" : self.get_event_main_interface,
            "gestion_interface" : self.get_event_gestion_interface,
        }
        self.interface_scenes_objects : dict = {
            "main_interface" : self.main_interface,
            "gestion_interface" : self.product_list,
        }

    @staticmethod
    def connect_to_database():
        return mysql.connector.connect(
            user='python',
            host='localhost',
            password='python123456',
            database='python_store_database'
        )

    def recover_product_list(self):
        database = self.connect_to_database()
        database_cursor = database.cursor()
        database_cursor.execute("SELECT * FROM product")
        return database_cursor.fetchall()
