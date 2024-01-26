from abc import ABC

from doublex import Spy
from doublex_expects import have_been_called
from mamba import description, it
from expects import expect, equal

from src.ba_survillance import SurveillanceController, MotionSensor, VideoRecorder

USER = "A_USER"


class FakeMotion(MotionSensor, ABC):
    def is_detecting_motion(self) -> bool:
        return False


class FakeRecorder(VideoRecorder, ABC):
    def start_recording(self) -> None:
        print("Start recording...")

    def stop_recording(self) -> None:
        print("Strop recording...")


class StubSensorDetectingMotion(MotionSensor):
    def is_detecting_motion(self) -> bool:
        return True


class StubSensorNoDetectingMotion(MotionSensor):
    def is_detecting_motion(self) -> bool:
        return False


class SpyVideoRecorder(VideoRecorder):
    def __init__(self):
        self.start_called = False
        self.stop_called = False

    def start_recording(self) -> None:
        self.start_called = True

    def stop_recording(self) -> None:
        self.stop_called = True


with description('The Surveillance Controller'):
    with description('No Mock'):
        with it('asks the recorder to stop recording when the sensor detects no motion'):
            sensor = StubSensorNoDetectingMotion()
            recorder = SpyVideoRecorder()
            controller = SurveillanceController(sensor, recorder)

            controller.record_motion()

            expect(recorder.stop_called).to(equal(True))
        with it('asks the recorder to start recording when the sensor detects motion'):
            sensor = StubSensorDetectingMotion()
            recorder = SpyVideoRecorder()
            controller = SurveillanceController(sensor, recorder)

            controller.record_motion()

            expect(recorder.start_called).to(equal(True))
    with description('Mock'):
        with it('asks the recorder to stop recording when the sensor detects no motion'):
            sensor = StubSensorNoDetectingMotion()  # Crear un spy para el sensor
            spy_recorder = Spy(SpyVideoRecorder)

            controller = SurveillanceController(sensor, spy_recorder)
            controller.record_motion()

            expect(spy_recorder.stop_recording).to(have_been_called)

        with it('asks the recorder to start recording when the sensor detects motion'):
            sensor = StubSensorDetectingMotion()
            spy_recorder = Spy(SpyVideoRecorder)

            controller = SurveillanceController(sensor, spy_recorder)
            controller.record_motion()

            expect(spy_recorder.start_recording).to(have_been_called)
