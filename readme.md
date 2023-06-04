# Backend

## Prerequisites

Setup a new python virtual environment
```
cd api
pip3 -m venv .venv
```

And activate the virutal environment

For MacOs
```bash
source .venv/bin/activate.fish
```

For Windows
```powershell
env/Scripts/Activate.ps1 
```

Then, install the dependencies using
```bash
pip3 install -r requirement.txt
```

**NOTE: VSCode can identify requirement.txt as pip file and prompt to create a 
virtual enviroment**

## Run

```bash
# Inside your api directory run the following command
uvicorn main:app

# for development, use --reload
uvicorn main:app --reload
```

This runs the server at [localhost:8000](http://localhost:8000) and API documentation can be found at [localhost:8000/docs](http://localhost:8000/docs)