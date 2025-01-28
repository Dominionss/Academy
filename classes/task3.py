class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.channel_number = 0

    def first_channel(self):
        self.channel_number = 0
        return self.channels[self.channel_number]

    def last_channel(self):
        self.channel_number = len(self.channels) - 1
        return self.channels[self.channel_number]

    def turn_channel(self, channel_number):
        if channel_number >= 1 and channel_number < len(self.channels):
            self.channel_number = channel_number - 1
            return self.channels[self.channel_number]
        else:
            raise ValueError("Channel number out of range.")

    def next_channel(self):
        self.channel_number = (self.channel_number + 1) % len(self.channels)
        return self.channels[self.channel_number]

    def previous_channel(self):
        self.channel_number = (self.channel_number - 1) % len(self.channels)
        return self.channels[self.channel_number]

    def current_channel(self):
        return self.channels[self.channel_number]

    def exists(self, query):
        if isinstance(query, int):
            if query >= 1 and query <= len(self.channels):
                return "Yes"
            else:
                return "No"
        elif isinstance(query, str):
            if query in self.channels:
                return "Yes"
            else:
                return "No"
        else:
            return "No"


# Tests

CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)


print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.exists(4))
print(controller.exists("BBC"))
