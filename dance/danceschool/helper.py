import qrcode
from .models import Profile


def get_qr_code():
    id_profile = Profile.id
    url = "127.0.0.1:8000" + "/profile/" + str(id_profile)
    # 1 строка будет изменена на домен(как только мы выйдем за рамки локальной разработки)
    img = qrcode.make(url)
    img.save("media/qr/test.png")
    qr_image = True
    return qr_image
