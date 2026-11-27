from flask import Flask, jsonify, render_template, request, redirect, url_for

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
            resultat = cursor.fetchall() # ou fetchall() pour obtenir tous les résultats
            print(resultat)

        # 3. Affichage du résultat au format JSON
        return render_template('index.html' , seances=resultat)

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

@app.route('/test')
def test():

    return render_template('formulaire.html')


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


@app.route('/admin')
def admin_accueil():
    return render_template('base_admin.html', action='accueil')

@app.route('/admin/films')
def voir_films():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM film")
        films = cursor.fetchall()
    conn.close()
    return render_template('base_admin.html', action='voir_films', films=films)

@app.route('/admin/ajouter_film', methods=['GET', 'POST'])
def ajouter_film():
    if request.method == 'POST':
        titre = request.form['titre']
        duree = request.form['duree']
        interdit = 1 if 'interdit' in request.form else 0
        langue = request.form['langue']
        resume = request.form['resume']
        affiche = request.form['affiche']

        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = """INSERT INTO film (titre, duree, `interdit_-16_ans`, langue, resume, affiche) 
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (titre, duree, interdit, langue, resume, affiche))
        conn.commit()
        conn.close()

        return redirect(url_for('voir_films'))

    return render_template('base_admin.html', action='ajouter_film')


@app.route('/admin/seances')
def voir_seances():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        sql = """
            SELECT seance.id, seance.horaire, film.titre, seance.id_salle
            FROM seance
            JOIN film ON seance.id_film = film.id
            ORDER BY seance.horaire ASC
        """
        cursor.execute(sql)
        seances = cursor.fetchall()
    conn.close()
    return render_template('base_admin.html', action='voir_seances', seances=seances)


@app.route('/admin/ajouter_seance', methods=['GET', 'POST'])
def ajouter_seance():
    conn = get_db_connection()

    if request.method == 'POST':
        horaire = request.form['horaire']
        id_film = request.form['id_film']
        id_salle = request.form['id_salle']

        with conn.cursor() as cursor:
            sql = "INSERT INTO seance (horaire, id_film, id_salle) VALUES (%s, %s, %s)"
            cursor.execute(sql, (horaire, id_film, id_salle))
        conn.commit()
        conn.close()
        return redirect(url_for('voir_seances'))

    with conn.cursor() as cursor:
        cursor.execute("SELECT id, titre FROM film")
        films = cursor.fetchall()
    conn.close()

    return render_template('base_admin.html', action='ajouter_seance', films=films)


if __name__ == '__main__':
    app.run(debug=True)
