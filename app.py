import flask as f
import hashlib
import datetime
import sqlite3
import json

g_jst = datetime.timezone(datetime.timedelta(hours=9))

app = f.Flask(__name__)
app.config['SECRET_KEY'] = hashlib.sha256("SAMPLE_00000000000001".encode()).hexdigest()

@app.route("/")
def index():
	conn = sqlite3.connect("db/sample.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM TESTTBL ORDER BY COLUM1")
	rows = cur.fetchall()
	cur.close()
	conn.close()
	return f.render_template("index.html", title_name="サンプル的な何か", items = rows)

@app.route("/api/<int:id>", methods=["GET", "POST"])
def api(id : int):
	conn = sqlite3.connect("db/sample.db")
	cur = conn.cursor()
	cur.execute("SELECT COLUM1, COLUM2 FROM TESTTBL WHERE ID=?", (id,))
	row = cur.fetchone()
	cur.close()
	conn.close()
	if row is None:
		return '{"COLUM1": 0, "COLUM2": ""}'
	response_dic = { "COLUM1" : row[0], "COLUM2" : row[1] }
	response = json.dumps(response_dic, ensure_ascii=False)
	return response

@app.errorhandler(404)
def notfound404(code):
    return f.render_template("404.html", title_name="なにもない")

if __name__ == "__main__":
	app.run(debug = True, host="127.0.0.1")
