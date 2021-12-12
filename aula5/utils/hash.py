import hashlib
from passlib.hash import pbkdf2_sha256


def hash_password_passlib(password: str) -> str:
    """encrypt user password using passlib

    Args:
        password (str): user password

    Returns:
        str: password encrypted
    """
    return pbkdf2_sha256.hash(password)


def verify_hash_password_passlib(password: str, hash: str) -> bool:
    """check if password is correct using passlib

    Args:
        password (str): user password
        hash (str): user password encrypted

    Returns:
        bool: True if correct password else False
    """
    return pbkdf2_sha256.verify(password, hash)


def hash_password_hashlib(password: str) -> str:
    """encrypt user password using hashlib

    Args:
        password (str): user password

    Returns:
        str: password encrypted
    """
    return hashlib.md5(password.encode('utf-8')).hexdigest()


def verifyhash_password_hashlib(password: str, hash: str) -> bool:
    """check if password is correct using hashlib

    Args:
        password (str): user password
        hash (str): user password encrypted

    Returns:
        bool: True if correct password else False
    """
    return hashlib.md5(password.encode('utf-8')).hexdigest() == hash
