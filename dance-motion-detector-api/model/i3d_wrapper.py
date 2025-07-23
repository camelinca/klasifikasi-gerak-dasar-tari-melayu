import tensorflow as tf
import tensorflow_hub as hub

NUM_FRAMES = 30         # Pastikan sama dengan yang kamu pakai
FRAME_SIZE = 224        # Sama seperti input size
I3D_MODEL_URL = "https://tfhub.dev/deepmind/i3d-kinetics-400/1"

class I3DWrapper(tf.keras.layers.Layer):
    def __init__(self, hub_url=I3D_MODEL_URL, **kwargs):
        super(I3DWrapper, self).__init__(**kwargs)
        self.hub_url = hub_url
        self.i3d = None

    def build(self, input_shape):
        self.i3d = hub.load(self.hub_url).signatures['default']
        dummy_input = tf.zeros((1, NUM_FRAMES, FRAME_SIZE, FRAME_SIZE, 3))
        _ = self.i3d(dummy_input)

    def call(self, inputs):
        inputs = tf.cast(inputs, tf.float32)
        outputs = self.i3d(inputs)
        return outputs['default']

    def compute_output_shape(self, input_shape):
        return (input_shape[0], 400)
