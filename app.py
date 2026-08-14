from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (email,username,phone,password,country_id) values (:email,:username,:phone,:password,:country_id)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['email','username','phone','password','country_id']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['email','username','phone','password','country_id']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['email','username','phone','password','country_id']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into city (name,country_id) values (:name,:country_id)",hey)
        user = query_db('select * from city')

        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)

@app.route("/add_one_cafe_bar", methods=["GET","POST"])
def add_one_cafe_bar():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        one_user = query_db("insert into cafe_bar (name,city_id) values (:name,:city_id)",hey)
        user = query_db('select * from cafe_bar')

        return render_template("cafe_barform.html", cafe_bars=user, one_user=one_user, the_title="add new cafe_bar", touslescity=touslescity)


    touslescity= query_db("select * from city")

    user = query_db('select * from cafe_bar')
    one_user = query_db("select * from cafe_bar limit 1", one=True)
    return render_template("cafe_barform.html", cafe_bars=user, one_user=one_user, the_title="add new cafe_bar", touslescity=touslescity)

@app.route("/add_one_cafe_drinks", methods=["GET","POST"])
def add_one_cafe_drinks():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into cafe_drinks (name,user_id,cafe_bar_id,date,time) values (:name,:user_id,:cafe_bar_id,:date,:time)",hey)
        user = query_db('select * from cafe_drinks')

        return render_template("cafe_drinksform.html", cafe_drinkss=user, one_user=one_user, the_title="add new cafe_drinks")


    user = query_db('select * from cafe_drinks')
    one_user = query_db("select * from cafe_drinks limit 1", one=True)
    return render_template("cafe_drinksform.html", cafe_drinkss=user, one_user=one_user, the_title="add new cafe_drinks")

@app.route("/add_one_musicgenre", methods=["GET","POST"])
def add_one_musicgenre():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musicgenre (name) values (:name)",hey)
        user = query_db('select * from musicgenre')

        return render_template("musicgenreform.html", musicgenres=user, one_user=one_user, the_title="add new musicgenre")


    user = query_db('select * from musicgenre')
    one_user = query_db("select * from musicgenre limit 1", one=True)
    return render_template("musicgenreform.html", musicgenres=user, one_user=one_user, the_title="add new musicgenre")

