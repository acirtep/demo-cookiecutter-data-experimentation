import duckdb
from demo_cookiecutter_data_experimentation.app import get_data
from demo_cookiecutter_data_experimentation.settings import DATA_LOCATION


def test_get_data():
    duckdb_conn = duckdb.connect()
    df = get_data(duckdb_conn, file=f"{DATA_LOCATION}/example_data.csv")
    assert df.shape[0] == 2
