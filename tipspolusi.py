import random
def tipschoosing():
    tip = ""
    tipnum = random.randint(1,10)

    if tipnum == 1:
        tip = "**Gunakan kembali kantong belanja**"
    elif tipnum == 2:
        tip = "**Matikan listrik saat tidak dugunakan**"
    elif tipnum == 3:
        tip = "**Kurangi penggunaan kendaraan bermotor**"
    elif tipnum == 4:
        tip = "**Pilah dan daur ulang sampah**"
    elif tipnum == 5:
        tip = "**Gunakan produk pembersih ramah lingkungan**"
    elif tipnum == 6:
        tip = "**Kurangi konsumsi air yang tidak berguna**"
    elif tipnum == 7:
        tip = "**Tanam pohon atau tanaman hias di rumah**"
    elif tipnum == 8:
        tip = "**Kurangi pembakaran sampah**"
    elif tipnum == 9:
        tip = "**Masak di rumah dan kurangi makanan kemasan**"
    elif tipnum == 10:
        tip = "**Gunakan lampu LED hemat energi**"
    return tip
