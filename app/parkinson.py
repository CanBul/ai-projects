from app import app
import numpy as np
import librosa  
from tensorflow.keras.layers import Dense, Dropout, Flatten, Convolution2D, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from tensorflow import keras 
    
def scale_minmax(X, min=0.0, max=1.0):
    X_std = (X - X.min()) / (X.max() - X.min())
    X_scaled = X_std * (max - min) + min
    return X_scaled

def bw_spectrogram_image(wav_path):

    temp_sample, sampleRate = librosa.load(wav_path) 
    
    temp_sample.astype(np.float32)   
    sample = np.zeros((3*sampleRate), dtype=np.float32)
    

    if len(temp_sample) <= 3*sampleRate:
        sample[0:len(temp_sample)] = temp_sample 
    else:
        sample = temp_sample[:3*sampleRate]
      
    
    # use log-melspectrogram
    mels = librosa.feature.melspectrogram(sample, sr=22050, n_mels=128)
    mels = np.log(mels + 1e-9)  # add small number to avoid log(0)

    # min-max scale to fit inside 8-bit range
    img = scale_minmax(mels, 0, 255).astype(np.uint8)
    img = np.flip(img, axis=0)  # put low frequencies at the bottom in image
    img = 255 - img  # invert. make black==more energy
    img = img.astype('float32')
    img /= 255
    img = img.reshape(-1, 128, 130, 1) 
    

    return img
    
def create_and_predict():

    model = Sequential()

    model.add(Convolution2D(filters = 32, kernel_size = (5,5),padding = 'Same',
                    activation ='relu', input_shape = (128,130,1)))
    model.add(Convolution2D(filters = 32, kernel_size = (5,5),padding = 'Same',
                    activation ='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))


    model.add(Convolution2D(filters = 64, kernel_size = (3,3),padding = 'Same',
                    activation ='relu'))
    model.add(Convolution2D(filters = 64, kernel_size = (3,3),padding = 'Same',
                    activation ='relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    model.add(Dropout(0.25))


    model.add(Flatten())
    model.add(Dense(256, activation = "relu"))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation = "sigmoid"))

    optimizer = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
    model.compile(optimizer = optimizer , loss='binary_crossentropy', metrics=['accuracy'])
    model.load_weights('/home/can/ai-projects/app/modelWeights.hdf5')

    

    return model


# print(create_and_predict(bw_spectrogram_image('./fromServer.wav')))