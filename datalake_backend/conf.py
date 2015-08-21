import configargparse

CONFIG_FILE = '/etc/datalake-backend.conf'

config_parser = configargparse.ArgParser(default_config_files=[CONFIG_FILE])

config_parser.add('-t', '--dynamodb-table',
                  help=('dynamodb table in which to store datalake records'),
                  env_var='DL_DYNAMODB_TABLE')

config_parser.add('-r', '--aws-region',
                  help=('region to use for aws services (e.g., s3, dynamodb)'),
                  env_var='DL_AWS_REGION')

config = config_parser.parse_args(args=[])

def get_config():
    return config
