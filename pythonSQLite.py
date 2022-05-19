import sqlite3

try:
    conn = sqlite3.connect("library_management.db")
    cursor = conn.cursor()

    ### Creating tables
    
    # cursor.execute("""create table books ( 
    #                         id integer primary key, 
    #                         title text, 
    #                         author text, 
    #                         category text,
    #                         edition text, 
    #                         publication_year integer,
    #                         available int )""")

    ### Inserting data to books table

    # cursor.execute("""INSERT INTO books VALUES (
    #                   2070384853, 
    #                   'The Picture of Dorian Gray', 
    #                   'Oscar Wilde',
    #                   'Novel',
    #                   'Folio Classique',
    #                   1891,
    #                   0)""")
    
    # cursor.execute("""INSERT INTO books VALUES (
    #                   2723451003, 
    #                   'Berserk T10', 
    #                   'Kentaro Miura',
    #                   'Manga',
    #                   'Glénat',
    #                   2005,
    #                   1)""")

    # cursor.execute("""INSERT INTO books VALUES
    #                   (1508566593, 
    #                   'Fretboard THEORY Volume I', 
    #                   'Desi Serna',
    #                   'Educational',
    #                   'CreateSpace Independent Publishing Platform',
    #                   2015,
    #                   1),
                     
    #                   (1508928746, 
    #                   'Fretboard THEORY Volume II', 
    #                   'Desi Serna',
    #                   'Educational',
    #                   'CreateSpace Independent Publishing Platform',
    #                   2015,
    #                   0)""")



    conn.commit()

except Exception as e:
    print("ERROR", e)
    conn.rollback()

finally:
    conn.close()







