# Backend

## Prerequisites

```bash
pip3 install fastapi
pip3 install "uvicorn[standard]"
```

## Run

```bash
# Inside your api directory run the following command
uvicorn main:app

# for development, use --reload
uvicorn main:app --reload
```

This runs the server at [localhost:8000](http://localhost:8000) and API documentation can be found at [localhost:8000/docs](http://localhost:8000/docs)