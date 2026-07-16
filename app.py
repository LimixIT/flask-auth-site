from flask import Flask, render_template, request, session, redirect
import json
import os
import hashlib

base_dir = os.path.dirname(os.path.abspath(__file__))
users_dir = os.path.join(base_dir, 'users')
os.makedirs(users_dir, exist_ok=True)

app = Flask(__name__)
app.secret_key = 'iMKU1w5V.n*G7$iO9,qe97Bc~j!cYSI-th[-8RHpgsuo>h7R=,-S3w|UHfDFwDU3.1Nl>7*/|AK^3eUMNF$UpEnmdfN1s79hnCXCY8%g&jn6IgQ2dh-+nyuiRc76P?`]z-V(NvN3#45gvjpAw]Q*to`U96uJFI^?L:1[YFJWTzGt)~DS9(wq]:sq%Lxc+6JVj5WmFR`/j?rpI7:uVy>:N%W6=z]8&&&-O)FQ!Nt[$r^cwy]U;AbCJ5qK@1d>&&ZO@Hs@L$o*W5^7C_o*8V#?quh_^TSBb:[]!bgLYVx0!M(j_egx>~jXg=EU0(2O[)n&on/2f3ws8Pq(&`9WP!RVb3xcl=)NiU,l#jf*]qFuL<%#D_TG3FD!HrDD|p49+B&8%m)koC<y@xJw^Jf#(V<-Ee:=w25[Y]L9I7oO5;>Y[p_pu$dDL2.mfGGm^Oj20S]IN73UMo%wQa!xh4)e`Yv^BIBb5)fvS@6i!`aovO>fRtqM=;t0Jx7HaB960q56z3Ov'

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def get_user_path(email: str) -> str:
    return os.path.join(users_dir, email, 'data.json')

@app.route('/')
def index():
    return render_template('index.html')

# -----------------------------------------

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        password = request.form['password']

        if not all([username, age, email, password]):
            return 'Все поля обязательны!'

        user_path = get_user_path(email)
        user_dir = os.path.dirname(user_path)

        if os.path.exists(user_path):
            return 'Пользователь с такой почтой уже существует!'

        os.makedirs(user_dir, exist_ok=True)

        user_data = {
            'username': username,
            'age': age,
            'email': email,
            'password': hash_password(password)
        }

        try:
            with open(user_path, 'w', encoding='utf-8') as f:
                json.dump(user_data, f, ensure_ascii=False, indent=2)
        except  Exception as e:
            return f'Ошибка при сохранении данных: {e}'
        session['email'] = email
        session['user'] = username
        return redirect('/profile')
    
    return render_template('register.html')
    
# -----------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
            return 'Заполните все поля!'
        
        user_path = get_user_path(email)

        if not os.path.exists(user_path):
            return 'Пользователь не найден!'

        try:
            with open(user_path, 'r', encoding='utf-8') as f:
                user_data = json.load(f)
        except (json.JSONDecodeError, IOError):
            return 'Ошибка чтения данных пользователя.'
        
        if user_data['password'] != hash_password(password):
            return 'Неверный пароль!'
        
        session['email'] = email
        session['user'] = user_data['username']
        return redirect('/profile')
    else:
        return render_template('login.html')

# -----------------------------------------

@app.route('/profile')
def profile():
    if 'email' not in session:
        return redirect('/register')
    
    email = session['email']
    
    user_path = get_user_path(email)

    if not os.path.exists(user_path):
        session.clear()
        return 'Профиль не найден. Пожалуйста, войдите заново.'
    
    try:
        try:
            with open(user_path, 'r', encoding='utf-8') as f:
                user_data = json.load(f)
        except (json.JSONDecodeError, IOError):
            return 'Ошибка загрузки профиля.'

        return render_template(
            'profile.html',
            user=user_data['username'],
            email=user_data['email'],
            age=user_data['age']
        )

    except Exception as e:
        return f"Возникла ошибка: {str(e)}"

# -------------------------------------------

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/register')

# -------------------------------------------

app.run(debug=True)