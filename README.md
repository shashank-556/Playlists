# Playlists

This is a the backend for a simple web application in which users can create and manage public and private playlists.

## Installation 

Clone the repo

```bash
# clone the repo
$ git clone https://github.com/shashank-556/Playlists.git

# change the working directory to MessageBoard
$ cd Playlists
```

### Virtual Environment

First create a virtual environment using venv

```bash
$ python3.8 -m venv env

# activate the virtual environment
$ source env/bin/activate
```

### Setup

Create a json file with the name *secrets.json* to store the secret key that will be used to sign JWT tokens. The *secrets.json* file 

```json
{"SECRET_KEY":""}
```
You can create a secure random secret key in bash using the following command 

```bash
openssl rand -hex 32
```
### Requirements

Install all the requirements when the virtual environment is active
```bash
pip install -r requirements.txt
```

## Documentation 
Run the server on localhost using 
```bash
uvicorn main:app
```
Go to localhost:8000/docs in your browser to see the documentation.

