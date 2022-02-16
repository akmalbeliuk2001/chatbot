import random

R_MAKAN = "Saya tidak suka makan apa pun karena saya bot!"


def unknown():
    response = ["Bisakah Anda mengucapkan ulang kata itu? ",
                "...",
                "Silakan masukkan kata dengan benar, karena bot tidak mengerti.",
                "Maaf, bot tidak mengerti yang anda maksud"][
        random.randrange(4)]
    return response