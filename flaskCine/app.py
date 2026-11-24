from flask import Flask, jsonify, render_template
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
    def home(id_film):
        connection = None
        try:
            # 1. Connexion à la base
            connection = get_db_connection()

            # 2. Exécution de la requête SQL
            with connection.cursor() as cursor:
                requete = "SELECT * FROM film WHERE id = %s;"

                valeurs = (id_film,)
                cursor.execute(requete, valeurs)
                resultat = cursor.fetchone()  # ou fetchall() pour obtenir tous les résultats



        finally:
            # 4. Fermeture obligatoire de la connexion
            if connection and connection.open:
                connection.close()
            return render_template('film.html', home=resultat)


@app.route('/test')
def test():
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


@app.route('/film/<id_film>')
def film(id_film):
    connection = None
    try:
        # 1. Connexion à la base
        connection = get_db_connection()


        # 2. Exécution de la requête SQL
        with connection.cursor() as cursor:
            requete= "SELECT * FROM film WHERE id = %s;"

            valeurs = (id_film,)
            cursor.execute(requete, valeurs)
            resultat = cursor.fetchone()  # ou fetchall() pour obtenir tous les résultats



    finally:
        # 4. Fermeture obligatoire de la connexion
        if connection and connection.open:
            connection.close()
        return render_template('film.html' , film=resultat)


@app.route('/getseances/<int:numSalle>', methods=['GET'])
def getseances(numSalle):
    connection = None
    try:
        # 1. Connexion à la base via votre fonction existante
        connection = get_db_connection()

        # 2. Exécution de la requête SQL
        with connection.cursor() as cursor:
            query = """ 
                        SELECT f.titre AS titre,
                        DATE_FORMAT(se.horaire, '%%Y-%%m-%%d %%H:%%i') AS horaire, f.langue  AS version,f.`interdit_-16_ans`  AS interdiction_16 
                        FROM seance se
                        JOIN film f ON se.id_film = f.id
                        JOIN salle sa ON se.id_salle = sa.id
                        WHERE sa.numero_salle = %s
            """
            print ( query, numSalle)
            cursor.execute(query, (numSalle,))
            seances_salle = cursor.fetchall()

        # 3. Renvoie uniquement la liste JSON des séances
        return jsonify(seances_salle), 200

    except pymysql.MySQLError as error:
        return jsonify({
            "statut": "erreur",
            "message": f"Erreur base de données : {str(error)}"
        }), 500

    finally:
        # 4. Fermeture propre de la connexion
        if connection and connection.open:
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
