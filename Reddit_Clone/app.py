from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
      
    'author':'Mario Monir',
    'title':'Blog post 1',
    'content':'First post Content',
    'date_posted':'May 1 2020'
    },
    {
            
    'author':'Mario Salim',
    'title':'Blog post 2',
    'content':'Second post Content',
    'date_posted':'May 2 2020'

    }
]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)