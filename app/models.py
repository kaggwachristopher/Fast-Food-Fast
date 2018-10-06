from flask import jsonify, request, json
import datetime
import psycopg2


class Database:
    def __init__(self):
        connection_credentials = """
        dbname='fast_food' user='postgres' password='idontgiveadamnwhatyouthink'
         host='localhost' port='5432'
         """
        try:
            self.connection = psycopg2.connect(connection_credentials)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print('\n\nConnected to Database')
        except:
            print("\n\n Failed to connect to db")


class RecipeOrders(Database):

    def __init__(self):
        super().__init__()
        self.all_orders_list = [{
            "order_date": "2018-09-22 02:36:27.956913",
            "order_id": 3,
            "order_status": "Pending",
            "quantity": 5,
            "food_name": "plain chips",
            "user_id": 21
        }]
        self.menu = []

    def get_all_orders(self):
        # This if statement checks whether the list contains dummy data then it empties the list
        if len(self.all_orders_list) == 1:
            return jsonify({'orders': []}), 200
        else:
            return jsonify({'orders': self.all_orders_list}), 200

    def get_single_order(self, order_id):
        for order in self.all_orders_list:
            if str(order['order_id']) == str(order_id):
                return jsonify(order), 200
        return jsonify({'error': 'Order does not exist not'}), 404

    def update_order_status(self, order_id):
        data = request.get_json()
        status_id = data['status_id']
        if type(status_id) != int:
            if str(status_id) == "0":
                pass
            return jsonify({'Bad request': 'order status has to be a number from 1-4'}), 400
        else:
            pass
        if str(status_id).strip() == "":
            return jsonify({'error': 'status_id cannot be empty'}), 400
        for order in self.all_orders_list:
            if str(order['order_id']) == str(order_id):
                if status_id == 4:
                    order['order_status'] = "Declined"
                    return jsonify({'status updated': order}), 201
                # when the status_id is zero,the order status is changed to declined

                elif status_id == 1:
                    order['order_status'] = "Pending"
                    return jsonify({'status updated': order}), 201
                # when the status_id is 1,the order status is changed to pending

                elif status_id == 2:
                    order['order_status'] = "Accepted"
                    return jsonify({'status updated': order}), 201
                # when the status_id is 2,the order status is changed to Accepted

                elif status_id == 3:
                    order['order_status'] = "Completed"
                    return jsonify({'status updated': order}), 201
                # when the status_id is 3,the order status is changed to Completed

                else:
                    return jsonify({'message': 'invalid status_id entry'}), 400

        return jsonify({'Not found': 'invalid order id'}), 404

    def add_meal(self):
        data = request.get_json()
        food_name = data.get('food_name')
        price = data.get('price')
        item_number = len(self.menu) + 1
        new_item = {
            "food": food_name,
            "item_number": item_number,
            "price": price
        }
        self.menu.append(new_item)
        return jsonify({'new_menu_item': new_item}), 201

    def get_menu(self):
        return jsonify({"Today's menu": self.menu}), 200

    def invalid_order(self):
        data = request.get_json()
        food_name = data.get('food_name')
        quantity = data.get('quantity')

        if not quantity:
            return jsonify({'missing field': 'input must contain the food quantity'}), 400
        elif type(quantity) != int:
            return jsonify({'error': 'the quantity should be a number'}), 400

        if not food_name:
            return jsonify({'missing field': 'input must contain a the name of the food you want'}), 400
        if type(food_name) != str:
                return jsonify({'error':'the food_name should be a string'}), 400
        elif food_name.strip() == "":
            return jsonify({'error': 'the food_name field cant be empty'}), 400

    def invalid_update(self):
        data = request.get_json()
        status_id = data.get('status_id')
        if not status_id:
            return jsonify({'missing field':'you must put a status_id field'}), 400

    def invalid_meal(self):
        data = request.get_json()
        food_name = data.get('food_name')
        price = data.get('price')
        if not food_name:
            if food_name == "":
                pass
            else:
                return jsonify({'missing field': 'input must contain a food_name'}), 400
        if type(food_name) != str:
            return jsonify({'error': 'the food_name should be a string'}), 400
        elif food_name.strip() == "" or food_name == "":
            return jsonify({'error': 'the food_name field cant be empty'}), 400

        if not price:
            if price == 0:
                pass
            else:
                return jsonify({'missing field': 'input must contain a price'}), 400
        if type(price) != int:
            return jsonify({'error': 'the price should be an integer'}), 400
        elif price == 0:
            return jsonify({'error': 'the price field cant be Zero'}), 400