@app.route("/add_one_celeb", methods=["GET","POST"])
def add_one_celeb():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into celeb (name,country_id,musicgenre_id) values (:name,:country_id,:musicgenre_id)",hey)
        user = query_db('select * from celeb')

        return render_template("celebform.html", celebs=user, one_user=one_user, the_title="add new celeb", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from celeb')
    one_user = query_db("select * from celeb limit 1", one=True)
    return render_template("celebform.html", celebs=user, one_user=one_user, the_title="add new celeb", touslescountry=touslescountry)

@app.route("/add_one_sport", methods=["GET","POST"])
def add_one_sport():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into sport (name,season) values (:name,:season)",hey)
        user = query_db('select * from sport')

        return render_template("sportform.html", sports=user, one_user=one_user, the_title="add new sport")


    user = query_db('select * from sport')
    one_user = query_db("select * from sport limit 1", one=True)
    return render_template("sportform.html", sports=user, one_user=one_user, the_title="add new sport")

@app.route("/add_one_sportpracticed", methods=["GET","POST"])
def add_one_sportpracticed():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into sportpracticed (user_id,sport_id,city_id) values (:user_id,:sport_id,:city_id)",hey)
        user = query_db('select * from sportpracticed')

        return render_template("sportpracticedform.html", sportpracticeds=user, one_user=one_user, the_title="add new sportpracticed")


    user = query_db('select * from sportpracticed')
    one_user = query_db("select * from sportpracticed limit 1", one=True)
    return render_template("sportpracticedform.html", sportpracticeds=user, one_user=one_user, the_title="add new sportpracticed")

@app.route("/add_one_userwaypoints", methods=["GET","POST"])
def add_one_userwaypoints():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescafe_bar= query_db("select * from cafe_bar")

        one_user = query_db("insert into userwaypoints (sportpracticed_id,user_id,lat,lon,cafe_bar_id) values (:sportpracticed_id,:user_id,:lat,:lon,:cafe_bar_id)",hey)
        user = query_db('select * from userwaypoints')

        return render_template("userwaypointsform.html", userwaypointss=user, one_user=one_user, the_title="add new userwaypoints", touslescafe_bar=touslescafe_bar)


    touslescafe_bar= query_db("select * from cafe_bar")

    user = query_db('select * from userwaypoints')
    one_user = query_db("select * from userwaypoints limit 1", one=True)
    return render_template("userwaypointsform.html", userwaypointss=user, one_user=one_user, the_title="add new userwaypoints", touslescafe_bar=touslescafe_bar)

@app.route("/add_one_userhasholographiccompanion", methods=["GET","POST"])
def add_one_userhasholographiccompanion():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesceleb= query_db("select * from celeb")

        one_user = query_db("insert into userhasholographiccompanion (celeb_id,user_id,waypoint_id) values (:celeb_id,:user_id,:waypoint_id)",hey)
        user = query_db('select * from userhasholographiccompanion')

        return render_template("userhasholographiccompanionform.html", userhasholographiccompanions=user, one_user=one_user, the_title="add new userhasholographiccompanion", touslesceleb=touslesceleb)


    touslesceleb= query_db("select * from celeb")

    user = query_db('select * from userhasholographiccompanion')
    one_user = query_db("select * from userhasholographiccompanion limit 1", one=True)
    return render_template("userhasholographiccompanionform.html", userhasholographiccompanions=user, one_user=one_user, the_title="add new userhasholographiccompanion", touslesceleb=touslesceleb)

@app.route("/add_one_street", methods=["GET","POST"])
def add_one_street():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into street (name,city_id) values (:name,:city_id)",hey)
        user = query_db('select * from street')

        return render_template("streetform.html", streets=user, one_user=one_user, the_title="add new street")


    user = query_db('select * from street')
    one_user = query_db("select * from street limit 1", one=True)
    return render_template("streetform.html", streets=user, one_user=one_user, the_title="add new street")

@app.route("/add_one_flat", methods=["GET","POST"])
def add_one_flat():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesstreet= query_db("select * from street")

        one_user = query_db("insert into flat (name_or_number,street_id,lat,lon) values (:name_or_number,:street_id,:lat,:lon)",hey)
        user = query_db('select * from flat')

        return render_template("flatform.html", flats=user, one_user=one_user, the_title="add new flat", touslesstreet=touslesstreet)


    touslesstreet= query_db("select * from street")

    user = query_db('select * from flat')
    one_user = query_db("select * from flat limit 1", one=True)
    return render_template("flatform.html", flats=user, one_user=one_user, the_title="add new flat", touslesstreet=touslesstreet)

@app.route("/add_one_flathasuser", methods=["GET","POST"])
def add_one_flathasuser():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesflat= query_db("select * from flat")

        one_user = query_db("insert into flathasuser (user_id,flat_id) values (:user_id,:flat_id)",hey)
        user = query_db('select * from flathasuser')

        return render_template("flathasuserform.html", flathasusers=user, one_user=one_user, the_title="add new flathasuser", touslesuser=touslesuser, touslesflat=touslesflat)


    touslesuser= query_db("select * from user")

    touslesflat= query_db("select * from flat")

    user = query_db('select * from flathasuser')
    one_user = query_db("select * from flathasuser limit 1", one=True)
    return render_template("flathasuserform.html", flathasusers=user, one_user=one_user, the_title="add new flathasuser", touslesuser=touslesuser, touslesflat=touslesflat)

@app.route("/add_one_flathasmusicgenre", methods=["GET","POST"])
def add_one_flathasmusicgenre():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesflat= query_db("select * from flat")

        touslesmusicgenre= query_db("select * from musicgenre")

        one_user = query_db("insert into flathasmusicgenre (flat_id,musicgenre_id) values (:flat_id,:musicgenre_id)",hey)
        user = query_db('select * from flathasmusicgenre')

        return render_template("flathasmusicgenreform.html", flathasmusicgenres=user, one_user=one_user, the_title="add new flathasmusicgenre", touslesflat=touslesflat, touslesmusicgenre=touslesmusicgenre)


    touslesflat= query_db("select * from flat")

    touslesmusicgenre= query_db("select * from musicgenre")

    user = query_db('select * from flathasmusicgenre')
    one_user = query_db("select * from flathasmusicgenre limit 1", one=True)
    return render_template("flathasmusicgenreform.html", flathasmusicgenres=user, one_user=one_user, the_title="add new flathasmusicgenre", touslesflat=touslesflat, touslesmusicgenre=touslesmusicgenre)

@app.route("/add_one_musicalinstrument", methods=["GET","POST"])
def add_one_musicalinstrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musicalinstrument (name) values (:name)",hey)
        user = query_db('select * from musicalinstrument')

        return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")


    user = query_db('select * from musicalinstrument')
    one_user = query_db("select * from musicalinstrument limit 1", one=True)
    return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")

@app.route("/add_one_userplaysinstrument", methods=["GET","POST"])
def add_one_userplaysinstrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into userplaysinstrument (musicallinstrument-id,user-id,flat-id) values (:musicallinstrument-id,:user-id,:flat-id)",hey)
        user = query_db('select * from userplaysinstrument')

        return render_template("userplaysinstrumentform.html", userplaysinstruments=user, one_user=one_user, the_title="add new userplaysinstrument")


    user = query_db('select * from userplaysinstrument')
    one_user = query_db("select * from userplaysinstrument limit 1", one=True)
    return render_template("userplaysinstrumentform.html", userplaysinstruments=user, one_user=one_user, the_title="add new userplaysinstrument")

@app.route("/add_one_flathasshopsnearby", methods=["GET","POST"])
def add_one_flathasshopsnearby():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into flathasshopsnearby (shopname,lat,lon) values (:shopname,:lat,:lon)",hey)
        user = query_db('select * from flathasshopsnearby')

        return render_template("flathasshopsnearbyform.html", flathasshopsnearbys=user, one_user=one_user, the_title="add new flathasshopsnearby")


    user = query_db('select * from flathasshopsnearby')
    one_user = query_db("select * from flathasshopsnearby limit 1", one=True)
    return render_template("flathasshopsnearbyform.html", flathasshopsnearbys=user, one_user=one_user, the_title="add new flathasshopsnearby")

