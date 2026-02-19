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
        self.schedule = [
            {"name": "truffle", "duration": 2, "category": 1, "priority": 3},
            {"name": "Chilling", "duration": 20, "category": 1, "priority": 3},
            {"name": "Nothing", "duration": True, "category": -1, "priority": 99},
            {"name": "Nothing", "duration": True, "category": 0, "priority": 99},
            {"name": "Nothing", "duration": True, "category": 1, "priority": 99},
            {"name": "Nothing", "duration": True, "category": 2, "priority": 99},
            {"name": "Nothing", "duration": True, "category": 3, "priority": 99},
            {"name": "Nothing", "duration": True, "category": 4, "priority": 99},
            {"name": "cheese", "duration": 8, "category": 1, "priority": 2}

        ]
        #example: {"name": "travel", "duration": 5 (this is the time in hours),"category": 1 (this should be the number in the time scheduler array) "priority": 1,(one has the highest priority) "fcall":"travel" (will be called once its finished)}
        self.time_plan = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.current_activity = {"category":1} #please work

    def get_time_plan(self,time_plan):
        self.time_plan = time_plan

    def sorting(self,e):
        if e is None:
            return 99
        return e["priority"]

    def scheduler(self,tp,newtask=None):
        hour = self.hour
        if tp is None: #this is for when new task will be added
            print("hello??")
            if newtask == None:
                return
            self.schedule.append(newtask)
            self.schedule.sort(key=self.sorting)
            print(f" new {self.schedule}")
            return
        for _ in range(tp):
            print(f"Current Activity: {self.current_activity}")
            if self.current_activity == None:
                for s in self.schedule:
                    if s["category"] == self.time_plan[hour]:
                        self.current_activity = s
                        print(f"Current Activity: {self.current_activity}")
                        break

            if self.time_plan[hour] == self.current_activity["category"]:
                print("Schedule works 1")
                if self.current_activity["duration"] is True:
                    pass
                else:
                    self.current_activity["duration"] -= 1
                hour = (hour + 1) % 24
                if self.current_activity["duration"] == 0:
                    self.current_activity = None
                    for s in self.schedule:
                        if s["category"] == self.time_plan[hour]:
                            self.current_activity = s
                            print(f"Current Activity: {self.current_activity}")
                            break
            else:
                self.current_activity = None
                for s in self.schedule:
                    if s["category"] == self.time_plan[hour]:
                        self.current_activity = s
                        print(f"Current Activity: {self.current_activity}")
                        break








    def newtime(self): #this code is not used for anything at the moment
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
        print(self.schedule)
        new_seconds = seconds
        while new_seconds > 0:
            new_seconds -= 1
            self.second += 1
            if self.second == 61:
                self.minute += 1
                self.second = 1
                if self.minute == 61:
                    self.scheduler(1)
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
            self.scheduler(24)
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
