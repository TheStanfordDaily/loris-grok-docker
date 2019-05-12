from werkzeug.serving import run_simple
from webapp import create_app
import sys
from os import path

if __name__ == '__main__':
    project_dp = path.dirname(path.dirname(path.realpath(__file__)))

    sys.path.append(path.join(project_dp)) # to find any local resolvers

    app = create_app(config_file_path='/opt/loris/etc/loris2.conf')

    run_simple('0.0.0.0', 5004, app, use_debugger=True, use_reloader=True)