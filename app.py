import sys

from common.Configuration import Configuration
from jira import JIRA
import importlib

import argparse

FETCHER_CLASS = "fetcher.class"

EXECUTOR_CLASS = "executor.class"

USER_NAME = "user.name"
PASSWD = "password"

JIRA_URL = "jira.url"

parser = argparse.ArgumentParser()
parser.add_argument('-config_file', required=False, nargs=1, dest='config_file')
parser.add_argument('--conf', required=False, nargs=1, type=str, action='append', dest='kv_collection')

if __name__ == '__main__':
    args = parser.parse_args(sys.argv)
    config_file = args.config_file
    kv_collection = args.kv_collection
    conf_dict = dict()
    for kv in kv_collection:
        [k, v] = kv.split('=')
        conf_dict[k] = v

    config = Configuration(config_file)

    for k, v in conf_dict.items():
        config.set(k, v)

    config.print_conf()

    user = config.get(USER_NAME)[0]
    password = config.get(PASSWD)[0]
    jira_url = config.get(JIRA_URL)[0]
    jira = JIRA(jira_url, basic_auth=(user, password))

    fetcher_module = importlib.import_module('Fetcher.' + config.get(FETCHER_CLASS)[0])
    fetcher_class = getattr(fetcher_module, config.get(FETCHER_CLASS)[0])
    fetcher = fetcher_class(jira, config)
    objects = fetcher.fetch()
    print objects
    executor_module = importlib.import_module('Executor.' + config.get(EXECUTOR_CLASS)[0])
    executor_class = getattr(executor_module, config.get(EXECUTOR_CLASS)[0])
    executor = executor_class(jira, config)
    executor.execute(objects)
    print 'done'
