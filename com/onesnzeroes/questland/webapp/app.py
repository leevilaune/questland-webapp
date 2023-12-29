from flask import Flask, render_template

from com.onesnzeroes.questland.webapp.qlapi.APICaller import APICaller

app = Flask(__name__)
qlapi = APICaller("wss://prod.ql-api-gamesture.com/ws")


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/api/guild/<guildid>/<token>')
def guild(guildid, token):
    print(guildid)
    return qlapi.get_guild(guildid,token)

if __name__ == '__main__':
    app.run(debug=True)
