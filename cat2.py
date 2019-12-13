from flask import Flask, render_template, redirect, request
from datetime import datetime
import sqlite3
app = Flask(__name__)

app.secret_key = "machineko"


@app.route("/")
def hello():
    return redirect("/top")

# -----------------------------------------------

@app.route("/top")
def top():
    return render_template("top.html")

# -----------------------------------------------

@app.route("/search")
def g_search():
    return render_template("search.html")

# -----------------------------------------------

@app.route("/search", methods=["POST"])
def search():
    color = request.form.get("color")
    age = request.form.get("age")
    ear = request.form.get("ear")
    
    print(color)
    print(age)
    print(ear)

    conn = sqlite3.connect('cat.db')
    c = conn.cursor()
    c.execute("select color, age, ear from cat where color = ? and age = ? and ear = ? order by id DESC limit 10", (color, age, ear))
    conn.commit()
    conn.close()

    # c = color
    # a = age
    # e = ear

    return redirect("/kensaku")


@app.route("/regist")
def g_regist():
    return render_template("regist.html")

# -----------------------------------------------

@app.route("/regist", methods=["POST"])
def regist():

    imgpath = request.form.get("imgpath")
    name = request.form.get("name")
    genre = request.form.get("genre")
    color = request.form.get("color")
    age = request.form.get("age")
    ear = request.form.get("ear")
    comment = request.form.get("comment")
    d = datetime.now()
    date = d.strftime("%Y/%m/%d %H:%M")

    conn = sqlite3.connect('cat.db')
    c = conn.cursor()
    c.execute(
        "insert into cat(id, imgpath, name, genre, color, age, ear, comment, date) values(null,?,?,?,?,?,?,?,?)",
        (imgpath, name, genre, color, age, ear, comment, date))
    conn.commit()
    conn.close()

    # cat_data = [id, imgpath, name, genre, color, age, ear, comment, date]
    return render_template("top.html")

# -----------------------------------------------

@app.route("/noraneko")
def noraneko():

    #データベースに接続
    conn = sqlite3.connect('cat.db')
    c = conn.cursor()
    
    # execute内のwhere,order,limitで条件を指定し、genreカラムに"ノラ"の値を持っているデータのみを算出し、並び順と表示件数を設定
    c.execute("select id, name, date, imgpath, comment, color, age, ear from cat where genre = 'ノラ' order by id DESC limit 10")
    noraneko_list = []
    for n_cat in c.fetchall():
        noraneko_list.append({
            "id": n_cat[0],
            "name": n_cat[1],
            "date": n_cat[2],
            "imgpath": n_cat[3],
            "comment": n_cat[4],
            "color": n_cat[5],
            "age": n_cat[6],
            "ear": n_cat[7]
        })
    c.close()
  
    conn.commit()
    conn.close()
    return render_template("noraneko.html", nora_list = noraneko_list)

# -----------------------------------------------

@app.route("/maigoneko")
def maigoneko():

    #データベースに接続
    conn = sqlite3.connect('cat.db')
    c = conn.cursor()

    # execute内のwhere,order,limitで条件を指定し、genreカラムに"迷子"の値を持っているデータのみを算出し、並び順と表示件数を設定
    c.execute("select id, name, date, imgpath, comment, color, ear, age from cat where genre = '迷子' order by id DESC limit 10")
    maigoneko_list = []
    for m_cat in c.fetchall():
        maigoneko_list.append({
            "id": m_cat[0],
            "name": m_cat[1],
            "date": m_cat[2],
            "imgpath": m_cat[3],
            "comment": m_cat[4],
            "color": m_cat[5],
            "ear": m_cat[6],
            "age": m_cat[7]
        })
    c.close()
    return render_template("maigoneko.html", maigo_list = maigoneko_list)

# -----------------------------------------------

@app.route("/kensaku")
def kensaku():

    #データベースに接続
    conn = sqlite3.connect('cat.db')
    c = conn.cursor()

    c.execute("select id, name, date, imgpath, comment, color, age, ear from cat where color = '茶' and age = '仔猫' and ear = 'サクラ' order by id DESC limit 10")
    search_list = []
    for s_cat in c.fetchall():
        search_list.append({
            "id": s_cat[0],
            "name": s_cat[1],
            "date": s_cat[2],
            "imgpath": s_cat[3],
            "comment": s_cat[4],
            "color": s_cat[5],
            "ear": s_cat[6],
            "age": s_cat[7]
        })
    c.close()
    return render_template("kensaku.html", s_list = search_list)
# , color = color, age = age, ear = ear

@app.errorhandler(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@app.errorhandler(404)
def notfound404(code):
    return "お探しのページはみつかりませんでした。<br>URLに誤りがあります。"


#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)












# @appp.route("/noraneko")

    # name = request.form.get("name")
    # # datetime = datetime.now()
    # # datetime = request.form.get("datetime")
    # imgpath = request.form.get("imgpath")
    # comment = request.form.get("comment")
    # color = request.form.get("color")
    # ear = request.form.get("ear")
    # age = request.form.get("age")
