# CREATE TABLE orders(
#     order_id  SERIAL PRIMARY KEY,
#     user_id int not null,
#     full_user_name varchar not null,
#     food_name varchar(30) not null,
#     quantity int not null,
#     order_status varchar(10) not  null,
#     order_date varchar(20) not null,
#     order_price int not null
# # );
# CREATE TABLE menu(
#     item_number  SERIAL PRIMARY KEY not null,
#     food_name varchar(20) not null,
#     price int not null
# );