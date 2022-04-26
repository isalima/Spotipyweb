import webbrowser

from flask import Flask, render_template, request
import dados


app = Flask(__name__)

# if __name__ == '__main__':
#     app.run(debug=True)


@app.route('/')
def index():
    musics = dados.get_dados('beyonce')
    return render_template('index.html',  listaMusic=musics)


@app.route('/search', methods=['GET', 'POST'])
def search():
    nameArtist = request.form.get('search')
    musics = dados.get_dados(nameArtist)
    return render_template('index.html', listaMusic=musics)


@app.route('/play')
def play():
    # webbrowser.open("https://open.spotify.com/track/3yfqSUWxFvZELEM4PmlwIR")
    return render_template('index.html')
