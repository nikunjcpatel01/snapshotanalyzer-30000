import click

@click.group()
def group1():
    """commands for group1"""

@group1.command("command1")
@click.option('--count',default=1,help='count of servers')
def start_server():
    "function to Start server"
    print("start server")
    return

@group1.command("command2")
@click.option('--count2',default=1,help='count2 of servers')
def command2_server():
    "function to command2 command2"
    print("stop server")
    return

@click.command()
def stop_server():
    "function to Stop server"
    print("stop server")
    return

if __name__ == '__main__':
    print("Hello")
    group1()
