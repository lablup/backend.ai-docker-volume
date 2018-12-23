from ipaddress import ip_address
from pathlib import Path
import subprocess

from bottle import app as bottle_app
import click
import docker
from waitress import serve

PLUGINNAME = 'lablup/backend.ai-docker-volume'
SOCKFILE = 'baivolume.sock'


def get_sock_path():
    """
    Compose socket directory.
    """
    try:
        sock_path = Path('/run/docker/plugins')
        if not sock_path.exists():
            sock_path.mkdir(parents=True)
        sock_path = sock_path / SOCKFILE
    except docker.errors.NotFound:
        pass
    return sock_path


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def main():
    """
    Command line interface for Lablup's docker volume plugin.
    """
    sock_path = get_sock_path()
    serve(bottle_app, unix_socket=sock_path, unix_socket_perms='660')


if __name__ == '__main__':
    main()
