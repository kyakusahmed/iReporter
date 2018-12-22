[![Build Status](https://travis-ci.org/kyakusahmed/iReporter.svg?branch=challenge-2%2Fapi)](https://travis-ci.org/kyakusahmed/iReporter)
[![Coverage Status](https://coveralls.io/repos/github/kyakusahmed/iReporter/badge.svg?branch=challenge-2%2Fapi)](https://coveralls.io/github/kyakusahmed/iReporter?branch=challenge-2%2Fapi)
<a href="https://codeclimate.com/github/kyakusahmed/iReporter/maintainability"><img src="https://api.codeclimate.com/v1/badges/0a8553265327c7269155/maintainability" /></a>

# iReporter
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

[HEROKU LINK](https://irepo.herokuapp.com)


Features User side:

- Signup page using personal information.
- Login page using Email and Password
- create a red-flag record.
- create an intervention record
- delete a red-flag or intervention record
- add videos or image to either red-flag or intervention record
- add geolocation to either red-flag or intervention record
- view all user red-flag  or intervention records a user has created

User's profile where a User can view
- the number of red-flags/interventions that has been resolved
- the number of red-flags/interventions that has yet be resolved(in draft or under investigation states)
- the number of red-flags/interventions that has been rejected
- list of all red-flag/interventions records

As an Admin:

- i can change the status of a red-flag/intervention records
- i can see all the red-flag/intervention records by all users



### How to run the app


Make sure that python 3.6 is installed on your computer

Clone the repo
```
git clone "https://github.com/kyakusahmed/iReporter.git"
```
Change to the app directory
```
$ cd <directory-name>
```
Create a virtual enviroment
```
virtualenv (name)
```
Activate the virtualenv
```
For Windows:
	$ (virtualenv name)\scripts\activate, and  	
For Linux: 
 	$source(virtualenv name)/bin/activate
```
Install the required modules from the requirements.txt file 
```
$ pip install -r requirements.txt
```
Run the app
```
$ python run.py
```

| tasks               |    URLS                |  METHOD  |         PARAMS                   |   OUTPUT                          |
| ------------------- | -----------------------|----------|----------------------------------|-----------------------------------|
| get all redflags    | api/v1/redflags        |  GET     |   ---------------                | {'redflag': [], 'status': 200 }   |
|                     |                        |          |                                  |                                   |
|                     |                        |          |                                  |                                   | 
| get a specific      |  api/v1/redflags/      |  GET     |   redflag_id                     | {'redflag': [], 'status': 200}    |
| redflag             |  redflag_id            |          |                                  |                                   |
|                     |                        |          |                                  |                                   |
| user creates redflag| api/v1/redflags        |  POST    |   comment, createdBy, image,     | {'data': [{'message': 'redflag    |
|                     |                        |          |   location, type, video          |           added successfully',    |
|	              |		               |	  |                                  |           'redflag_id': id }],    |
|                     |                        |          |                                  |      'status': 201 }              |
|                     |                        |          |                                  |                                   |
|                     |                        |          |                                  |                                   |
|user updates redflag | api/v1/redflags/       |  PUT     |   comment                        | {'redflag': [{'message': 'comment |
|                     | redflag_id             |          |                                  | updated', 'redflag': redflag_id}],|
|                     |                        |          |                                  |            'status': 200 }        |
|                     |                        |          |                                  |                                   |
|                     |                        |          |                                  |                                   |


### How to run the Tests:

open the terminal,activate virtual enviroment in the iReport directory  and enter:
 ```
 $ pytest --cov
```




