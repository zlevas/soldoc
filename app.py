#!/bin/env/python3

from jinja2 import Environment, FileSystemLoader, select_autoescape
import read_json

if __name__ == "__main__":
    env = Environment(
        loader=FileSystemLoader('./templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    doc = read_json.docFromJson()
    contract_name = doc["title"]
    
    template = env.get_template('template.html')
    print (template.render(contract_name=contract_name, go='here'))
