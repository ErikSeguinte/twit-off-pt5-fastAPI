import secrets

#
# import the CryptContext class, used to handle all hashing...
#
from passlib.context import CryptContext
from twit_off_pt5.core.models import Admin, db

#
# create a single global instance for your app...
#
pwd_context = CryptContext(
    # Replace this list with the hash(es) you wish to support.
    # this example sets pbkdf2_sha256 as the default,
    # with additional support for reading legacy des_crypt hashes.
    schemes=["argon2", "pbkdf2_sha256", "des_crypt"],
    # Automatically mark all but first hasher in list as deprecated.
    # (this will be the default in Passlib 2.0)
    deprecated="auto",
    # Optionally, set the number of rounds that should be used.
    # Appropriate values may vary for different schemes,
    # and the amount of time you wish it to take.
    # Leaving this alone is usually safe, and will use passlib's defaults.
    ## pbkdf2_sha256__rounds = 29000,
)


def create_api_key():
    key = secrets.token_urlsafe()
    return key


def _create_admin():
    key = create_api_key()
    admin = Admin(username="admin", api_key = pwd_context.hash(key))
    db.session.add(admin)
    db.session.commit()
    return key




