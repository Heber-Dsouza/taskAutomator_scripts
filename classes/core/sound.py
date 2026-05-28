from enum import Enum
from playsound3 import playsound

class LaunchOperationTypes(Enum):
    QUICK = "QUICK"
    SUCCESS = "SUCCESS"

class Sound:
    @staticmethod
    def play_alert(alert_type:LaunchOperationTypes=LaunchOperationTypes.QUICK):
        match alert_type:
            case LaunchOperationTypes.SUCCESS:
                playsound('../../assets/sounds/success-alert.wav')
                return

        playsound('../../assets/sounds/quick_tone.wav')
