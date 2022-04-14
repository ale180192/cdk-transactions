import os


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 54321 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", "password")
    user, db_name = "user", "user"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

def get_sqlite_uri(base_dir):
    host = os.environ.get("DB_HOST", "localhost")
    port = 54321 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", "password")
    user, db_name = "user", "user"
    path_db = os.path.join(base_dir, "db.sqlite3")
    return f"sqlite:////{path_db}"