import numpy as np
import sympy as sp
from PIL import Image

def determinant(matrix):
    if matrix.shape == (2,2) or matrix.shape == (3,3):
        return int(np.linalg.det(matrix))
    else:
        raise ValueError("Matriks harus berordo 2x2 atau 3x3")

def adjoint(matrix):
    if matrix.shape == (2,2) or matrix.shape == (3,3):
        return np.array(sp.Matrix(matrix).adjugate())
    else:
        raise ValueError("Matriks harus berordo 2x2 atau 3x3")

def m_score(matrix):
    det = determinant(matrix)
    for i in range(1, 256):
        if det * i % 256 == 1:
            return i

def inverse(matrix):
    inv = (m_score(matrix) * adjoint(matrix)) % 256
    return np.array(inv)

def encrypt_channel(channel, kunci_matrix):
    # Mengubah array channel menjadi matrix
    channel_matrix = np.matrix(channel)

    # Inisialisasi baris dan kolom channel gambar ke variabel
    baris_channel, kolom_channel = channel_matrix.shape

    # Inisialisasi baris dan kolom kunci ke variabel
    kunci_rows, kunci_cols = kunci_matrix.shape

    # Mengubah dimensi channel matrix menjadi blok dengan panjang yang sama dengan kunci matrix
    blok_matrix_channel = []
    for i in range(0, baris_channel, kunci_rows):
        for j in range(0, kolom_channel, kunci_cols):
            blok_matrix_channel.append(channel_matrix[i:i+kunci_rows, j:j+kunci_cols])

    # Mengenkripsi setiap blok menggunakan algoritma Hill Cipher
    blok_matrix_enkripsi = []
    for blok in blok_matrix_channel:
        blok_enkripsi = (kunci_matrix * blok) % 256
        blok_matrix_enkripsi.append(blok_enkripsi)

    # Combine all the encrypted matrix blok into a single matrix
    matrix_enkripsi = np.block([[blok_matrix_enkripsi[j*kolom_channel//kunci_cols + i] for i in range(kolom_channel//kunci_cols)] for j in range(baris_channel//kunci_rows)])

    # Convert the encrypted matrix back into an array
    channel_enkripsi = np.array(matrix_enkripsi, dtype=np.uint8)

    return channel_enkripsi

def hill_cipher_encrypt(img_path, key_matrix):
    # Mengubah ordo matriks kunci
    if len(list(key_matrix)) == 4:
        key_matrix = np.array(key_matrix).reshape(2,2)
    elif len(list(key_matrix)) == 9:
        key_matrix = np.array(key_matrix).reshape(3,3)
    
    # Load gambar
    img = Image.open(img_path).convert('RGB')
    img_arr = np.array(img)
    
    for i in range(3):
        # Membagi channel gambar -> R,G,B
        r_channel = img_arr[:, :, 0]
        g_channel = img_arr[:, :, 1]
        b_channel = img_arr[:, :, 2]

        # Mengenkripsi setiap channel
        encrypted_red_channel = encrypt_channel(r_channel, key_matrix)
        encrypted_green_channel = encrypt_channel(g_channel, key_matrix)
        encrypted_blue_channel = encrypt_channel(b_channel, key_matrix)

        # Menggabungkan enkripsi channel gambar menjadi 1 array
        encrypted_img_arr = np.stack((encrypted_red_channel, encrypted_green_channel, encrypted_blue_channel), axis=2)
        img_arr = encrypted_img_arr

        # Mengubah array gambar menjadi gambar
        encrypted_img = Image.fromarray(encrypted_img_arr)
        encrypted_img.save('static/image/encrypted_image.png')
        encrypt = 'image/encrypted_image.png'

    return encrypt

def hill_cipher_decrypt(img_path, key_matrix):
    # Mengubah ordo matriks kunci
    if len(list(key_matrix)) == 4:
        key_matrix = np.array(key_matrix).reshape(2,2)
    elif len(list(key_matrix)) == 9:
        key_matrix = np.array(key_matrix).reshape(3,3)
        
    key_matrix = inverse(key_matrix)

    # Load gambar
    img = Image.open(img_path).convert('RGB')
    img_arr = np.array(img)
    
    for i in range(3):
        # Membagi channel gambar -> R,G,B
        r_channel = img_arr[:, :, 0]
        g_channel = img_arr[:, :, 1]
        b_channel = img_arr[:, :, 2]

        # Mendekripsi setiap channel
        decrypted_red_channel = encrypt_channel(r_channel, key_matrix)
        decrypted_green_channel = encrypt_channel(g_channel, key_matrix)
        decrypted_blue_channel = encrypt_channel(b_channel, key_matrix)

        # Menggabungkan enkripsi channel gambar menjadi 1 array
        decrypted_img_arr = np.stack((decrypted_red_channel, decrypted_green_channel, decrypted_blue_channel), axis=2)
        img_arr = decrypted_img_arr

        # Mengubah array gambar menjadi gambar
        decrypted_img = Image.fromarray(decrypted_img_arr)
        decrypted_img.save('static/image/decrypted_image.png')
        decrypt = 'image/decrypted_image.png'

    return decrypt

def evaluate(original_path, crypted_path):
    # open the image
    original_image = np.array(Image.open(original_path).convert('RGB')).astype('float64')
    crypted_image = np.array(Image.open(crypted_path).convert('RGB')).astype('float64')

    # MSE (Mean Squared Error)
    mse = np.mean((original_image - crypted_image) ** 2)

    # PSNR (Peak Signal-to-Noise Ratio)
    max_pixel_value = 255.0
    psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))

    return mse, psnr
