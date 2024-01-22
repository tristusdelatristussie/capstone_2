from kih.preprocessors import ResnetPreprocessor
from kih.preprocessors import XceptionPreprocessor
from kih.preprocessors import VGGPreprocessor
from kih.preprocessors import InceptionPreprocessor
from kih.preprocessors import EfficientNet


# reference: https://keras.io/api/applications/

preprocessors = {
    'xception': XceptionPreprocessor,
    'resnet50': ResnetPreprocessor,
    'vgg16': VGGPreprocessor,
    'inception_v3': InceptionPreprocessor,
    'efficientnet_v2' : EfficientNet 
}


def create_preprocessor(name, target_size, **params):
    name = name.lower()
    if name not in preprocessors:
        raise Exception('Unknown model %s' % name)
    Preprocessor = preprocessors[name]
    return Preprocessor(target_size=target_size, **params)