import flask

app = flask.Flask(__name__)

class Person:
    def __init__(self, name, lastname, age, gender):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.gender = gender

# Lista przechowująca obiekty klasy Person
people_list = []

@app.route('/')
def home():
    return flask.render_template("str.html")

@app.route('/add/<name>/<lastname>/<age>/<gender>', methods=['POST'])
def add_person(name, lastname, age, gender):
    # Tworzenie nowego obiektu Person i dodanie go do listy
    new_person = Person(name, lastname, age, gender)
    people_list.append(new_person)

    # Dodanie informacji o osobie do pliku bazy
    with open('db/base.csv', 'a') as f:
        f.write(f'{name};{lastname};{age};{gender}\n')

    return ''

@app.route('/list')
def list_people():
    list_lines = ''
    for person in people_list:
        list_lines += f'<li>{person.name} {person.lastname} {person.age} {person.gender} <button data-action="edit" data-id="{person.name};{person.lastname}">Edytuj</button> <button data-action="del" data-id="{person.name};{person.lastname}">Usuń</button> </li>'
    return flask.render_template("list.html", list_values=list_lines)

@app.route('/del/<name>/<lastname>', methods=['POST'])
def delete_person(name, lastname):
    for person in people_list:
        if person.name == name and person.lastname == lastname:
            people_list.remove(person)

    # Zapisanie aktualnej listy osób do pliku bazy
    with open('db/base.csv', 'w') as f:
        for person in people_list:
            f.write(f'{person.name};{person.lastname};{person.age};{person.gender}\n')

    return list_people()

@app.route('/edit/<name>/<lastname>', methods=['POST'])
def edit_form(name, lastname):
    person = next((p for p in people_list if p.name == name and p.lastname == lastname), None)
    if person:
        return flask.render_template("edit.html", name=person.name, lastname=person.lastname, age=person.age, gender=person.gender)
    else:
        return "Person not found"

@app.route('/updatedb/<edit>/<name>/<lastname>/<age>/<gender>', methods=['POST'])
def update_db(edit, name, lastname, age, gender):
    edited_person = next((p for p in people_list if f'{p.name};{p.lastname}' == edit), None)
    if edited_person:
        edited_person.name = name
        edited_person.lastname = lastname
        edited_person.age = age
        edited_person.gender = gender

        # Zapisanie aktualnej listy osób do pliku bazy
        with open('db/base.csv', 'w') as f:
            for person in people_list:
                f.write(f'{person.name};{person.lastname};{person.age};{person.gender}\n')

        return list_people()
    else:
        return "Person not found"
