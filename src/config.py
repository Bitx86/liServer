import yaml
from pathlib import Path

class Config:
    # Valid variables for config
    __var__ = ('ip', 'buffer_size', 'port', 'log_to_file', 'log_file_name')
    
    def __init__(self, config_file: str):
        self.file = config_file
        self.data = self.__open_config__()
        self.validate_config()

    def __open_config__(self):
        path = Path(self.file)
        if not path.exists():
            print(f'Error: Configuration file {self.file} does not exist')
            exit(1)   

        try:
            with open(self.file, 'r') as file:
                config = yaml.safe_load(file)
                return config

        except yaml.YAMLError as e:
            print(f'Error: Failed while parsing YAML configuration: {e}')
            exit(1)

        except Exception as e:
            print(f'Error: Unexpected error reading configuration: {e}')
            exit(1)


    def validate_config(self):
        server_keys = self.data.get('server', {}).keys()

        # List of keys not in __var__ (or incorrect keys in config)
        invalid_keys = [key for key in server_keys if key not in self.__var__] 
        
        if invalid_keys:
            print(f'Error: Invalid configuration keys found: {invalid_keys}')
            exit(1)

    # Return the value of a key in the yaml config
    def getVar(self, v):
        return self.data.get('server', {}).get(v)
