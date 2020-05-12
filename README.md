# Capstone Project
## Casting Agency
This project is the capstone project of the Full Stack Developer Nano Degree by Udacity. The goal of this project is to deploy a Flask application to Heroku with Role-Based Access Control(RBAC) using Auth0, a third-party authentication system.

I decided to implement a RESTful for a Casting Agency application that enables users to create/manage actors and movies.

## Getting Started
## API Reference
### Getting Started
- Base URL: This app is hosted on: (URL), or it can be run locally on http://0.0.0.0:8080
- Authentication: This version of the application requires authentication for all endpoints

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
  "success": False,
   "error": 400,
   "message": "Bad Request"
}
```
The API will return these error types when requests fail:
- 400: Bad Request
- 404: Not Found
- 422: Unprocessable
- 405: Method Not Allowed
- 500: Internal Server Error

If authentication is required, these error types will be returned when requests fail:
- 401 : Errors regarding authorization headers or token (i.e: "Token expired")
- 403: Permission not found
- 400: Invalid header
### Roles and Permissions
There are 3 roles:
- Casting Assistant: Can view actors and movies
- Casting Director: Can view actors and movies, add or delete an actor from the database, and modify actors or movies
- Producer: Have all permissions

### Endpoints
#### GET /actors (Casting Assistant, Casting Director, Producer)
- General: Returns a list of all actors objects and success value
- Sample:
```
{
  "actors": [
    {
      "age": 33,
      "gender": "Female",
      "name": "Angelina Jolie"
    },
    {
      "age": 23,
      "gender": "Female",
      "name": "Natalie Brown"
    }
  ],
  "success": true
}
```
#### GET /movies (Casting Assistant, Casting Director, Producer)
- General: Returns a list of all movies objects and success value
- Sample:
```
{
  "movies": [
    {
      "release date": "2019-07-07",
      "title": "Ava"
    },
    {
      "release date": "2010-12-10",
      "title": "Boba"
    }
  ],
  "success": true
}
```

#### POST /actors (Casting Director, Producer)
- General: Creates a new actor using JSON request parameters and returns success value, newly created actor
- Sample: Response for a request with following body {"name": "Brad P", "age": 45, "gender": "Male"} and the appropriate header: 

```
{
  "new actor added": {
    "age": 45,
    "gender": "Male",
    "name": "Brad P"
  },
  "success": true
}
```
#### POST /movies (Producer)
- General: Creates a new movie using JSON request parameters and returns success value, newly created movie
- Sample: Response for a request with following body {"title": "Avatar", "release_date": "2020-01-03"} and the appropriate header:
```
{
  "new movie added": {
    "release_date": "2020-01-03",
    "title": "Avatar"
  },
  "success": true
}
```
#### DELETE /actors/<<int:id>> (Casting Director, Producer)
- General: Deletes an actor from the database by id and returns success value and id of the deleted actor
- Sample: Response for a request to delete an actor with id=2 and the appropriate header:
```
{
  "deleted": 2,
  "success": true
}
```
#### DELETE /movies/<<int:id>> (Producer)
- General: Deletes a movie from the database by id, returns success value and id of the deleted movie
- Sample: Response for a request to delete a movie with id=2 and the appropriate header:
```
{
  "deleted": 2,
  "success": true
}
```
#### PATCH /actors/<<int:id>> (Casting Director, Producer)
- General: Modifies an actor by id using JSON request parameters and returns success value and id of the modified actor
- Sample: Response for a request to modify an actor with id=3, with the following body {"name": "Tien Le","age": "22","gender": "Female"} and the appropriate header:
```
{
  "success": true,
  "updated": 3
}
```
#### PATCH /movies/<<int:id>> (Casting Director, Producer)
- General: Modifies a movie by id using JSON request parameters; returns success value and id of the modified movie
- Sample: Response for a request to modify a movie with id=3, with the following body{"title": "Mat Biec", "release_date": "2020-01-02"} and the appropriate header:
```
{
  "success": true,
  "updated": 3
}
```
## Authors
Tien Le
## Acknowledgements
I would like to thank Udacity for the idea suggestion of this project
