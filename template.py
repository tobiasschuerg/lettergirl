import yaml


def replace_placeholders(section, data: dict):
    section = section.replace('\n', ' \\\\\n')  # prepare linebreaks for latex
    for key, value in data.items():
        section = section.replace(f'[{key}]', value)
    return section


def prepare_template(template_file, data: dict):
    with open(template_file, "r", encoding="utf-8") as file:
        # Load the YAML data
        template = yaml.safe_load(file)

    params = template.pop("params")
    for param in params:



        if param['key'] not in    data.keys():



            raise KeyError(str(param) + " missing")

    with open('letter.tex', encoding="utf-8") as f:
        letter = f.read()

    template.pop("metadata")
    for key, value in template.items():
        modified_value = replace_placeholders(value, data)
        letter = letter.replace(":" + key, modified_value)

    return letter
