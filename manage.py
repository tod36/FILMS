#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import export as export

import movies


def main():
    """Run administrative tasks."""
    # os.environ['DJANGO_SETTINGS_MODULE'] = 'films.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'films.settings')
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# export DJANGO_SETTINGS_MODULE = movies.settings

if __name__ == '__main__':
    main()

# if __name__ == "__main__":
#     print("Hello, World!")
# def DJANGO_SETTINGS_MODULE():
#     return None
