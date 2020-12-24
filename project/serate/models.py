from project import db
import datetime

from project.corsi.models import Corso

# Tabella di relazione 1 Corso : N Serate
class Serata(db.Model):

    __tablename__ = "serata"

    __table_args__ = (db.UniqueConstraint("id", "data", name="constraint_serata"),)

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descrizione = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime(), nullable=False)
    link_partecipazione = db.Column(db.String(255), nullable=True)
    link_registrazione = db.Column(db.String(255), nullable=True)

    corso_id = db.Column(db.Integer(), db.ForeignKey("corso.id"))

    def __init__(
        self, nome, descrizione, data, link_partecipazione="", link_registrazione=""
    ):
        self.nome = nome
        self.descrizione = descrizione
        self.data = data
        self.link_partecipazione = link_partecipazione
        self.link_registrazione = link_registrazione

    def __repr__(self):
        return "<Descrizione '{}'. Link registrazione>".format(
            self.descrizione, self.link_registrazione
        )

    # Per la gestione API - Serializing Resources to JSON
    def to_json(self):
        json_serata = {
            "id": self.id,
            "nome": self.nome,
            "descrizione": self.descrizione,
            "data": self.data,
            "link_partecipazione": self.link_partecipazione,
            "link_registrazione": self.link_registrazione,
        }
        return json_serata

    @staticmethod
    def insert_test_serate():
        lista_serate = [
            (
                "Flask 1",
                "Introduzione a Flask e ai web server con Jinja Base",
                datetime.datetime(2020, 10, 12, hour=20),
                "",
                "https://youtu.be/QrxCia2bvC8",
            ),
            (
                "Flask 2",
                "Jinja avanzato e Forms",
                datetime.datetime(2020, 10, 19, hour=20),
                "",
                "https://youtu.be/7v39odgWmS4",
            ),
            (
                "Flask 3",
                "Flask con Database",
                datetime.datetime(2020, 10, 26, hour=20),
                "",
                "https://youtu.be/t4HoAmFiTqY",
            ),
            (
                "Flask 4",
                "Review con Andrea",
                datetime.datetime(2020, 11, 2, hour=20),
                "",
                "https://youtu.be/Ap_2Ocp_qdA",
            ),
            (
                "Flask 5",
                "Review con Mario",
                datetime.datetime(2020, 11, 9, hour=20),
                "",
                "https://youtu.be/-K3L0QkTs_4",
            ),
            (
                "Flask 6",
                "Blueprints, refactoring e tests con Mario",
                datetime.datetime(2020, 11, 16, hour=20),
                "https://zoom.us/j/99953652561?pwd=NFpGVzBJazJXOW5MMEQvNFBrVnNLUT09",
                "https://youtu.be/LNHedPR4r74",
            ),
            (
                "Flask 7",
                "Autenticazione con Mario",
                datetime.datetime(2020, 11, 23, hour=20),
                "https://zoom.us/j/95155339456?pwd=Zk1wcVViazMvdkt0SlhJZENyZ0Iydz09",
                "https://youtu.be/bwOsvfnOjVo",
            ),
            (
                "Flask 8",
                "Profili, ruoli e blog con Mario",
                datetime.datetime(2020, 11, 30, hour=20),
                "https://zoom.us/j/98250996690?pwd=UzhPUFRHUjJmdy9uWWNKUDBCak5rQT09",
                "https://youtu.be/al0kBJQzv7c",
            ),
            (
                "Flask 9",
                "Config, Heroku e Docker: deploy in produzione con Andrea",
                datetime.datetime(2020, 12, 7, hour=20),
                "https://zoom.us/j/98193137080?pwd=bWFEVm9obEZNc2Rjb2tqSXhTS0xkQT09",
                "https://youtu.be/1Tf8bt_oE7I",
            ),
            (
                "Flask 10",
                "REST API con Mario",
                datetime.datetime(2020, 12, 14, hour=20),
                "https://zoom.us/j/95665293446?pwd=QWZIaEJ2VTNtRCszc0ZLcy9FKzJHdz09",
                "https://youtu.be/RcNbXuHovXs",
            ),
        ]
        corso_flask = Corso.query.filter_by(nome="Flask").first()
        for serata in lista_serate:
            serata_db = Serata.query.filter_by(nome=serata[0]).first()
            if serata_db is None:
                serata_db = Serata(*serata)
                serata_db.corso_id = corso_flask.id
                db.session.add(serata_db)
            db.session.commit()