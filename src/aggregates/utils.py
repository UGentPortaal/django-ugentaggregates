NO_DEFAULT = object()  # Marker for missing default parameter.


def has_field(obj, field):
    """Check if an object has a certain attribute, or if a dictionary
    has a certain key.

    :param obj: the data object
    :type obj: object or dict
    :param field: the field name
    :type field: str
    :returns: True if the object has the field, False otherwise
    :rtype: bool
    """
    if isinstance(obj, dict):
        # Object is a dictionary.
        return field in obj
    else:
        # Object is an instance.
        return hasattr(obj, field)


def get_field(obj, field, default=NO_DEFAULT):
    """Return the value for a certain attribute or a certain key.

    :param obj: the data object
    :type obj: object or dict
    :param field: the field name
    :type field: str
    :param default: the default value (optional)
    :type default: object
    :returns: the field's value
    :rtype: object
    :raises AttributeError: if the object doesn't have the field
    :raises KeyError: if the dictionary doesn't have the field
    """
    try:
        if isinstance(obj, dict):
            # Object is a dictionary.
            return obj[field]
        else:
            # Object is an instance.
            return getattr(obj, field)
    except (AttributeError, KeyError):
        # Field is missing.
        if default == NO_DEFAULT:
            # Default parameter is missing; reraise the exception.
            raise
        else:
            # Return the default parameter.
            return default
