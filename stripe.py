import stripe

# global api key
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

# per request api key
charge = stripe.Charge.retrieve(
  "ch_19yUdo2eZvKYlo2CQlMNMP5b",
  api_key="sk_test_4eC39HqLyjWDarjtT1zdp7dc"
)
charge.save() # Uses the same API Key.

customer = stripe.Customer.create()
print(customer.last_response.request_id)
