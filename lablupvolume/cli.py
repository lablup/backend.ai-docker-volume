import click
from ipaddress import ip_address

from plugin import run_server

@click.option('-H', '--host', type=str, default='127.0.0.1', show_default=True,
              help='Host address of the plugin server.')
@click.option('-p', '--port', type=int ,default=1331, show_default=True,
              help='Host port of the plugin server.')
@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def main(host, port):
    """
    Command line interface for Lablup's docker volume plugin.
    """
    run_server(host, port)


if __name__ == '__main__':
    main()
