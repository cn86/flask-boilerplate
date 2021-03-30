from core.extensions import db

import core.models as core_models


def get_or_create_counter(counter_name):
    counter = db.session.query(core_models.Counter)\
        .filter(core_models.Counter.name == counter_name)\
        .one_or_none()

    if not counter:
        counter = core_models.Counter(name=counter_name)
        db.session.add(counter)
        db.session.commit()

    return counter


def increment_counter(counter):
    counter.count += 1
    db.session.add(counter)
    db.session.commit()

    return counter
