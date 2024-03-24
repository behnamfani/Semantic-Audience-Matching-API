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
The response should be:
```
"message": "{'sim': 0.5914979, 'label_id_long': 50307010100, 'label_id': 503070101, 'parent_id': 5030701, 'segment_description': 'Frequency of consuming food and drinks', 'label_name': 'Purchases & Consumption | Food & Drink | General Food | Ethic | Arabic Food'}"
```

## Installation
1. Clone the repository: ```git clone https://github.com/behnamfani/Semantic-Audience-Matching-API.git```
2. Navigate to the directory of the cloned repo and build docker: ```docker build -t api-app .```
3. Start the container: ```docker run -d --name api-container -p 8000:8000 api-app```
  * It should build the API as well. For the first time it takes some time to download the language model.
  * If the API did not build correctly, it can start alternavetivly in the container's bash using  ```uvicorn API:app --reload --host 0.0.0.0```
4. In a terminal, open the container's bash: ```docker exec -t -i api-container /bin/bash```
5. In the container bash, navigate to the scripts folder and run modify API_Call.py with the required payload and run it: ```python3 API_Call.py```

## License
This project licensed under the MIT license

