# EECS441-Backend

# Requirements
1. Python 3.x

# Download Instructions
Clone the project
```
git clone https://github.com/roblkenn/EECS441-Backend.git
```
Navigate to the directory EECS441-Backend
```
cd EECS441-Backend
```
Dependencies
```
pip install flask
pip install azure-cosmosdb-table
```
Running Flask App in Development Mode
```
MacOSX/Linux:
  export FLASK_APP=__init__.py
  export FLASK_ENV=development
  flask run

Windows:
  Replace export with set
```

# File Structure
<pre>
.
├── README.md
├── __init__.py
├── auth.py
└── dataset.py
</pre>
## API Endpoints

/dataset
- get : Retrieve data for use in machine learning model training
- post : Add new datum
- delete : Remove datum

/market
- get : Retrieve listing information
- post : Create a new listing
- put : Update an existing listing
- delete : Remove a listing

/purchase
- get : Retrieve payment info for user
- post : Create a charge for user
- put : Update payment info for user
- delete : Remove payment info for user

## Reference Material
[Azure Table Storage Documentation](https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-how-to-use-python)

[Flask Documentation](http://flask.pocoo.org/docs/1.0/#)
