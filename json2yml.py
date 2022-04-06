import json

from ruamel.yaml import YAML

def json2yml(in_file, out_file):
#in_file = "json_in.json"
#out_file = "yaml_out.yml"

    yaml = YAML(typ="safe")
    yaml.default_flow_style = False
    with open(in_file, "r", encoding="utf-8") as i:
        data =json.load(i)

    with open(out_file, "w", encoding="utf-8") as o:
        yaml.dump(data, o)

json2yml("json_in.json","yaml_out.yml")