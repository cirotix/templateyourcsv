# -*- coding: utf-8 -*-
import jinja2 as jinja
import csv

from bottle import Bottle, run, static_file, request

from urllib import urlopen


app = Bottle()

env= jinja.Environment()
env.loader= jinja.FileSystemLoader("template")

def csv_to_dict(url):
    """
    Convert a csv file, open from a remote url in a list of dicts
    The keys of each dict are the name of the column, from the header
    """
    headers = None
    content = []
    reader= csv.reader( urlopen(url) )

    for row in reader:
        if reader.line_num == 1:
            # If we are on the first line, create the headers list from the first row
            headers = row
        else:
            """
            Otherwise, the key in the content dictionary is the first item in the
            row and we can create the sub-dictionary by using the zip() function.
            """
            row_dict = {}
            for idx, val in enumerate(headers):
                row_dict[val] = unicode(row[idx], "utf8")
            content.append(row_dict)
    return content


def render_csv(data_dict, template):
    template = jinja.Template(template)
    rendered = template.render(rows=data_dict)
    return "<!-- Genrated by Template your CSV -->" + rendered


@app.get('/')
@app.post('/')
def index():

    url = request.forms.get('url')

    data_template = request.forms.get('template') 
    
    # convert data_template to unicode
    data_template = data_template if data_template else ""
    data_template = unicode(data_template, "utf8")

    rendered = ""
    

    if url:
        data_dict = csv_to_dict(url)
        if data_template:
            rendered = render_csv(data_dict, data_template)

    
    template= env.get_template("home.html")

    return template.render(
            url=url,
            template=data_template,
            rendered = rendered
            )


@app.route('/static/<basedir>/<filename>')
def server_static(basedir, filename):
    return static_file(filename, root='/home/cirotteau/dev/csvtohtml/csvtohtml/template/static/' + basedir + '/')

run(app, host='localhost', port=8000)
