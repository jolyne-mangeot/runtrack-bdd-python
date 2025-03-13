import mysql.connector

def database_connection():
    return mysql.connector.connect(
        user='python',
        host='localhost',
        password='python123456',
        database='python_mysql_runtrack'
    )

def add_cage(database):
    superficie = input("Superficie : ")
    capacite = input("Capacité : ")
    database.cursor().execute("insert into cage (superficie, capacite) values(%s,%s)", (superficie, capacite))

def add_animal(database):
    
    pass

def erase_animal(database):
    pass

def modify_animal(database):
    pass

def display_animals(database):
    pass

def display_cages_surface(database):
    pass

def leave_program(none):
    exit()

def main():
    managament_dict : dict = {
        1 : add_cage,
        2 : add_animal,
        3 : erase_animal,
        4 : modify_animal,
        5 : display_animals,
        6 : display_cages_surface,
        7 : leave_program
    }
    done = False
    while not done:
        print(
            f"- - - - - - Database management - - - - - -",
            f"1. Ajouter une cage",
            f"2. Ajouter un animal",
            f"3. Supprimer un animal",
            f"4. Modifier un animal",
            f"5. Afficher les animaux",
            f"6. Calculer la supperficie des cages",
            f"7. Quitter",
            sep="\n"
        )
        input_done = False
        while not input_done:
            user_input = input("Choisissez une option (1-7) : ")
            try:
                user_input = int(user_input)
                input_done = True
            except Exception:
                print(f"Entrée incorrecte, réessayez")
                continue
        if 1 <= user_input <= 7:
            database = database_connection()
            managament_dict[user_input](database)
            database.commit()
            database.close()
        else:
            print(f"Entrée incorrecte, réessayez")
            continue

main()