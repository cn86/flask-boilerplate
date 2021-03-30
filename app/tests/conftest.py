import fsspec

import pytest

from app import create_app
from core.extensions import db as _db

# Add all fixture files here.
pytest_plugins = [
    'tests.fixtures.counter'
]


@pytest.fixture(scope='session', autouse=True)
def app(request):
    _app = create_app('test')
    ctx = _app.app_context()
    ctx.push()
    return _app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(scope="session")
def db(app):
    _db.app = app
    _db.create_all()

    yield _db

    _db.drop_all()


@pytest.fixture(scope="function")
def clear_db(db):
    # Resets all database state between tests. Auto increment IDs will not be reset.
    connection = db.engine.connect()
    transaction = connection.begin()
    options = dict(bind=connection, binds={})

    session = db.create_scoped_session(options=options)
    db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()


@pytest.fixture(scope='function')
def clean_fs():
    ''' Delete all files in the in-memory test filesystem.
    '''
    yield
    fs = fsspec.filesystem('memory')
    for file in fs.find('/'):
        fs.delete(file)


@pytest.fixture(scope='function')
def test_fs(clean_fs):
    return fsspec.filesystem('memory')
