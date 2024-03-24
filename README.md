# Semantic-Audience-Matching-API
Find the best possible semantic match from a source list given a description of an audience segment

## Description
The aim of the project is to create an API when given segment descriptions from different audiences, it find the best match from source_list and returns it.
The API.py method in the scripts folder uses the FastAPI library to create the /match endpoint. It is executed using "uvicorn API:app --reload" command in the terminal and creates the endpoint on  http://127.0.0.1:8000 and the documentation of the API can be found on  http://127.0.0.1:8000/docs after the creation of the API (message: "Application startup complete" in terminal). Running the API will also call the create an object from the Semantic class in Semanic_Match.py in the src folder which uploads the language model and the required datasets. 
Then the API_Call.py can be used to send requests to "http://127.0.0.1:8000/match" endpoint with different descriptions in the payload such as:
```
payload = {"input_segments": ["Market -> food -> vegan -> tufo"]}
```
In the API.py, this payload is passed to the find_match method of the Semantic class to find the best match where it is encoded and compared with the embeddings of the source_list using cos-sim (more info: [reports](reports))

## Installation


## License
This project licensed under the MIT license

