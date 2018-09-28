[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5e07e858943a454b90a8e40d9f8c2a6e)](https://app.codacy.com/app/kaggwachristopher/Fast-Food-Fast?utm_source=github.com&utm_medium=referral&utm_content=kaggwachristopher/Fast-Food-Fast&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/kaggwachristopher/Fast-Food-Fast.svg?branch=api)](https://travis-ci.org/kaggwachristopher/Fast-Food-Fast)[![Coverage Status](https://coveralls.io/repos/github/kaggwachristopher/Fast-Food-Fast/badge.svg?branch=api)](https://coveralls.io/github/kaggwachristopher/Fast-Food-Fast?branch=api)[![Test Coverage](https://api.codeclimate.com/v1/badges/7e866f55b4e3f8e28a17/test_coverage)](https://codeclimate.com/github/kaggwachristopher/Fast-Food-Fast/test_coverage)[![Maintainability](https://api.codeclimate.com/v1/badges/7e866f55b4e3f8e28a17/maintainability)](https://codeclimate.com/github/kaggwachristopher/Fast-Food-Fast/maintainability)

# Fast-Food-Fast

Fast-Food-Fast is a food delivery application for a restaurant which enables users to order for food and admin users to handle and manage the different orders.


### Prerequisites

The app works well on all operating systems provided you have the following installed and well setup 

```
python (version 3 and above recommended)
Virtual environment
Flask(A python web framework)
Pytest
An API development environment forexample postman and insomnia
```
* You can read out more of the prerequesities in [requirements.txt](https://github.com/kaggwachristopher/Fast-Food-Fast/blob/api/requirements.txt)

### Installing

###### Install python

* You need to first get python installed on your system. Find out [here](https://realpython.com/installing-python/) how to download and install python on your system

###### Install virtual environment
* A Virtual environment is an isolated python environment
* Use this [link](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) to find out how to install and activate virtual environment on your system 

###### Install flask
* Navigate into your virtual environment and open your terminal
* use this command to install flask 

    ```$ pip install flask```

###### Install pytest
* Navigate into your virtual environment and open your terminal
* use this command to install pytest 

    ```$ pip install pytest```

###### Install an API development environment
* For these, the choice is yours to choose which one you are familiar with or most convinient with.
* There are lots of such environments out there but i take postman to be the best
* You can click [here](https://www.getpostman.com/docs/v6/postman/launching_postman/installation_and_updates) to learn more about how you can install and use postman
#### Running the app
1. After setting up the above successfully, run the python file named run.py which is on the root directory. 
2. This will automatically start the flask server to run your app
3. You can now open post man and send the following HTTP requests to the following URLS
4. To access the API endpoints add the resource url to the host name and port number(localhost:5000/resource url)  

|Resource URL|Methods   |Description|
|----------------|------------|-------------|
|`/api/v1/orders` |GET |Get all orders|
|`/api/v1/orders` |POST |Add an order|
|`/api/v1/orders/<order_id>` |GET|Fetch a specific order with this order_id|
|`/api/v1/orders/<order_id>` |PUT |Update the status of an order with this order_id |

#### Working with the api

pass in such json data inorder to post an order
```
{
  "user_id":"21",
  "recipe_id":"4",
  "quantity":"5"
}
```

pass in such json data inorder to update the status of an order an order
```
{
  "status_id":"1"
}

status_id=0 declines an order
status_id=1 puts an order on pending
status_id=2 accepts an order
status_id=3 completes an order

```

## Running the tests

* Since you now have pytest installed you just need to open your terminal and navigate into the project directory
* Enter the command below to run the tests

```$ Pytest```

* To run the tests with coverage navigate to the root directory and run this code in your terminal

pytest test.py --cov=app --cov-report term-missing


###### Automated tests
The tests are automated and can be seen on travis CI. Use this [link](https://travis-ci.org/kaggwachristopher/Fast-Food-Fast) to have a look at the automated tests 

## Deployment

* This app is automatically deployed on heroku. Follow this [link](https://fast-foods.herokuapp.com) to see how the app is working on heroku
* You can also use postman to send requests as you do it locally on your server 
## Built With

* Flask - The python web framework used
* JSON - The data transfer model used

## Versioning

* This app is versioned using url versioning

## Authors

* **Christopher Kaggwa** 

## Acknowledgments

* I greatfully thank my bootcamp 12(LFA) learning facilitator assistant Nshemerirwe Flavia for feedback on improvement of the project. 
* I also extend my appreciation to my bootcamp 12 teammates for all their contributions towards this great output
* Finally I appreciate Andela Uganda for the facilitated learning I recieved to enable me deliver such output



