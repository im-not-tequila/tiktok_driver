# python3.11.8
from packages import TiktokAuthorization
# from packages import YoutubeActions


def test():
    pass


def main():
    profiles_directory = r'C:\work\activity_project\profiles'
    profile_directory = r''
    link_to_video = 'https://www.youtube.com/watch?v=L6kWCS6TKGs&ab_channel=IT-%D1%81%D0%BF%D0%B5%D1%86.%D0%94%D0%B5%D0%BD%D0%B8%D1%81%D0%9A%D1%83%D1%80%D0%B5%D1%86'
    comment = 'ну я бы этот топ вопросов еще расширил бы)'

    yt_auth = TiktokAuthorization(login='REDACTED_TIKTOK_LOGIN',
                                  password='REDACTED_TIKTOK_PASSWORD',
                                  profiles_directory=profiles_directory)

    yt_auth.email_auth()


if __name__ == '__main__':
    main()
