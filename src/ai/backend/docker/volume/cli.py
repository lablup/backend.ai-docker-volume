from ipaddress import ip_address
from pathlib import Path
import subprocess

from bottle import app as bottle_app
import click
import docker
from waitress import serve

PLUGINNAME = 'lablup/backend.ai-docker-volume'
SOCKPATH = 'baivolume.sock'


def get_sock_path():
    """
    Docker seems to search the plugin in /run/docker/plugins/<plugin_id>/<sock_name>
    (https://github.com/moby/moby/issues/31723#issuecomment-286391588).

    This function compose the correct socket directory by getting plugin's id info.
    """
    global SOCKPATH
    client = docker.from_env()
    try:
        plugin = client.plugins.get(PLUGINNAME)
        SOCKPATH = Path('/run/docker/plugins') / plugin.id / SOCKPATH
    except docker.errors.NotFound:
        pass
    return SOCKPATH


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def main():
    """
    Command line interface for Lablup's docker volume plugin.
    """
    sock_path = get_sock_path()
    serve(bottle_app, unix_socket=sock_path)


if __name__ == '__main__':
    main()
