import mysql.connector


class Boss:
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname

    def add_to_db(self, db):
        db._execute_query("""
        INSERT INTO Boss (id, name, surname) VALUES ( 
        """ + str(self.id) + """ , 
        '""" + self.name + """' , 
        '""" + self.surname + "')")

    def drop_from_db(self):
        db._execute_query("""
            DELETE from Boss WHERE id='%s';
            """ % self.id)


class Employee:
    def __init__(self, id, name, surname, boss_id):
        self.id = id
        self.name = name
        self.surname = surname
        self.boss_id = str(boss_id)

    def add_to_db(self, db):
        db._execute_query("""
        INSERT INTO Employee (id, name, surname, boss_id) VALUES ( 
        """ + str(self.id) + """ , 
        '""" + self.name + """' , 
        '""" + self.surname + """' , 
        '""" + self.boss_id + "')")

    def drop_from_db(self):
        db._execute_query("""
            DELETE from Employee WHERE id='%s';
            """ % self.id)


def creating_tables(db):
    db._execute_query(create_table_boss_sql)
    db._execute_query(create_table_employee_sql)


def connect_db(host, user, password, database):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        db=database
    )


def drop_tabel_if_exists(db):
    db._execute_query("DROP TABLE IF EXISTS Employee;")
    db._execute_query("DROP TABLE IF EXISTS Boss")


def show_company(db):
    cur = db.cursor()
    cur.execute("SELECT name, surname FROM Boss WHERE id='1'")
    print("Szef:")
    for name, surname in cur.fetchall():
        print(name, surname)

    print("Pracownicy:")
    cur.execute("SELECT name, surname FROM Employee WHERE boss_id='1'")
    for name, surname in cur.fetchall():
        print(name, surname)

    cur = db.cursor()
    cur.execute("SELECT name, surname FROM Boss WHERE id='2'")
    print()
    print("Szef:")
    for name, surname in cur.fetchall():
        print(name, surname)

    print("Pracownicy:")

    cur = db.cursor()
    cur.execute("SELECT name, surname FROM Employee WHERE boss_id='2'")

    for name, surname in cur.fetchall():
        print(name, surname)

    print("-------------------------")
    print()
    print()


# Creating tables
create_table_employee_sql = """
    CREATE TABLE Employee(
        id char(3) PRIMARY KEY,
        name CHAR(20),
        surname CHAR(30),
        boss_id CHAR(3) NOT NULL,
        
        CONSTRAINT foreign_key_boss FOREIGN KEY (boss_id) REFERENCES Boss(id)
    );
    """

create_table_boss_sql = """
    CREATE TABLE Boss(
        id CHAR(3) PRIMARY KEY,
        name CHAR(20),
        surname CHAR(30)
    );
    """

db = connect_db("localhost", "kamil", "kamil", "company")
drop_tabel_if_exists(db)
creating_tables(db)

# Add some values
boss1 = Boss(1, "Marcin", "Wazny")
boss1.add_to_db(db)

boss2 = Boss(2, "Michal", "Zarzadczy")
boss2.add_to_db(db)

employee1 = Employee(1, "Lukasz", "Sredni", 1)
employee1.add_to_db(db)

employee2 = Employee(2, "Mateusz", "BardzoMaly", 1)
employee2.add_to_db(db)

employee3 = Employee(3, "Krzysztof", "Wazny", 2)
employee3.add_to_db(db)

employee4 = Employee(4, "Basia", "NieZaSzybka", 2)
employee4.add_to_db(db)


show_company(db)

employee3.drop_from_db()
employee1.drop_from_db()

print("Po zwolnieniach:")
print()

show_company(db)