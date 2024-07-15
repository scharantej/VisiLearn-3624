
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for lessons list
lessons = [
    {"id": 1, "title": "Lesson 1", "image": "image1.jpg", "content": "Content for lesson 1"},
    {"id": 2, "title": "Lesson 2", "image": "image2.jpg", "content": "Content for lesson 2"},
    {"id": 3, "title": "Lesson 3", "image": "image3.jpg", "content": "Content for lesson 3"},
]

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for lessons list
@app.route('/lessons')
def lessons():
    return render_template('lessons.html', lessons=lessons)

# Route for a specific lesson
@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    lesson = next((lesson for lesson in lessons if lesson["id"] == lesson_id), None)
    return render_template('lesson.html', lesson=lesson)

# Route for user progress tracking (not included in the provided design)
@app.route('/progress')
def progress():
    return render_template('progress.html')

# Route for user login (not included in the provided design)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Placeholder code for user authentication (not included in the provided design)
        if username == 'admin' and password == 'password':
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

# Route for user registration (not included in the provided design)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Placeholder code for user registration (not included in the provided design)
        if username not in ['admin']:
            return redirect(url_for('index'))
        else:
            return redirect(url_for('register'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
