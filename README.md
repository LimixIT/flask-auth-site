# 🔐 Flask Auth Site
## **(RU) Сайт на Flask с регистрацией, входом, профилем и хешированием паролей.**
Мой первый fullstack-проект — сайт с регистрацией, входом и личным профилем. Написан на **Flask** с нуля.

### ✨ Что умеет сайт

- 📝 Регистрация новых пользователей (имя, возраст, почта, пароль)
- 🔑 Вход по email и паролю
- 👤 Личный профиль с данными пользователя
- 🔒 Хеширование паролей (SHA-256)
- 🎨 Красивый дизайн с анимациями и адаптивной вёрсткой
- 📱 Адаптация под мобильные устройства
- 🚪 Выход из аккаунта

### 🛠 Технологии

| Сфера | Инструменты |
|-------|-------------|
| Бэкенд | Python, Flask |
| Фронтенд | HTML5, CSS3 |
| Хранение данных | JSON-файлы |
| Безопасность | hashlib (SHA-256), Flask sessions |
| Анимации, адаптация, шрифты | CSS @keyframes, @media, @font-face |

### 🚀 Как запустить

#### Для продвинутых

##### 1. Клонируй репозиторий:
```bash
git clone https://github.com/LimixIT/flask-auth-site.git
```

##### 2. Перейди в папку проекта:
```bash
cd flask-auth-site
```

##### 3. Установи Flask:
```bash
pip install flask
```

##### 4. Запусти файл `app.py` (кнопка ▶️ в правом верхнем углу VSCode или команда в терминале):
```bash
python app.py
```

##### 5. В терминале появится ссылка `http://127.0.0.1:5000` — открой её в браузере.

#### Для новичков

##### 1. Скачай проект (зелёная кнопка **Code → Download ZIP**)
##### 2. Распакуй ZIP в любую папку
##### 3. Открой папку в **VS Code**
##### 4. Установи Flask (один раз):
   - Открой терминал (`Ctrl + J`)
   - Напиши: `pip install flask`
##### 5. Открой файл `app.py`
##### 6. Нажми кнопку ▶️ (Run Python File) в правом верхнем углу
##### 7. Перейди по ссылке из терминала в браузере
</details>

---
---
---

## **(EN) A Flask website with registration, login, profile, and password hashing.**

My first full-stack project is a website with registration, login, and a personal profile. It was written in Flask from scratch.

### ✨ What the site can do

- 📝 New user registration (name, age, email, password)
- 🔑 Login with email and password
- 👤 Personal profile with user data
- 🔒 Password hashing (SHA-256)
- 🎨 Beautiful design with animations and responsive layout
- 📱 Mobile-friendly
- 🚪 Account logout

### 🛠 Technologies

| Industry | Tools |
|-------|-------------|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3 |
| Data Storage | JSON Files |
| Security | hashlib (SHA-256), Flask sessions |
| Animations, responsiveness, fonts | CSS @keyframes, @media, @font-face |

### 🚀 How to run

#### For advanced users

##### 1. Clone the repository:
```bash
git clone https://github.com/LimixIT/flask-auth-site.git
```

##### 2. Change to the project folder:
```bash
cd flask-auth-site
```

##### 3. Install Flask:
```bash
pip install flask
```

##### 4. Run the `app.py` file (click the ▶️ button in the upper right corner of VSCode or enter the command in the terminal):
```bash
python app.py
```

##### 5. The link `http://127.0.0.1:5000` will appear in the terminal – open it in your browser.

#### For Beginners

##### 1. Download the project (green button **Code → Download ZIP**)
##### 2. Unzip the ZIP to any folder
##### 3. Open the folder in **VS Code**
##### 4. Install Flask (once):
- Open the terminal (`Ctrl + J`)
- Type: `pip install flask`
##### 5. Open the `app.py` file
##### 6. Click the ▶️ (Run Python File) button in the upper right corner
##### 7. Follow the link from the terminal in your browser

---
---
---

### 📁 Структура проекта / 📁 Project structure
```text
flask-auth-site/
├── app.py              # Основной файл с бэкендом / Main file with backend
├── templates/          # HTML-шаблоны / HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── profile.html
├── static/
│   ├── style.css       # Все стили / All styles
|   ├── 3.webp          # Фон шапки / Header background
│   └── fonts/          # Шрифты / Fonts
└── users/              # Данные пользователей (JSON) / User data (JSON)
```

### 📸 Скриншоты / 📸 Screenshots
