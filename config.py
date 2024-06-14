from .logger import log

import yaml

class configloader:
    def __init__(self, type):
        mapping = {
            "config": ("config.yml"),
            "edition": ("edition-configuration.yml"),
            "sources": ("upstream-sources.yml")
        }
        if type in mapping:
            self.file = open(mapping[type], 'r')
        else:
            log.fail(f"Invailid mapping for loading '{type}'")
            exit()

    def load(self):
        return yaml.safe_load(self.file)

       
