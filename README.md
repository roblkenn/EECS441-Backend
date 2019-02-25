# EECS441-Backend



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

/analytics
- get : Retrieve an analytics event
- post : Create a new analytics event
- delete : Remove an analytics event

/auth/{login,logout,register}
- post: login, logout, register a user
