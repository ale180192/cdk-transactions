import os


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 54321 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", "password")
    user, db_name = "user", "user"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

def get_sqlite_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 54321 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", "password")
    user, db_name = "user", "user"
    return f"sqlite:////db.sqlite3"