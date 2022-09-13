import logging
import argparse

def foo():
    print("Regular print statement")
    logging.debug("logging.debug print statement")
    logging.info("Logging.info statement")

def main():
    foo()
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
