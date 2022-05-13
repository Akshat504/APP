from flask import Blueprint

example_blueprint = Blueprint('example_blueprint', __name__)
'''
    example_blueprint is the name of Bluprint's which is used by flask, & __name__ is the Blueprint's import name.

'''


@example_blueprint.route('/example')
def myorders():
    return "This is an example appp."


@example_blueprint.route('/hey')
def hey():
    return "Say Hello!"