# _api
this is a simple api that can display list of available drivers and create them and filter them using driver's email, mobile_number, langeuage and truck's number_plate
access "/myapi/driver" to create a driver and after create one you can display the drivers with the same endpoint 
access "/myapi/driver/id"to view a single driver for example "myapi/driver/1" to display the driver with id = 1 

****libraries used*****     
serializers: to be able to deal with model data through convert the object to format where we can store them and filter them and apply methods on them  
generics filters:to use its method where we can view the the list of drivers and filter to enable searching through drivers deatils 
     
improvments****
we can add some features in term of security we can allow access the api via token which will be like a key to access it 
we can add more models like the users model and set the relations between the driver and the others model accordingly 

Production consideration***
database conncation 
modules conflictions 
and we should turn off debugging mode 

Assumptions**

I assume that one driver can have many trucks when I desgined the models 
