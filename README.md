# ImageWebApi
Simple web api for manipulating images using python and django <br>
Project created for increasing django and python skills

## Installation
Using package manager import required packages
```bash
pip install -r requirements.txt
```

After this create db files by migration command

```bash
python3 imageapi/manage.py migrate
```

And thats all!

## Usage

To run server run specified command

```bash
python3 imageapi/manage.py runserver
```

By default server runs on port 8000

## API

Server has following endpoints:
* POST: server_address:8000/images/ <br> upload image; required fields: image_title: str, image_url: Image
<br>
  To upload fields you have to use 'form-data' as request with according fields
<br><br>
* GET,PUT,PATCH,DELETE: server_address:8000/images/(id) <br>
Get, modify or delete existing image in database. There is a path param in curly brackets as image id
<br><br>
* GET,PUT,PATCH,DELETE: server_address:8000/images/(id)/image <br> 
Returns rendered image as response in specified image id
<br><br>
* GET: server_address:8000/images/(id)/image/crop/(start_x)/(start_y)/(end_x)/(end_y)
Crop image(without modifications on stored one) and return as rendered image <br>
  Could return response with 400 if specified parameters are invalid 
  
## Plans for future 
- [ ] swagger documentation generation
- [ ] create Dockerfile for containerization 
- [ ] improve image manipulation endpoints
- [ ] consider creating front application
## License
[MIT](https://choosealicense.com/licenses/mit/)
