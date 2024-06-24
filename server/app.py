from flask import Flask, make_response, render_template_string, abort
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    return '<h1>Zoo app</h1>'


@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get_or_404(id)
    
    response_body = f'''
    <h2>Animal Details</h2>
    <ul>
        <li>ID: {animal.id}</li>
        <li>Name: {animal.name}</li>
        <li>Species: {animal.species}</li>
        <li>Zookeeper: {animal.zookeeper.name}</li>
        <li>Enclosure: {animal.enclosure.environment}</li>
    </ul>
    '''
    return render_template_string(response_body)


@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get_or_404(id)
    
    response_body = f'''
    <h2>Zookeeper Details</h2>
    <ul>
        <li>ID: {zookeeper.id}</li>
        <li>Name: {zookeeper.name}</li>
        <li>Birthday: {zookeeper.birthday}</li>
    '''
    
    if zookeeper.animals:
        response_body += '<li>Animals:</li><ul>'
        for animal in zookeeper.animals:
            response_body += f'<li>{animal.name}</li>'
        response_body += '</ul>'
    
    response_body += '</ul>'
    return render_template_string(response_body)


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get_or_404(id)
    
    response_body = f'''
    <h2>Enclosure Details</h2>
    <ul>
        <li>ID: {enclosure.id}</li>
        <li>Environment: {enclosure.environment}</li>
        <li>Open to Visitors: {enclosure.open_to_visitors}</li>
    '''
    
    if enclosure.animals:
        response_body += '<li>Animals:</li><ul>'
        for animal in enclosure.animals:
            response_body += f'<li>{animal.name}</li>'
        response_body += '</ul>'
    
    response_body += '</ul>'
    return render_template_string(response_body)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
