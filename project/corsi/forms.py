from time import strftime
from flask_wtf import FlaskForm
from wtforms import (
    Form,
    validators,
    StringField,
    IntegerField,
    SubmitField,
    BooleanField,
    SelectField,
    TextAreaField,
    DateField,
    SelectMultipleField
)
from sqlalchemy import desc,asc
from wtforms.validators import DataRequired, Length

from project.corsi.models import StatoCorso, LivelloCorso
from project.tags.models import Tag

'''
Corso Form
'''
class CorsiForm(FlaskForm):

    # String field: Name of the course
    name = StringField(
        "Titolo del corso",
        validators=[
            validators.Length(min=1, max=120),
            validators.required("Inserisci il nome del corso"),
        ],
    )

    # Free Text: Descrizione del corso
    description = TextAreaField("Descrizione del corso")

    # String field: Course Teacher
    teacher = StringField(
        "Insegnante/i",
        validators=[
            validators.Length(min=1, max=120),
            validators.required("Inserisci il nome dell'insegnante"),
        ],
    )

    # Livello di difficoltà del corso
    level = SelectField(
        "",
        #choices=course_level_list,
        validators=[
            validators.required("Definisci il livello di difficoltà del corso")
        ],
    )

    stato_corso = SelectField(
        "",
        #choices=stato_corso_list,
        validators=[
            validators.required("Situazione del corso")
        ],
    )

    # Free Text: Descrizione del corso
    link_materiale = StringField(
        u"Collegamento al materiale disponibile",
        validators=[Length(min=-1, max=255, message='Massimo 255 caratteri')])

    # Tags - Scelta multipla, valorizzata nell'init
    multiselect_tags = SelectMultipleField('', coerce=int)

    # Submit button
    submit = SubmitField("Conferma")

    def __init__(self, *args, **kwargs):
        super(CorsiForm, self).__init__(*args, **kwargs)
        # Caricamento scelte listbox
        self.multiselect_tags.choices = [(t.id, t.name) for t in (Tag.query.order_by(asc(Tag.name)).all())]
        self.stato_corso.choices = [(sc.value, sc.value) for sc in list(StatoCorso)]
        self.level.choices = [(l.value, l.value) for l in list(LivelloCorso)]

# Utilities functions
def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time


def write_to_disk(name, surname, email):
    data = open("file.log", "a")
    timestamp = get_time()
    data.write(
        "DateStamp={}, Name={}, Surname={}, Email={} \n".format(
            timestamp, name, surname, email
        )
    )
    data.close()