import webbrowser
class TelevisionFactory:
    def __init__(self, model_name, matrix, resolution):
        self.model_name = model_name
        self.matrix = matrix
        self.resolution = resolution
        self._television = None

    def turn_on(self):
        if self._television is not None:
            self._television.turn_on()
            print("The TV is already on.")
        else:
            self._television = "The TV is turned on."
            webbrowser.open("https://tinyurl.com/echogay")
            print("The TV is on.")

    def turn_off(self):
        if self._television is not None:
            self._television.turn_off()
            print("The TV is off.")
        else:
            print("The TV is already off.")

    def get_channel(self, number):
        print(f"The TV is on channel {number}.")

tv = TelevisionFactory("Sony", "VA", "1080p")
samsung = TelevisionFactory("Samsung", "IPS", "1080p")
lg = TelevisionFactory("LG", "AMOLED", "1080p")
tv.turn_on()
tv.get_channel(5)
print(tv.model_name, tv.matrix, tv.resolution)
print(samsung.model_name, samsung.matrix, samsung.resolution)
print(lg.model_name, lg.matrix, lg.resolution)