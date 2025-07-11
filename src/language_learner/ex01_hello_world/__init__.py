import getpass


def hello(name: str = None):
    """Exercise to print 'hello {NAME}' """

    print(f'Hello {name or getpass.getuser()}')