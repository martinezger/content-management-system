[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/martinezger/content-management-system)

# Simple Content Management System

This project aims to create a system for administration of articles and publishers.
Things you can do:

- Create, read, update and delete Publisher.
- Create, read, update and delete Articles.
- Set articles as headlines.
- Add a picture for every Article.

# Install 

For installing this software you need to do:

## Check python version
This project was written with python 3.8.0 so I strongly suggest you to test with this version or higher just to not have any compatibility issues.

How I check my python version, 

in *nix systems:

```bash
> python --version
> Python 3.8.0
```

in windows:

```bash
c:\> py --version
c:\> Python 3.8.0
```

## Install Dependencies

In order to install dependencies you need to run `pip install`, make sure you are in the project folder and you can see the `requirements.txt` file when you do a `ls` or `dir`:

```bash
> pip install -r requirements.txt
```
This last will return a bunch of stuff in the terminal.

`Some operative systems will required you to use pip3 instead of pip `

## Setting Up the Django Application

Once you finish the dependencies installation you need to run some django commands.

### Migrations

Initialize the database
*nix:
```bash
> python mananage.py migrate
```
windows:
```bash
c:\> py mananage.py migrate
```

### Run the test server

```bash
> python mananage.py runserver
```
windows:
```bash
c:\> py mananage.py runserver
```
Go to localhost:8000/

to have access to the app.

If everthing goes well you should be able to open the browser and see the application run

