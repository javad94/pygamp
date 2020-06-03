from .transport import send


def custom_dimension(cid, index: str, value: str):
    """Populate a Google Analytics custom dimension using the Measurement Protocol API.
    Google Analytics only provides 20 custom dimension slots so you will need to use them wisely.

    :param cid: Client ID
    :param index: The custom dimension index you wish to populate (only 20 are available).
    :param value: The value you wish to assign to the custom dimension
    :return: HTTP response status
    """

    payload = {
        'cid': cid,
        't': 'event',
        'ec': 'Measurement Protocol requests',
        'ea': 'cd{0}'.format(index) + '=' + value,
        'ni': 1,
        'cd{0}'.format(index): value,
    }
    send(payload)


def custom_metric(cid, index: str, value: str):
    """Populate a Google Analytics custom metric using the Measurement Protocol API.
    Google Analytics only provides 20 custom metric slots so you will need to use them wisely.

    :param cid: Client ID
    :param index: The custom metric index you wish to populate (only 20 are available).
    :param value: The value you wish to assign to the custom metric
    :return: HTTP response status
    """

    payload = {
        'cid': cid,
        't': 'event',
        'ec': 'Measurement Protocol requests',
        'ea': 'cm{0}'.format(index) + '=' + value,
        'ni': 1,
        'cm{0}'.format(index): value,
    }
    send(payload)
