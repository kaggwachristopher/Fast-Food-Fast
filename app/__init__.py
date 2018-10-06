# import psycopg2
#
#
# connection_credentials = '''database="fast_food", user = "fast_food", password = "fastfoodfast", host = "localhost", port = "5432"'''
#
# try:
#     database_connection = psycopg2.connect(connection_credentials)
#     database_connection.autocommit = True
#     cursor = database_connection.cursor()
#     print('\n\nConnected to Database\n\n')
# except Exception as e:
#     print(e.message())
#     print("Failed to connect to db")
#
# # if database_connection:
# #     print("successfully connected to database")
# # else:
# #     print("Database connection failed")
