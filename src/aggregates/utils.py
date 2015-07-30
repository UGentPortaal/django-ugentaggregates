NO_DEFAULT = object()


def has_field(obj, field):
    """Check if an object has a certain attribute, or if a dictionary
    has a certain key.
    """
    if isinstance(obj, dict):
        return field in obj
    else:
        return hasattr(obj, field)


def get_field(obj, field, default=NO_DEFAULT):
    """Return the value for a certain attribute or a certain key.
    """
    try:
        if isinstance(obj, dict):
            return obj[field]
        else:
            return getattr(obj, field)
    except (AttributeError, KeyError):
        if default == NO_DEFAULT:
            raise
        else:
            return default
