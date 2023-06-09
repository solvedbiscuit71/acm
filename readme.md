# Backend

## Prerequisites

### Python Environment

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

### CLI

To load menu data into the database, run
```bash
python3 script.py --menu
```

To load waiter's credentials into the database, run
```bash
python3 script.py --waiter
```

To initiate the sequence generator for orders, run
```bash
python3 script.py --order
```

To generate a bcrpyt salt, run
```bash
python3 script.py --salt
```

Or, to run all the above command
```bash
python3 script.py --all
```


### Environment variables

```env
ALGORITHM=HS256
ORIGINS=<list-of-origins>
SALT=<salt-for-hashing>
SECRET=<jwt-secret>
WAITER_SECRET=<password-for-waiter>
SEQ_START=<integer>
```

## Run

```bash
# Inside your api directory run the following command
uvicorn main:app

# for development, use --reload
uvicorn main:app --reload
```

This runs the server at [localhost:8000](http://localhost:8000) and API documentation can be found at [localhost:8000/docs](http://localhost:8000/docs)

# Frontend

## Prerequisites

- Nodejs
- NPM

Run the following command to install the node packages,
```bash
cd frontent
npm install
```

## Run

```bash
# for development purpose
npm run dev

# for production purpose
npm run build
npm run preview
```

This runs the frontend server at [localhost:8080](http://localhost:8080) for both development and production