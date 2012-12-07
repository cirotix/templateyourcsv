templateyourcsv
===============

This is the code that runs http://example.com, a simple csv templating engine.

It takes in input a csv url (from a Google doc for exemple), a Jinja2 template 
and render each row of the csv file with the template.

This is only a few lines written with Bottle and Jinja2


## Installation

* Create a virtualenv and activate it

  ```
  $ virtualenv --no-site-packages .
  $ source bin/activate
  ```

* Install the packages with pip

  ``` 
  $ pip install -r REQUIERMENTS.txt
  ``` 

* Run the server
  ```
  $ python run.py
  ```
