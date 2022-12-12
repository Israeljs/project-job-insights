from src.counter import count_ocurrences


def test_counter():
    '10 - Implemente um teste para a função count_ocurrences'
    assert count_ocurrences('src/jobs.csv', 'work') == 14174
