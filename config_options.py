# 01 - Configuration file in order to retrieve YAML parameters
import yaml

class ConfigOptions():

    with open('config.yml', 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        base_url = 'https://' + cfg['url']
        web_d = cfg['webdriver']