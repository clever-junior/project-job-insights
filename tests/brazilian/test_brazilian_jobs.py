from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    result = read_brazilian_file(path)
    result_keys = result[0].keys()

    assert "title" in result_keys
    assert "salary" in result_keys
    assert "type" in result_keys
