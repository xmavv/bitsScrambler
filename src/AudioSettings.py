class AudioSettings:
    def __init__(self, numberOfChannels, sampWidth, framerate, numberOfFrames, compressionType, compressionName):
        self.numberOfChannels = numberOfChannels
        self.sampWidth = sampWidth
        self.framerate = framerate
        self.numberOfFrames = numberOfFrames
        self.compressionType = compressionType
        self.compressionName = compressionName