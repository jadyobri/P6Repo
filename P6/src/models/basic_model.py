from models.model import Model
from tensorflow.keras import Sequential, layers
from tensorflow.keras.layers.experimental.preprocessing import Rescaling
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import RMSprop, Adam

class BasicModel(Model):
    def _define_model(self, input_shape, categories_count):
        # Your code goes here
        # you have to initialize self.model to a keras model
        model = Sequential()

        model.add(Conv2D(8, (3, 3), activation='relu', input_shape=(150, 150, 3)))
        model.add(MaxPooling2D((2, 2)))
        model.summary()

        model.add(Conv2D(16, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2)))
        model.summary()

        model.add(Conv2D(16, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2)))
        model.summary()

        model.add(Flatten())
        model.add(Dense(16, activation='relu'))
        model.add(Dense(16, activation='relu'))
        model.summary()
        
        # 3 classes with softmax
        model.add(Dense(3, activation='softmax'))

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