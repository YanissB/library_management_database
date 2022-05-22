import mysql.connector

try:


    ### Connection to MySQL Server and "library_management_db" ###
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "password",
        database = "library_management_db" 
    )

    cursor = mydb.cursor()

    
    ### Create library_management_db ###

    # cursor.execute("CREATE DATABASE library_management_db")

    
    ### Create tables ###
    
    ## books table
    # cursor.execute("""create table books ( 
    #                     id INTEGER PRIMARY KEY NOT NULL, 
    #                     title VARCHAR(255) NOT NULL,
    #                     edition VARCHAR(255), 
    #                     publication_year DATE,
    #                     copie_owned INTEGER NOT NULL)""")

    ## author table
    # cursor.execute("""CREATE TABLE authors ( 
    #                     id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, 
    #                     first_name VARCHAR(255) NOT NULL,
    #                     last_name VARCHAR(255))""") 

    ### Insert data to tables
    
    ## => books
    # cursor.execute("""INSERT INTO books VALUES (
    #                   2070384853, 
    #                   'The Picture of Dorian Gray', 
    #                   'Novel',
    #                   'Folio Classique',
    #                   1891,
    #                   0)""")
    
    # cursor.execute("""INSERT INTO books VALUES (
    #                   2723451003, 
    #                   'Berserk T10', 
    #                   'Manga',
    #                   'Glénat',
    #                   2005,
    #                   1)""")

    # cursor.execute("""INSERT INTO books VALUES
    #                   (1508566593, 
    #                   'Fretboard THEORY Volume I',
    #                   'Educational',
    #                   'CreateSpace Independent Publishing Platform',
    #                   2015,
    #                   1),
                     
    #                   (1508928746, 
    #                   'Fretboard THEORY Volume II',
    #                   'Educational',
    #                   'CreateSpace Independent Publishing Platform',
    #                   2015,
    #                   0)""")

    ## => author

    # cursor.execute(""" INSERT INTO author (first_name, last_name) 
    #                    VALUES ('Oscar',
    #                            'Wilde')""")
    
    # cursor.execute(""" INSERT INTO author (first_name, last_name) 
    #                    VALUES ('Kentaro',
    #                            'Miura'),

    #                           ('Deni',
    #                            'Serna')""")

    mydb.commit()
    print("DB Updated !")
except Exception as e:
    
    print("ERROR", e)
    mydb.rollback()

finally:
    mydb.close()







