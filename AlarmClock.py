class AlarmClock:
    # importing necessary modules :
    from datetime import datetime
    from playsound import playsound
    import re


    def recieve_alarm(self):
        """
        :return: starts alarm if format is True, otherwise False
        """
        # require input from user
        alarm_time = input("please enter alarm time by this format HH:MM:SS AM/PM\n\t")
        
        # check if the format of the input is right.
        if self.re.compile('.{2}:.{2}:.{2} .{2}').match(alarm_time):
                self.start_alarm(alarm_time)
        else:
            print("false format, try again")


    def start_alarm(self, alarm_time: str):
        """
        :param alarm_time: the required alarm time
        :return: alert when alarm time is positive
        """
        # spliting input time into parts.
        hour, minutes, seconds, period = alarm_time[:2], alarm_time[3:5], alarm_time[6:8], alarm_time[9:11].upper()

        # alert the user that alarm is starting
        print("setting up alarm ....")
        while True:
            current_time = self.datetime.now()
            curr_hour, curr_min, curr_sec, curr_perr = \
                current_time.strftime('%I'), current_time.strftime('%M'), current_time.strftime('%S'), current_time.strftime('%p')

            if curr_perr == period:
                if curr_hour == hour:
                    if curr_min == minutes:
                        if curr_sec == seconds:
                            # required time is reached, alarm activated.
                            print("alarm activated!")
                            self.playsound('mixkit-facility-alarm-sound-999.wav')
                            break
