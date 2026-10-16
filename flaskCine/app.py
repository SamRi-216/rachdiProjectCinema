from flask import Flask, jsonify
import pymysql

from config import Config
app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
        )

# Route unique pour la page d'accueil
@app.route('/')
def home():
    connection = None
    try:
        # 1. Connexion à la base
        connection = get_db_connection()

        # 2. Exécution de la requête SQL
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM seance WHERE horaire >= NOW();")
            resultat = cursor.fetchone() # ou fetchall() pour obtenir tous les résultats

        # 3. Affichage du résultat au format JSON
        return jsonify({
            "statut": "succès",
            "message": "Connexion BDD réussie !",
            "donnees": resultat
    }), 200
    except pymysql.MySQLError as error:
        # En cas d'erreur de connexion ou SQL
        return jsonify({
            "statut": "erreur",
            "message": f"Impossible de se connecter : {str(error)}"
        }), 500
    finally:
        # 4. Fermeture obligatoire de la connexion
        if connection and connection.open:
            connection.close()
if __name__ == '__main__':
    app.run(debug=True)