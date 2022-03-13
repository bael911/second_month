from package import models, config

if config.starting:
    persons = []
    for person in config.fake_db:
        person.append(
            models.person(person.username, person.salary)
        )