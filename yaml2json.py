import json
from mando import command,main
from ruamel.yaml import YAML

@command
def yaml2json(in_file,out_file):

    yaml = YAML(typ="safe")

    with open(in_file, "r", encoding="utf-8") as i:
        data =yaml.load(i)

    with open(out_file, "w", encoding="utf-8") as o:
        json.dump(data, o, indent=4, ensure_ascii=False)
	
    print("job done")

if __name__ == '__main__':
    main()
