import os # On importe un outil pour lire les variables secrètes
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy # On importe l'outil de base de données

# 1. On crée le "moteur"
app = Flask(__name__)

# 2. On connecte la base de données
# On dit à l'app de trouver l'adresse secrète qu'on a mise sur Render
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app) # On initialise la base de données

# 3. On définit le "Modèle" (la structure) de notre casier
# On crée une table pour le Livre d'Or avec un id, un nom, et un message
class MessageLivreDOr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Message {self.nom}>'

# -----------------------------------------------
# ROUTE POUR L'ACCUEIL (/)
# -----------------------------------------------
@app.route("/")
def page_accueil():
    return render_template("index.html")

# -----------------------------------------------
# ROUTE POUR LES PROJETS (/projets)
# -----------------------------------------------
@app.route("/projets")
def page_projets():
    return render_template("projets.html")

# -----------------------------------------------
# ROUTE POUR LA PAGE CONTACT (/contact)
# -----------------------------------------------
@app.route("/contact")
def page_contact():
    return render_template("contact.html")

# -----------------------------------------------
# NOUVELLE ROUTE : LE LIVRE D'OR (/livredor)
# -----------------------------------------------
@app.route("/livredor", methods=["GET", "POST"])
def page_livre_dor():
    # Si le visiteur envoie le formulaire (POST)
    if request.method == "POST":
        # On récupère les données du formulaire
        nom_visiteur = request.form['nom']
        message_visiteur = request.form['message']

        # On crée un nouvel objet "Message"
        nouveau_message = MessageLivreDOr(nom=nom_visiteur, message=message_visiteur)

        # On l'ajoute au "casier" (la base de données)
        db.session.add(nouveau_message)
        db.session.commit() # On sauvegarde

        # On redirige vers la même page pour voir le message apparaître
        return redirect("/livredor")

    # Si le visiteur charge juste la page (GET)
    # On lit tous les messages du plus récent au plus ancien
    tous_les_messages = MessageLivreDOr.query.order_by(MessageLivreDOr.id.desc()).all()

    # On envoie la page HTML et la liste des messages
    return render_template("livredor.html", messages=tous_les_messages)

# -----------------------------------------------
# Lancement du moteur
# -----------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
