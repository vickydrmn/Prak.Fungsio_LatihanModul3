def konversi(m):
    def hari(h):
        def jam(j):
            def menit(mn):
                return m * 7 * 24 * 60 + h * 24 * 60 + j * 60 + mn
            return menit
        return jam
    return hari

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

hasil_konversi = []

for item in data:
    data_split = item.split()
    m = int(data_split[0])
    h = int(data_split[2])
    j = int(data_split[4])
    mn = int(data_split[6])

    konvert = konversi(m)(h)(j)(mn)

    hasil_konversi.append(konvert)

for item in hasil_konversi:
    print(item)
