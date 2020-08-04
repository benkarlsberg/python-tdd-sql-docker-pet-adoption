from pet import Pet
import sqlite3

def db_insert(pet):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()
    sql = "INSERT INTO pets (name, species, age, sex) values ('{}', '{}', {}, '{}')".format(
        pet.name, pet.species, pet.age, pet.sex)
    c.execute(sql)
    conn.commit()
    conn.close()

while True:
    response = input("(e)nter a pet, open a (f)ile, or (q)uit: ")
    print(response)
    if response == 'q':
        break

    if response == 'e':
        name = input("name: ")
        species = input("species: ")
        age = input("age: ")
        sex = input("sex: ")
        p = Pet(name, species, age, sex)
        print('pet:', p)
        db_insert(p) # adds pet to database using function above

    if response == 'f':
        file = input("filename: ")
        with open(file) as f:
            for line in f:
                name, species, age, sex = line.strip().split(',')
                p = Pet(name, species, age, sex)
                print("p: ", p)
                db_insert(p) # adds pet to database using function above