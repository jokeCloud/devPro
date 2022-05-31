import requests


def search_avatar(user):
    """
    Busca o avatar de um usuários no github

    :param user: str com nome do usuário no github
    :return: str com link do avatar
    """

    url = f'https://api.github.com/users/{user}'
    response = requests.get(url)
    avatar = response.json()['avatar_url']
    return avatar


if __name__ == '__main__':
    print(search_avatar('jokeCloud'))
