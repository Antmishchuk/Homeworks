def pallindrome(str_):
    if len(str_) < 1:
        return True
    else:
        if str_[0].lower() == str_[-1].lower():
            return pallindrome(str_[1:-1])
        else:
            return False
print(pallindrome('АрозаупаланалапуАзора'))

