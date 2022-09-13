from utils import logged
import argparse
import logging

@logged
def do_something(name):
    print("hello name")
    return "gobble"


def main():
    do_something("hello")
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='logging.py')
    parser.add_argument('-log',
                     '--loglevel',
                     default='warning',
                     choices=['debug', 'info', 'warning'],
                     help='Provide logging level. Example --loglevel debug, default=warning')

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel.upper())
    logging.info( 'Logging now setup.' )
    main()