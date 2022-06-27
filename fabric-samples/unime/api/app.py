from config_app import app
from config_db import db
from flask_sqlalchemy import SQLAlchemy
from blueprints.studente import studente_bp
from blueprints.corso import corso_bp
from blueprints.personale import personale_bp
from blueprints.categoria import categoria_bp
from blueprints.titolo import titolo_bp
from blueprints.evento import evento_bp
from blueprints.tipologia import tipologia_bp
from blueprints.partecipazione import partecipazione_bp
from blueprints.dipartimento import dipartimento_bp
from blueprints.universita import universita_bp
from blueprints.citta import citta_bp
from blueprints.nazione import nazione_bp
from blueprints.promotore import promotore_bp
from blueprints.ente import ente_bp

app.register_blueprint(studente_bp)
app.register_blueprint(corso_bp)
app.register_blueprint(personale_bp)
app.register_blueprint(categoria_bp)
app.register_blueprint(titolo_bp)
app.register_blueprint(evento_bp)
app.register_blueprint(ente_bp)
app.register_blueprint(tipologia_bp)
app.register_blueprint(partecipazione_bp)
app.register_blueprint(dipartimento_bp)
app.register_blueprint(universita_bp)
app.register_blueprint(citta_bp)
app.register_blueprint(nazione_bp)
app.register_blueprint(promotore_bp)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)