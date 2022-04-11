import time
import psycopg2
from transactions import config


def wait_for_postgres_to_come_up():
    deadline = time.time() + 10
    while time.time() < deadline:
        try:
            return psycopg2.connect(config.get_postgres_uri())
        except psycopg2.OperationalError:
            time.sleep(1)
    raise Exception("Postgres never came up")


if __name__ == "__main__":
    wait_for_postgres_to_come_up()
