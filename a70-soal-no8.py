import math

klaim = [2, 3, 4]
probabilitas = [0.5, 0.3, 0.2]

manfaat = [0, 10]
peluang_manfaat = [0.7, 0.3]

ekspetasi = sum([klaim[i] * probabilitas[i] * manfaat[j] * peluang_manfaat[j] for i in range(len(klaim)) for j in range(len(manfaat))])
standar_deviasi = math.sqrt(sum([klaim[i] * probabilitas[i] * (manfaat[j] - ekspetasi) ** 2 for i in range(len(klaim)) for j in range(len(manfaat))]))

threshold = ekspetasi + 2.5 * standar_deviasi

peluang = sum([probabilitas[i] * peluang_manfaat[j] for i in range(len(klaim)) for j in range(len(manfaat)) if (klaim[i] * manfaat[j]) > threshold])

jawaban = round(peluang * 100, 1)

print("Peluang total nilai manfaat yang lebih besar dari threshold: {}%".format(jawaban))
