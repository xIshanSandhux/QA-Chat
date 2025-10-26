This is the backend. will be filling the readme file as the project progresses.

To isolate the backend created a venv using the following command: python -m venv venv
Command to start the backend python vitural env: venv\Scripts\activate
using python and not python3

fastapi dev main.py from backend folder to start the fastapi server

using redis for the keeping track of the chat history in the backend.
currently running on local host so pulling the redis docker image and running on local host
command to run the docker image: docker run -d --name redis -p 6379:6379 redis:<version>
<version> is basically the tag, currently using the 'latest' tag