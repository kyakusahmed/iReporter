# iReporter
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention



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

| tasks               |    URLS                |  METHOD  |         PARAMS                                |   OUTPUT             |
| ------------------- | -----------------------|----------|-----------------------------------------------|----------------------|
| get all redflags    | api/v1/redflags        |  GET     |   ---------------                             | list of dictionaries |
|                     |                        |          |                                               |                      | 
| get a specific      | api/v1/redflags/id     |  GET     |  id                                           | list                 |
| redflag             |                        |          |                                               |                      |
|                     |                        |          |                                               |                      |
| user posts a parcel | api/v1/redflags        |  POST    | client_id, body, location                     | messsage that says   | 
|                     |                        |          |                                               | "redflag added       |
|	                    |			                   |	        |                                               |       successfully"  |
|                     |                        |          |                                               |                      |
|user updates redflag | api/v1/redflags/id     |  PUT     | Body                                          |  message that says   |
|                     |                        |          |                                               |  "redflag updated"   |


### How to run the Tests:

 open the terminal,activate virtual enviroment in the iReport directory  and enter:
 ```
 $ pytest --cov
```



