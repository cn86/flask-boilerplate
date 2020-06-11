import pytest

import core.models as core_models


@pytest.fixture
def counter(db, clear_db):
    count = core_models.Counter(name='My first counter', count=10)
    db.session.add(count)
    db.session.commit()

    return count
