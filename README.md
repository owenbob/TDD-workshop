[![Build Status](https://travis-ci.org/owenbob/TDD-workshop.svg?branch=master)](https://travis-ci.org/owenbob/TDD-workshop)

#  Testing GraphqL Python Flask API .

## TTD-workshop repo is a simple API written using python Flask and Graphql using the graphene library with focus on testing queries and mutations.

## Required Features
  * Test Query
  * Test Mutations (Create,Update and Delete)
  * Test Snapshots

  ## Installation
First clone this repository
```
$ git clone https://github.com/owenbob/TDD-workshop.git
$ cd TDD-workshop
```
Create virtual environment and install it
```
$ virtualenv env
$ source/env/bin/activate
```
Then install all the necessary dependencies
```
pip install -r requirements.txt
```

## Run the application
At the terminal or console type
```
python app.py
```
## Run tests
Set `APP_SETTINGS` to testing
```
export APP_SETTINGS=testing
```
To run tests run this command at the console/terminal
```
pytest -vv
```

##Python Version Used
```
Python 3.6
```
## Do share you thoughts and ideas  because together we learn more. 