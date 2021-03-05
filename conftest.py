from projeto import settings


@pytest.fixture(autouse=True)
def turn_ssl_rediret_off_for_tests(settings):
    """
    There is no need to place secure=True in all client requests
    """
    settings.SECURE_SSL_REDIRECT = False
