class NoAudioUploadedServiceError(Exception):
    pass


class AudioTooLargeServiceError(Exception):
    pass


class UnsupportedAudioTypeServiceError(Exception):
    pass


class ProviderNotSupportSpeechToTextServiceError(Exception):
    pass


class ProviderNotSupportTextToSpeechServiceError(Exception):
    pass


class ProviderNotSupportTextToSpeechLanguageServiceError(Exception):
    pass
