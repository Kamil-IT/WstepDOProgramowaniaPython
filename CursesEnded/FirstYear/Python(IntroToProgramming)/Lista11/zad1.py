import dbm

# Open database or create if not exists
with dbm.open('cache', 'c') as db:

    # Add some value to db
    db[b'hello'] = b'Welcome in database'
    db['name_constructor'] = 'Kamil'
    db['id_constructor'] = '254331'

    # Read value from db
    print(bytes.decode(db.get('hello')))
    print(bytes.decode(db.get('name_constructor')))
    print(bytes.decode(db.get('hello', None)))