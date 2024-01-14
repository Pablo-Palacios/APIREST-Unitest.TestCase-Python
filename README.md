Hi, this is my first REST API created using Flask. It's a basic API that supports the methods GET, POST, PUT, and DELETE.
In this API, I've implemented a table from a database using Flask-SQLAlchemy to store user data (ID - username - job) in a MySQL database. 
For organizing the model of the table, I've utilized Flask-Marshmallow with fields ("id - username - job"). You can either call a single user or retrieve all of them using the provided methods.
With these methods, you can save a new user, retrieve a user by ID, update data for any user, or delete a user.

For testing, I've employed the Unitest.TestCase library with several individual tests to ensure that all methods work correctly. 
In a simple test, I use a request and with an assertEqual, I compare the status code for the HTTP response from the API.