class Users(RecipeOrders,Database):

    def __init__(self):
        super().__init__()
        fetch_emails = """
        SELECT email FROM users;
        """
        self.cursor.execute(fetch_emails)
        fetched_emails = self.cursor.fetchall()
        self.all_users_list = []
        self.user_emails = []
        for email in fetched_emails:
            self.user_emails.append(email[0])

        fetch_contacts = """
                SELECT contact FROM users;
                """
        self.cursor.execute(fetch_contacts)
        fetched_contacts = self.cursor.fetchall()
        self.user_contacts=[]
        for contact in fetched_contacts:
            self.user_contacts.append(contact[0])

        self.logged_in_user = ""
        self.login_status = False
        self.logged_in_user_details = dict()

        fetch_users = """
                SELECT * FROM users;
                """
        self.cursor.execute(fetch_users)
        users = self.cursor.fetchall()
        print(users)
        for user in users:
            user_dict = dict(user_id=user[0], first_name=user[1], last_name=user[2], account_type=user[3],
                             contact=user[4], email=user[5], residence=user[6], address=user[7], password=user[8],
                             creation_date=user[9])
            self.all_users_list.append(user_dict)

        self.logged_in_user = ""
        self.login_status = False
        self.logged_in_user_details = dict()


    def get_users(self):
        return jsonify({'all users': self.all_users_list}), 200

    def create_user(self):
        data = request.get_json()
        # only for those to signup as admins
        admin_key = data.get('admin_key')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        address = data.get('address')
        residence = data.get('residence')
        contact = data.get('contact')
        email = data.get('email')
        password = data.get('password')
        creation_date = str(str(datetime.date.today())+str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute))
        if admin_key == 99001122:
            account_type = "admin"
        else:
            account_type = "customer"


        # self.all_users_list.append(new_user)
        insert_user_command = """
                INSERT INTO users (first_name, last_name,contact,account_type, email,password,residence,address, creation_date) 
                VALUES ('{}', '{}','{}','{}','{}','{}','{}','{}','{}');
                """.format(first_name, last_name,contact,account_type, email, password, residence,address, creation_date)
        self.cursor.execute(insert_user_command)
        id_fetch = """
                select user_id from users where email='{}'
                """.format(email)
        execution = self.cursor.execute(id_fetch)
        fetched_id = self.cursor.fetchone()
        return jsonify({'signup successful your user id is':'you may now login'}), 201

    def get_user_history(self):
        history_list = []
        for order in RecipeOrders().all_orders_list:
            if order['user_id'] == self.logged_in_user_details['user_id']:
                history_list.append(order)

        return jsonify({'your order history': history_list}), 200

    def user_login(self):
        data = request.get_json()
        email_or_contact = data.get('email/contact')
        password = data.get('password')

        for user in self.all_users_list:
            if (user['email'] == email_or_contact or user['contact'] == email_or_contact) and user['password'] == password:
                self.logged_in_user = user['account_type']
                self.logged_in_user_details = user
                self.login_status = True
                return jsonify({'success': 'logged in'}), 201
            else:
                return jsonify({'login failed': 'check your password, email, or phone'}), 401
        return jsonify({'Login failure': 'users list is empty, please signup!!'}), 400

    def invalid_login(self):
        data = request.get_json()
        email_or_contact = data.get('email/contact')
        password = data.get('password')
        if not email_or_contact:
            if email_or_contact != "":
                return jsonify({'missing field': 'you have to include your email or contact'}), 400
        elif not password:
            if password != "":
                return jsonify({'missing field': 'you have to include your password'}), 400

    def invalid_signup(self):
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        address = data.get('address')
        residence = data.get('residence')
        contact = data.get('contact')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')


        # checks that all fields are included in json data and are not blank
        if not first_name or first_name.strip() == "":
                return jsonify({'missing field' : 'you have to include your first name and it shouldnt be blank'}), 400
        elif not last_name or last_name.strip() == "":
            return jsonify({'missing field' : 'you have to include your last name and it shouldnt be blank'}), 400
        elif not email or last_name.strip() == "":
            return jsonify({'missing field' : 'you have to include your email and it shouldnt be blank'}), 400
        elif not residence or residence.strip() == "" :
            return jsonify({'missing field' : 'you have to include your area of residence and it shouldnt be blank'}), 400
        elif not address or address.strip() == "":
            return jsonify({'missing field' : 'you have to include your address and it shouldnt be blank'}), 400
        elif not contact or contact.strip() == "":
            return jsonify({'missing field' : 'you have to include your contact and it shouldnt be blank'}), 400
        elif not password or password.strip() == "":
            return jsonify({'missing field' : 'you have to include your password and it shouldnt be blank'}), 400
        elif not confirm_password or confirm_password.strip() == "":
            return jsonify({'missing field' : 'you have to include your password confirmaton and it shouldnt be blank'}), 400

        # password validation
        if len(json.dumps(password)) < 6:
            return jsonify({'invalid password': 'password should bear atleast 6 characters'}), 411
        if str(password) != str(confirm_password):
            return jsonify({'error': 'passwords do not match'})

        # check whether email or phone already exists
        if str(email) in self.user_emails:
            return jsonify({'Signup failure': 'This email belongs to another account'})
        if str(contact) in self.user_contacts:
            return jsonify({'Signup failure': 'This contact is already used'})

        # checks whether field data is in the right data types
        if type(first_name) != str or type(last_name) != str or type(address) != str or type(contact) != str or type(password) != str or type(confirm_password) != str or type(email) != str:
            return jsonify({'type error': 'all inputs must be strings'}), 400


    def place_order(self):
        data = request.get_json()
        user_id = self.logged_in_user_details['user_id']
        food_name = data['food_name']
        full_name = self.logged_in_user_details['first_name'] + " " + self.logged_in_user_details['last_name']
        quantity = data['quantity']
        order_id = len(RecipeOrders().all_orders_list) + 1
        new_order = {
            "user_id": user_id,
            "full name": full_name,
            "quantity": quantity,
            "food_name": food_name,
            "order_id": order_id,
            "order_status": "Pending",
            "order_date": str(datetime.datetime.now())
        }
        RecipeOrders().all_orders_list.append(new_order)
        return jsonify({'order': new_order}), 201

    def not_logged_in(self):
        if not self.login_status:
            return jsonify({'Login required': 'Please login to your account and then try again'})

    def not_admin(self):
        if self.logged_in_user != "admin":
            return jsonify({'Unauthorized': 'only admin users can have access to this information'})

