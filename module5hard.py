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
            else:
                print('Введен неправильный логин или пароль')

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(new_user)
            self.current_user = new_user




if __name__ == '__main__':
    user1 = User('Anton', '12345qwe', 53)
    print(user1, user1.password)
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
