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

To load item's data into the database, run
```bash
python3 script.py --item
```

To generate a bcrpyt salt, run
```bash
python3 script.py --salt
```

### Environment variables

For token generation, we need a SECRET and ALGORITHM. add the following inside
`schema/.env` file
```env
SECRET=<your-secret>
ALGORITHM=HS256
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