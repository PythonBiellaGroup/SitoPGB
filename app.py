"""
Per eseguire:

set FLASK_APP=app.py
set FLASK_DEBUG=true
flask run

oppure

python app.py

Per cambiare configurazione da ambiente:
set FLASK_CONFIG=...

"""

import os
from project import create_app, db
from flask import render_template
from flask_migrate import Migrate


app = create_app()

# Create db and migrations
Migrate(app, db)

"""
Per "navigare" in modalità shell
Use shell_context_processor() to add other automatic imports.
"""


@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,
        Tag=Tag,
        Corso=Corso,
        Serata=Serata,
        Ruolo=Ruolo,
        Utente=Utente,
        Post=Post,
        Comment=Comment,
    )


"""
Per i test di unità automatici, il decorator
app.cli.command permette di creare comandi "custom".
Il nome della funzione "decorata", in questo caso "test" sarà il comando per richiamarla.
In questo caso l'implementazione di test() invoca il test runner del package unittest.

Quindi per lanciare i test automatici:

set FLASK_APP=app.py
flask test

"""


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest

    # tests è il modulo
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command("create_db")
def create_db():

    print("Start creating db")

    from project.serate.models import Serata
    from project.corsi.models import Corso
    from project.tags.models import Tag
    from project.ruoli.models import Ruolo
    from project.utenti.models import Utente
    from project.blog.models import Post
    from project.commenti.models import Comment

    from random import randint
    from faker import Faker

    try:
        user_list = Utente.query.all()
        course_list = Corso.query.all()
        post_list = Post.query.all()
        comment_list = Comment.query.all()
        post_list = Post.query.all()
        ruolo_list = Ruolo.query.all()
        print("DB Tables already exists")

    except Exception as message:
        print(f"No db data exist, inserting them:")
        # Utilizzo dell'application factory
        # app = create_app("development")
        # app_context = app.app_context()
        # app_context.push()
        def users(count=100):
            fake = Faker("it_IT")
            i = 0
            while i < count:
                u = Utente(
                    email=fake.email(),
                    username=fake.user_name(),
                    password="password",
                    confirmed=True,
                    name=fake.name(),
                    location=fake.city(),
                    about_me=fake.text(),
                    member_since=fake.past_date(),
                )
                db.session.add(u)
                try:
                    db.session.commit()
                    i += 1
                except IntegrityError:
                    db.session.rollback()

        def posts(count=100):
            fake = Faker("it_IT")
            user_count = Utente.query.count()
            for i in range(count):
                u = Utente.query.offset(randint(0, user_count - 1)).first()
                p = Post(body=fake.text(), timestamp=fake.past_date(), author=u)
                db.session.add(p)
                db.session.commit()

        def comments(count=100):
            fake = Faker("it_IT")
            user_count = Utente.query.count()
            post_count = Post.query.count()
            for i in range(count):
                u = Utente.query.offset(randint(0, user_count - 1)).first()
                p = Post.query.offset(randint(0, post_count - 1)).first()
                c = Comment(
                    body=fake.text(), timestamp=fake.past_date(), post=p, author=u
                )
                db.session.add(c)
                db.session.commit()

        print("Creating structure")
        db.create_all()
        db.session.commit()

        print("Creating roles")
        Ruolo.insert_roles()

        print("Creating fake users")
        users(3)

        print("Creating test users")
        Utente.insert_test_users()

        print("Creating tags")
        Tag.insert_test_tags()

        print("Creating corsi")
        Corso.insert_test_corsi()

        print("Creating serate")
        Serata.insert_test_serate()

        print("Creating posts fake")
        posts(3)

        print("Creating commenti fake")
        comments(3)

        print("\nDB Dummy data inserted succesfully")


"""
Prova "flask pippo" :-)
"""


@app.cli.command()
def pippo():
    print("Bravo! Hai capito come funziona il decorator cli di flask")


if __name__ == "__main__":
    app.run()