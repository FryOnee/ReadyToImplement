import h5py
import numpy as np
from PIL import Image

def process_floor_data(floor_data):
    """Funkcja przetwarzająca dane podłogi."""
    # Konwertuj dane do numpy.ndarray, jeśli nie są już w tym formacie
    if not isinstance(floor_data, np.ndarray):
        floor_data = np.array(floor_data)

    # Jeśli dane są jednowymiarowe, przekształć je na dwuwymiarowe
    if floor_data.ndim == 1:
        floor_data = floor_data.reshape((1, -1))

    # Rozmiary pliku
    image_height, image_width = floor_data.shape

    # creating clear png
    image = Image.new('1', (image_width, image_height))

    # putting colors on that clear png
    for y, floor_row in enumerate(floor_data):
        for x, value in enumerate(floor_row):
            pixel_color = 0 if value == 0 else 1
            image.putpixel((x, y), pixel_color)

    # Tutaj możesz dodać dodatkowe operacje na obrazie lub zwrócić go, jeśli to konieczne
    return image

def process_wall_data(floor_data):
#"""Funkcja przetwarzająca dane podłogi."""
# Konwertuj dane do numpy.ndarray, jeśli nie są już w tym formacie
    if not isinstance(floor_data, np.ndarray):
        floor_data = np.array(floor_data)
    # Jeśli dane są jednowymiarowe, przekształć je na dwuwymiarowe
    if floor_data.ndim == 1:
        floor_data = floor_data.reshape((1, -1))
    # Rozmiary pliku
    image_height, image_width = floor_data.shape
    # creating clear png
    image = Image.new('RGBA', (image_width, image_height))
    # putting colors on that clear png
    for y, floor_row in enumerate(floor_data):
        for x, value in enumerate(floor_row):
            pixel_color = (0, 0, 0, 0) if value == 0 else (255, 0, 0, 255)
            image.putpixel((x, y), pixel_color)
    # Tutaj możesz dodać dodatkowe operacje na obrazie lub zwrócić go, jeśli to konieczne
    return image

names=['floor_bw','helping_lines_bw_high','helping_lines_bw_mid','helping_lines_bw_low']



mat_file_path = 'example\\multiple_helping_lines_exmpl.mat'
with h5py.File(mat_file_path, 'r') as mat_file:
    # Iteruj przez wszystkie grupy w pliku .mat
    for idx2,group_key in enumerate(mat_file.keys()):
        #if idx2>0:
        #print(idx2)
        current_group = mat_file[group_key]
        
        #Sprawdź, czy to jest grupa
        if isinstance(current_group, h5py.Group):
            number=len(mat_file["floor_bw"])
            #print(number)
            # Dla każdego zbioru danych wewnątrz grupy
            counter=0
            counter2=0
            for idx, data_key in enumerate(current_group.keys()):
                if idx > 0:  # Wyświetl dane tylko dla indeksów większych niż 0
                    data = current_group[data_key][()]  # Wczytaj dane z grupy
                    #print(len(current_group))
                    #print(data_key)
                    if(counter2==number):
                        counter2=0

                    if(counter//number>0):
                        obraz=process_wall_data(data)
                    else:
                        obraz=process_floor_data(data)


                    #print(counter)
                    print(counter//number)
                    
                    obraz.save(f"{names[counter//number]}\\floor_{counter2}.png")
                    counter+=1
                    counter2+=1
                    

