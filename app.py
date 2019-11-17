import sys

from common.Configuration import Configuration
from jira import JIRA
import importlib

FETCHER_CLASS = "fetcher.class"

EXECUTOR_CLASS = "executor.class"

USER_NAME = "user.name"
PASSWD = "password"

JIRA_URL = "jira.url"

if __name__ == '__main__':
    if len(sys.argv) == 2:
        config = Configuration(sys.argv[1])
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
    else:
        config = Configuration()