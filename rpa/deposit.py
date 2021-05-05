from infra.sokupad_client import SokupadClient


def deposit(data):
    client = SokupadClient()
    client.login(data['id'], data['password'], data['p_ars'])
    client.quit()