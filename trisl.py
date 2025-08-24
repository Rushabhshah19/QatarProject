from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient("YOUR_TOKEN")
db = client.get_database_by_api_endpoint(
  "https://8727c016-47a5-428c-b709-586730434296-us-east-2.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")