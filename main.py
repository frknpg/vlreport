import logging

import flaskr


def main():
    logging.info('Report application running')
    app = flaskr.create_app()
    app.run()


if __name__ == '__main__':
    main()