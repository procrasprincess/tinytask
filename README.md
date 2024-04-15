# tinytask

## Setup
- `npm create vite@latest frontend -- --template react`
- Frontend
  - `npm install`
  - `npm run dev`
- Backend
  - `pip3 install Flask`
  - ORM(object relational mapping): connects to a sql db > map entries into a python object
    -  `pip3 install Flask-SQLAlchemy`
   - COR(cross origin request): send requests to backend from a different url & handles cors related errors
     - `pip3 install flask-cors`

## Dev

### Backend
- `config`: basic config, db connection
- `models`: db models
- `main`: main routes/endpoints