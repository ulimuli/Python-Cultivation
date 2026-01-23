class Timming:
    def __init__(self, dct, bls, cue, second, minute, hour, day, month, year):
        self.dct = dct
        self.bls = bls
        self.cue = cue
        self.second = second
        self.minute = minute
        self.hour = hour
        self.day = day
        self.month = month
        self.year = year

    def newtime(self):
        year = 100
        month = 1
        day = 1
        days = 1312
        while days > 0:
            if days >= 360:
                year += 1
                days -= 360
                if days <= 30:
                    month += 1

    def dtime(self, seconds,):  # for the 24-hour cycles
        new_seconds = seconds
        while new_seconds > 0:
            new_seconds -= 1
            self.second += 1
            if self.second == 61:
                self.minute += 1
                self.second = 1
                if self.minute == 61:
                    self.hour += 1
                    self.minute = 1
                    if self.hour == 24:
                        Timming.time(self, 1)
                        self.hour = 0
        return self.second, self.minute, self.hour, self.day, self.month, self.year

    def time(self, days=None):

        new_days = days
        nhf = Timming.cultivate(self, days)
        while new_days > 0:
            new_days -= 1
            self.day += 1
            if self.day == 31:
                self.month += 1
                self.day = 1
                if self.month == 13:
                    self.month = 1
                    self.year += 1

        return self.day, self.month, self.year, self.cue, nhf

    def cultivate(self, days):
        try:
            nhf = False  #no hours first selected
            dc = self.bls * self.dct * days / 100
            self.cue += dc
        except:
            pass
        if self.dct == 0:
            nhf = True

        return nhf
