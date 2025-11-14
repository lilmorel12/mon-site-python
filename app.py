# 1. On IMPORTE "request" pour pouvoir lire les données du formulaire
from flask import Flask, render_template, request

# 2. On crée le "moteur"
app = Flask(__name__)

# -----------------------------------------------
# ROUTE POUR L'ACCUEIL
# -----------------------------------------------
@app.route("/")
def page_accueil():
    # Il va chercher "index.html" dans le dossier "templates"
    return render_template("index.html")

# -----------------------------------------------
# ROUTE POUR LES PROJETS
# -----------------------------------------------
@app.route("/projets")
def page_projets():
    return render_template("projets.html")
    
# -----------------------------------------------
# ROUTE POUR LA PAGE CONTACT (Celle qui AFFICHE le formulaire)
# -----------------------------------------------
@app.route("/contact")
def page_contact():
    return render_template("contact.html")
    
# -----------------------------------------------
# NOUVELLE ROUTE ! (Celle qui REÇOIT le formulaire)
# -----------------------------------------------
# Cette fonction ne s'exécute que quand des données sont ENVOYÉES (methods=["POST"])
@app.route("/submit-contact", methods=["POST"])
def recevoir_formulaire():
    
    # On attrape les données du formulaire
    # Les noms ('nom', 'email', 'message') doivent être les MÊMES
    # que les attributs "name=..." dans ton HTML
    nom = request.form['nom']
    email = request.form['email']
    message = request.form['message']
    
    # LA PREUVE : On affiche les données dans notre terminal (la fenêtre noire)
    print("--- NOUVEAU MESSAGE REÇU ---")
    print(f"Nom: {nom}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    print("------------------------------")
    
    # On renvoie un simple message de remerciement à l'utilisateur
    return "Merci ! Votre message a été reçu par le serveur Python."
    

# -----------------------------------------------
# Lancement du moteur
# -----------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)