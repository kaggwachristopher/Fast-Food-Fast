from flask import Flask
from app.models import RecipeOrders, Users

app = Flask(__name__)

recipe = RecipeOrders()
user = Users()


@app.route('/api/v1/orders', methods=['POST'])
def place_an_order():
    if user.not_logged_in():
        return user.not_logged_in()
    elif recipe.invalid_order():
        return recipe.invalid_order()
    else:
        return user.place_order()


@app.route('/api/v1/orders', methods=['GET'])
def all_orders_getter():
    if user.not_logged_in():
        return user.not_logged_in()
    elif user.not_admin():
        return user.not_admin()
    else:
        return recipe.get_all_orders()


@app.route('/api/v1/orders/<order_id>', methods=['GET'])
def get_an_order(order_id):
    if user.not_logged_in():
        return user.not_logged_in()
    elif user.not_admin():
        return user.not_admin()
    else:
        return recipe.get_single_order(order_id)


@app.route('/api/v1/orders/<order_id>', methods=['PUT'])
def update_an_order(order_id):
    if user.not_logged_in():
        return user.not_logged_in()
    elif user.not_admin():
        return user.not_admin()
    elif recipe.invalid_update():
        return recipe.invalid_update()
    else:
        return recipe.update_order_status(order_id)

@app.route('/api/v1/menu', methods=['POST'])
def add_menu_item():
    if user.not_logged_in():
        return user.not_logged_in()
    elif user.not_admin():
        return user.not_admin()
    elif recipe.invalid_meal():
        return recipe.invalid_meal()
    else:
        return recipe.add_meal()


@app.route('/api/v1/menu', methods=['GET'])
def menu_getter():
    return recipe.get_menu()


@app.route('/api/v1/users/orders', methods=['GET'])
def history_getter():
    if user.not_logged_in():
        return user.not_logged_in()
    else:
        return user.get_user_history()


@app.route('/api/v1/auth/signup', methods=['POST'])
def create_new_user():
    if user.invalid_signup():
        return user.invalid_signup()
    else:
        return user.create_user


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    if user.invalid_login():
        return user.invalid_login()
    else:
        return user.user_login()



@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
    if user.not_logged_in():
        return user.not_logged_in()
    elif user.not_admin():
        return user.not_admin()
    else:
        return user.get_users()
