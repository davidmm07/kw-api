# kw-api

The API kw-api, built with FastApi, perform basic MongoDB operations with Motor and Beanie.


### :pick: Previous Requirements
* Python
* Pip
* Virtualenv
* [Fast Api](https://fastapi.tiangolo.com/).

### :pick: Other tools used

* [Beanie](https://beanie-odm.dev/)
* [Motor-asyncio] (https://motor.readthedocs.io/en/stable/tutorial-asyncio.html)
* [cdk] (https://docs.aws.amazon.com/cdk/v2/guide/home.html)
## How to run

## Installation dependencies

```bash
 pip install --no-cache-dir --upgrade -r /app/requirements.txt
```
add environment variables
```bash
 cd app/
 touch .env
```

### Ways of running the api
#### 1. Run with uvicorn

```bash
 uvicorn app.main:app --reload
```

#### 2.Run with docker :whale:


1. Move to the folder
```sh
cd app/
```

2. Run container and check logs with:
```sh
docker-compose up --d && docker-compose logs -f
```

4. Verify that the containers are running
```sh
docker ps 
```
### Testing with pytest

1. Run the following command
```sh
  pytest
```

### Swagger section

1. Go to domain below
```sh
 localhost:8000/docs 
```
2. Check endpoints /smallest and /stats

