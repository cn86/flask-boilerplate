

def test_index(client):
    with client.get('/') as response:
        assert response.status_code == 200
        assert 'To create or increment a count, pass in a request argument' in str(response.data)


def test_index_existing_counter(client, counter):
    with client.get('/', query_string={'counter_name': counter.name}) as response:
        assert response.status_code == 200
        assert f'The {counter.name} counter is at {counter.count}' in str(response.data)


def test_index_new_counter(client, clear_db):
    counter_name = 'New counter'
    with client.get('/', query_string={'counter_name': counter_name}) as response:
        assert response.status_code == 200
        assert f'The {counter_name} counter is at 1' in str(response.data)
