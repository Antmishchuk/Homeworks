import time
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __str__(self):
        return self.title


class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return self.username
    def __eq__(self, other):
        return self.username == other.username



class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_out(self):
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.username == nickname and user.password == hash(password):
                self.current_user = user
                break
        else:
            print('Введен неправильный логин или пароль')

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(new_user)
            self.current_user = new_user

    def add(self, *vid):
        for video in vid:
            if video.title not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        title_list = []
        for video in self.videos:
            if search_word.upper() in video.title.upper():
                title_list.append(video.title)
        return title_list

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if title == video.title:
                if self.current_user.age >= 18 or not video.adult_mode:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=' ')
                        time.sleep(0.1)
                    video.time_now = 0
                    print('Конец видео')

                else:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                break


if __name__ == '__main__':
    ur = UrTube()

    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    ur.add(v1, v2)
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    ur.watch_video('Лучший язык программирования 2024 года!')