import unittest
import numpy as np
from handwriting_synthesis.hand import Hand
from handwriting_synthesis.rnn import rnn
from handwriting_synthesis.data_frame import DataFrame
import os
import tensorflow as tf

class TestHandwritingSynthesis(unittest.TestCase):

    def setUp(self):
        # Setup any state specific to the test cases.
        self.data_dir = 'data/processed/'
        self.hand = Hand()
        self.rnn_model = rnn(
            lstm_size=400,
            output_mixture_components=20,
            attention_mixture_components=10,
            log_dir='logs',
            checkpoint_dir='checkpoints',
            prediction_dir='predictions',
            learning_rates=[.0001, .00005, .00002],
            batch_sizes=[32, 64, 64],
            patiences=[1500, 1000, 500],
            beta1_decays=[.9, .9, .9],
            validation_batch_size=32,
            optimizer='rms',
            num_training_steps=100000,
            warm_start_init_step=0,
            regularization_constant=0.0,
            keep_prob=1.0,
            enable_parameter_averaging=False,
            min_steps_to_checkpoint=2000,
            log_interval=20,
            logging_level=logging.CRITICAL,
            grad_clip=10
        )

    def test_data_processing(self):
        # Test if data is processed correctly
        data_cols = ['x', 'x_len', 'c', 'c_len']
        data = [np.load(os.path.join(self.data_dir, '{}.npy'.format(i))) for i in data_cols]
        df = DataFrame(columns=data_cols, data=data)
        self.assertEqual(len(df.columns), 4)
        self.assertEqual(df.length, len(data[0]))

    def test_model_training(self):
        # Test if the model can be initialized and trained
        try:
            self.rnn_model.fit()
            trained = True
        except tf.errors.OpError as e:
            print(f"Training failed with TensorFlow exception: {e}")
            trained = False
        except Exception as e:
            print(f"Training failed with exception: {e}")
            trained = False
        self.assertTrue(trained)

    def test_handwriting_generation(self):
        # Test if handwriting generation works
        lines = ["Hello world", "This is a test"]
        try:
            self.hand.write(filename='test_output.svg', lines=lines)
            generated = True
        except tf.errors.OpError as e:
            print(f"Handwriting generation failed with TensorFlow exception: {e}")
            generated = False
        except Exception as e:
            print(f"Handwriting generation failed with exception: {e}")
            generated = False
        self.assertTrue(generated)

if __name__ == '__main__':
    unittest.main()