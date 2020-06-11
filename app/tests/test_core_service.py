import core.service as core_service


def test_get_or_create_counter_get_counter(counter):
    counter = core_service.get_or_create_counter(counter.name)
    assert counter.count == 10


def test_get_or_create_counter_create_counter(clear_db):
    counter = core_service.get_or_create_counter('My first counter')
    assert counter.count == 0


def test_increment_counter(counter):
    initial_count = counter.count

    counter = core_service.increment_counter(counter)

    final_count = counter.count

    assert final_count == initial_count + 1
