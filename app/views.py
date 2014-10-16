from datetime import datetime
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, \
    login_required
from app import app, db, lm, oid
import json

from forms import LoginForm, EditForm
from .models import User
from  QueryStockOnline import traeIndicadoresxInstrumento
#from QueryStock import BaseDatos


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/ohlvc/<nemo>',methods=['GET', 'POST'])
@login_required
def queryStock(nemo):
 
    #qstol = QueryStockOnline()
    
    
    qst,bol_up,bol_down, volume, sma200, sma50, sma10 =   traeIndicadoresxInstrumento(str(nemo), "20120101", "20141010")


    
    #stockdata = {"data": qst}
    stockdata = json.dumps(qst.tolist())
    bollinger_up = json.dumps(bol_up.tolist())
    bollinger_down = json.dumps(bol_down.tolist())
    volume = json.dumps(volume.tolist())
    sma200 = json.dumps(sma200.tolist())
    sma50 = json.dumps(sma50.tolist())
    sma10 = json.dumps(sma10.tolist())


    return render_template('ohlvc.html',
                           title='OHLVC',
                           stockdata=stockdata,
                           bol_up = bollinger_up,
                           bol_down = bollinger_down,
                           volume = volume,
                           sma200=sma200,
                           sma50=sma50,
                           sma10=sma10,
                           user=g.user,
                           data=nemo)



@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()

@app.route('/')
@app.route('/index')
@login_required
def index():
    print "index :: ", g.user
    user = g.user
    posts = []

    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        print "ingresando......", form.openid.data
        session['remember_me'] = form.remember_me.data

        oid.try_login(form.openid.data, ask_for=['nickname', 'email'])

#        usr = validaUsuario(form.openid.data)
        return after_login( form.openid.data)



    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=[])


def validaUsuario(usuario):
    user = User.query.filter_by(email=usuario).first()
    return user


@oid.after_login
def after_login(resp):

    user = User.query.filter_by(email=resp).first()
    if user is None:
        form = LoginForm()
        return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=[])
    #    nickname = resp.nickname
    #    if nickname is None or nickname == "":
    #        nickname = resp.email.split('@')[0]
    #    user = User(nickname=nickname, email=resp.email)
    #    db.session.add(user)
    #    db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)

    print "AAAAAAAAAAAAAAAAAA"
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                           user=user,
                           posts=posts)


@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Datos guardados.')
        return redirect(url_for('edit'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form, user=g.user)