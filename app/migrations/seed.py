from app import create_app, db

import core.models as core_models

app = create_app()
with app.app_context():
    db.session.commit()
    db.drop_all()
    db.create_all()
    db.session.commit()

    count = core_models.Counter(name='My first counter', count=10)
    db.session.add(count)
    db.session.commit()
