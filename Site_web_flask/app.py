from flask import Flask, render_template, request

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def index():
    return render_template('questionnaire.html')

@app.route('/verifier', methods=['POST'])
def verifier():
    
    reponse1 = request.form['reponse1']
    reponse2 = request.form['reponse2']
    reponse3 = request.form['reponse3']
    reponse4 = request.form['reponse4']
    reponse5 = request.form['reponse5']

    score = 0
    if reponse1 == 'Un site internet est une collection de pages Web qui sont hébergées sur un serveur':
        score += 1
    if reponse2 == 'HTML,CSS,JS':
        score += 1
    if reponse3 == 'Hypertext Markup Language':
        score += 1
    if reponse4 == 'Cascading Style Sheets':
        score += 1
    if reponse5 == 'JavaScript':
        score += 1

    return render_template('resultat.html', score=score)

if __name__ == '__main__':
    app.run(debug=False, port=3000)
