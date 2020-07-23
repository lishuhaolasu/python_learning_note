import keras
from keras import regularizers
import keras.backend as K
from keras.layers import Input, Activation, BatchNormalization, Flatten, Conv2D
from keras.applications.resnet50 import conv_block, indentity_block
from keras.layers import Convolution2D, ZeroPadding2D
from keras.layers import MaxPooling2D, Dense, GlobalAveragePooling2D, PReLU, LSTM


def keras_model(image_size_x, image_size_y, image_channel, action_space):
    input_shape = (image_size_x, image_size_y, image_channel)
    img_input = Input(shape=input_shape)
    bn_axis = 3
    x = ZeroPadding2D((3, 3))(img_input)
    x = Convolution2D(8,7,7,subsample=(2,2),name='conv1')(x)
    x = BatchNormalization(axis=bn_axis,name='bn_conv1')(x)
    x = Activation('relu')(x)
    x = MaxPooling2D((3,3),strides=(2,2))(x)
    x = conv_block(x,3,[8,8,16],stage=2,block='a',strides=(1,1))
    x = indentity_block(x,3,[8,8,16],stage=2,block='b')
    x = indentity_block(x,3,[8,8,16],stage=2,block='c')
    x = conv_block(x,3,[16,16,32],stage=3,block='a')
    x = indentity_block(x,3,[16,16,32],stage=3,block='b')
    x = indentity_block(x,3,[16,16,32],stage=3,block='c')
    x = indentity_block(x,3,[16,16,32],stage=3,block='d')
    x = conv_block(x,3,[32,32,64],stage=4,block='a')
    x = indentity_block(x,3,[32,32,64],stage=4,block='b')
    x = indentity_block(x,3,[32,32,64],stage=4,block='c')
    x = indentity_block(x,3,[32,32,64],stage=4,block='d')
    x = indentity_block(x,3,[32,32,64],stage=4,block='e')
    x = indentity_block(x,3,[32,32,64],stage=4,block='f')
    x = conv_block(x,3,[64,64,128],stage=5,block='a')
    x = indentity_block(x,3,[64,64,128],stage=5,block='b')
    x = indentity_block(x,3,[64,64,128],stage=5,block='c')
    x = conv_block(x,3,[64,64,256],stage=6,block='a')
    x = indentity_block(x,3,[64,64,256],stage=6,block='b')
    x = indentity_block(x,3,[64,64,256],stage=6,block='c')
    x = GlobalAveragePooling2D()(x)
    x = Dense(200,name='fc_feature')(x)
    x = PReLU()(x)
    x = Dense(action_space,activation='softmax',name='fc_action')(x)
    model = model(img_input,x)
    return model
