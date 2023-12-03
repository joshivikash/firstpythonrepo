class Time:

    def __init__(self, time):
        self.time = time
        self.mins = self.time // 60
        self.__remaining_secs = self.time - (self.mins * 60)
        self.hours = self.mins // 60
        self.__remaining_mins = self.mins - (self.hours * 60)
        self.days = self.hours // 24
        self.__remaining_hours = self.hours - (self.days * 24)

    def seconds_to_minutes(self):
        return '{} min {} sec'.format(self.mins, self.__remaining_secs)
    
    def seconds_to_hours(self):
        return '{} hrs {} min {} sec'.format(self.hours,self.__remaining_mins, self.__remaining_secs)
    
    def seconds_to_days(self):
        return '{} days {} hrs {} min {} sec'.format(self.days,self.__remaining_hours,self.__remaining_mins, self.__remaining_secs)

    
t = Time(10000)
print('seconds to minutes {}'.format(t.seconds_to_minutes()))
print('seconds to hours {}'.format(t.seconds_to_hours()))
print('seconds to days {}'.format(t.seconds_to_days()))