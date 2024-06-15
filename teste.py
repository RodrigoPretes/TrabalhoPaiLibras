import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing import image
import os

# Configurações iniciais
IMG_WIDTH, IMG_HEIGHT = 64, 64
BATCH_SIZE = 32
EPOCHS = 20

# Função para carregar dados e dividir em treinamento e teste
def load_data():
    data = []
    labels = []
    for label in os.listdir('dataset'):
        if os.path.isdir(f'dataset/{label}'):
            for img_name in range(60):  # Supondo que as imagens são numeradas de 0 a 59
                img_path = f'dataset/{label}/{img_name}.png'
                if os.path.exists(img_path):
                    img = image.load_img(img_path, target_size=(IMG_WIDTH, IMG_HEIGHT))
                    img = image.img_to_array(img)
                    img = img / 255.0
                    data.append(img)
                    labels.append(label)
    data = np.array(data)
    labels = np.array(labels)
    
    # Codificar labels como inteiros
    le = LabelEncoder()
    labels = le.fit_transform(labels)
    
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test, le

# Função para aumento de dados
def augment_data():
    datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    for label in os.listdir('dataset'):
        if os.path.isdir(f'dataset/{label}'):
            for img_name in range(60):  # Supondo que as imagens são numeradas de 0 a 59
                img_path = f'dataset/{label}/{img_name}.png'
                if os.path.exists(img_path):
                    img = image.load_img(img_path, target_size=(IMG_WIDTH, IMG_HEIGHT))
                    x = image.img_to_array(img)
                    x = np.expand_dims(x, axis=0)
                    i = 0
                    for batch in datagen.flow(x, batch_size=1, save_to_dir=f'dataset/{label}', save_prefix='aug', save_format='png'):
                        i += 1
                        if i > 20:
                            break

# Construção do modelo de rede neural
def build_model():
    model = Sequential([
        Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(len(os.listdir('dataset')), activation='softmax')
    ])
    model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Treinamento do modelo
def train_model(model, X_train, y_train, X_test, y_test):
    history = model.fit(X_train, y_train, epochs=EPOCHS, validation_data=(X_test, y_test), batch_size=BATCH_SIZE)
    return history

# Função para avaliação em tempo real
def recognize_sign(model, label_encoder):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        img = cv2.resize(frame, (IMG_WIDTH, IMG_HEIGHT))
        img = np.expand_dims(img, axis=0) / 255.0
        prediction = model.predict(img)
        label = np.argmax(prediction)
        letter = label_encoder.inverse_transform([label])[0]
        cv2.putText(frame, f'Letter: {letter}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Real-time Sign Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Aumento de dados
augment_data()

# Carregar dados
X_train, X_test, y_train, y_test, label_encoder = load_data()

# Construir e treinar o modelo
model = build_model()
history = train_model(model, X_train, y_train, X_test, y_test)

# Reconhecimento em tempo real
recognize_sign(model, label_encoder)
