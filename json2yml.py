from mando import command, main
import json
from ruamel.yaml import YAML

@command
def json2yml(in_file, out_file):


    yaml = YAML(typ="safe")
    yaml.default_flow_style = False
    with open(in_file, "r", encoding="utf-8") as i:
        data =json.load(i)

    with open(out_file, "w", encoding="utf-8") as o:
        yaml.dump(data, o)

    print("job done")


if __name__ == '__main__':
    main()
