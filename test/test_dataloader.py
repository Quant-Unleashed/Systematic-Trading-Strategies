from src.data.data_loader import DataLoader


def test_loader_initialization():

    loader = DataLoader(["SPY","TLT"], "2020-01-01", "2021-01-01")

    assert loader is not None
