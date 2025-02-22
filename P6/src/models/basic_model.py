from models.model import Model
from tensorflow.keras import Sequential, layers
from tensorflow.keras.layers.experimental.preprocessing import Rescaling
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization, GlobalAveragePooling2D
from tensorflow.keras.optimizers import RMSprop, Adam

class BasicModel(Model):
    def _define_model(self, input_shape, categories_count):
        # Your code goes here
        # you have to initialize self.model to a keras model
        model = Sequential([

            Conv2D(8, (3, 3), activation='relu', input_shape=input_shape),
            MaxPooling2D((2, 2)),

            Conv2D(16, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),

            Conv2D(32, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),


            # Flatten layer to transition to dense layers
            Flatten(),
            
            # Dense layers
            Dense(32, activation='relu'),
            Dense(categories_count, activation='softmax')
        ])

        self.model = model
    
    def _compile_model(self):
        # Your code goes here
        # you have to compile the keras model, similar to the example in the writeup
        # example:
        self.model.compile(
            optimizer=RMSprop(learning_rate=0.001),
            loss='categorical_crossentropy',
            metrics=['accuracy'],
        )