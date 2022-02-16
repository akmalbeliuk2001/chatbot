import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Menghitung berapa banyak kata yang ada di setiap pesan yang sudah ditentukan sebelumnya
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Hitung persentase kata yang dikenali dalam pesan pengguna
    percentage = float(message_certainty) / float(len(recognised_words))

    # Memeriksa bahwa kata-kata yang diperlukan ada dalam string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Harus memiliki kata-kata yang diperlukan, atau menjadi respons tunggal
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Menyederhanakan pembuatan respons / menambahkannya ke kamus
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Respon -------------------------------------------------------------------------------------------------------
    response('Hallo, ada yang bisa kami bantu?', ['hallo', 'hi', 'hey', 'sup', 'heyo', 'selamaset', 'pagi', 'siang', 'sore', 'malam'],
             single_response=True)
    response('Ketersediaan barang bisa dilihat melalui catalog', ['Apakah', 'produk', 'masih', 'ada', 'stock'],
             single_response=True)
    response('Silahkan isi form pembelian berikut:\n\t Nama lengkap\t:\n\t Alamat lengkap\t:\n\t No telpon\t\t:',
             ['bagaimana', 'cara', 'pemesanan', 'pemesanannya'], single_response=True)
    response('Pembayaran melalui metode transfer atau COD, Metode apa yang anda pilih?', ['bagaimana', 'cara', 'pembayaran', 'pembayarannya'],
             required_words=['pembayarannya'])
    response('Silahkan transfer ke no.rek berikut: \n\t Bank\t: BNI \n\t No.Rek\t: 012-345-678\n\t a/n\t: Maju makmur', ['transfer'],
             single_response=True)
    response('Pembayaran bisa dilakukan kepada kurir yang mengantar saat barang sudah tiba ditujuan. ', ['cod'],
             single_response=True)
    response('Terimakasih sudah berkunjung!', ['terimakasih', 'oke', 'bye', 'goodbye'],
             single_response=True)

    # Respon panjang
    response(long.R_MAKAN, ['apa', 'kamu', 'sudah', 'makan'], required_words=['makan'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    return best_match

    # return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Digunakan untuk mendapatkan tanggapan
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Menguji sistem respons
while True:
    print('Bot: ' + get_response(input('You: ')))