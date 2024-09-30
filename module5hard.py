class Video:
    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode



class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age

    def __hash__(self):
        return hash((self.password))

class UrTube:
    def __init__(self, users, videos,current_user):



if __name__ == '__main__':
    user1 = User('Anton', '8c34eacd', 53)
    print(hash(user1))
    v1 = Video('Лучший язык программирования 2024 года', 200, 0, False)
    v2 = Video('Для чего девушкам парень программист?', 10, 0,adult_mode=True)

