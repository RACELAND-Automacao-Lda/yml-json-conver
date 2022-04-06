import json

from ruamel.yaml import YAML

def yaml2json(in_file,out_file):
#in_file = "yaml_in.yml"
#out_file = "json_out.json"

    yaml = YAML(typ="safe")

    with open(in_file, "r", encoding="utf-8") as i:
        data =yaml.load(i)

    with open(out_file, "w", encoding="utf-8") as o:
        json.dump(data, o, indent=4, ensure_ascii=False)

yaml2json("docker-compose.yml","docker-compose_out.json")