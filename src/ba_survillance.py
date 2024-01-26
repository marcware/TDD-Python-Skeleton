from abc import ABC, abstractmethod


class MotionSensor(ABC):
    @abstractmethod
    def is_detecting_motion(self) -> bool:
        pass


class VideoRecorder(ABC):
    @abstractmethod
    def start_recording(self) -> None:
        pass

    @abstractmethod
    def stop_recording(self) -> None:
        pass


class SurveillanceController:
    def __init__(self, sensor, recorder):
        self.sensor = sensor
        self.recorder = recorder

    def record_motion(self):
        if self.sensor.is_detecting_motion():
            self.recorder.start_recording()
        else:
            self.recorder.stop_recording()


