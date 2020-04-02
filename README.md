# my_wildfire_bot

Technical test that consists on creating a bot that determinates origin date of wildfires.
This repository is a REST API that corresponds to the backend.

To run the app, you will need to:

1. Create a venv folder:

```
$ python3 -m venv venv
```

2. Activate venv:

```
$ source venv/bin/activate
```

3. Install dependencies:

```
$ pip install -r requirements.txt
```

4. Run the app:

```
python app.py
```

To try the API, you can use Postman with the following endpoints:

1. POST:
   http://127.0.0.1:5000/images

   Body example:

   {
   "longitude": -120.70418,
   "latitude": 38.32974,
   "begin_date": "2017-01-01",
   "end_date": "2020-01-01"
   }

2. GET:
   http://127.0.0.1:5000/images

3. POST:
   http://127.0.0.1:5000/answer

   Body example:

   {
   "answer":"n"
   }
