import dbm

# Open database or create if not exists
with dbm.open('cache', 'c') as db:

    # Add some value to db
    db[b'hello'] = b'Welcome in database'
    db['name_constructor'] = 'Kamil'
    db['id_constructor'] = '254331'

    # Read value from db
    print(db.get('hello'))
    print(db.get('name_constructor'))
    print(db.get('id_constructor'))