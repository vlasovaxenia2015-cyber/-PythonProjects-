from src.processing import sort_by_date, filter_by_state

def test_filter_by_state(transactions, filter_data):
    assert filter_by_state(transactions) == filter_data


def test_sort_by_date(transactions, sort_data):
    assert sort_by_date(transactions) == sort_data