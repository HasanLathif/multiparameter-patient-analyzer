# normal ecg = 60 <= ecg <= 99 (in BPM)
# normal respiration = 12 <= respiration <= 16
# normal spo2 = 95 <= spo2 <= 100
# normal nibps = 90 <= nibps <= 120 (Sistolik)
# or
# normal nibpd = 60 <= nibpd <= 80 (Diastolik)
# normal temperature = 36.6 <= temperature <= 37.2 (Celcius)
# normal ibps = 90 <= ibps <= 120 (Sistolik)
# or
# normal ibpd = 60 <= ibpd <= 80 (Diastolik)
# normal etco2 = 35 <= etco2 <= 45 (mmHg)
# full sentence
# 60 <= ecg <= 99 and 12 <= respiration <= 16 and 95 <= spo2 <= 100 and ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and 36.6 <= temperature  37.2.2 and ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and 35 <= etco2 <= 45:

ecg = float(input("Insert ECG Number: "))
respiration = float(input("Insert Respiration Number: "))
spo2 = float(input("Insert SPO2 Number: "))
nibps = float(input("Insert NIBPS Number: "))
nibpd = float(input("Insert NIBPD Number: "))
temperature = float(input("Insert Temperature Number: "))
ibps = float(input("Insert IBPS Number: "))
ibpd = float(input("Insert IBPD Number: "))
etco2 = float(input("Insert ETCO2 Number: "))

if (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["You Are All Good ^_^"]
    print("No abnormalities detected! Probabilities for possible conditions:")
    print(conditions)

#Hasan mulai dari sini
#High
#ECG, SPO2, ETCO2	Terlalu tinggi 1
elif (ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Hiperventilasi, Gangguan pernapasan, Masalah jantung, Keracunan karbon dioksida"]
    print("High ECG, SpO2, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, NIBP, Temperature	Terlalu tinggi 2
elif (ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Sepsis, vasculitis, hipertiroidisme, aritmia"]
    print("High ECG, NIBP, and Temperature detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, NIBP, IBP	Terlalu tinggi 3
elif (ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi, aterosklerosis, hipertiroidisme, gangguan neurologis"]
    print("High ECG, NIBP, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, NIBP, ETCO2	Terlalu tinggi 4
elif (ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Takikardia, hipertensi, hiperventilasi"]
    print("High ECG, NIBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, Temperature, IBP	Terlalu tinggi 5
elif (ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = [" Aritmia, sepsis, tirotoksikosis, reaksi inflamasi, gangguan sistem saraf pusat"]
    print("High ECG, Temperature, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, Temperature, ETCO2	Terlalu tinggi 6
elif (ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = [" Infark miokard, demam, penyakit paru-paru, infeksi, hipertiroidisme"]
    print("High ECG, Temperature, and ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, IBP, ETCO2 Terlalu tinggi 7
elif (ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Hipertensi, serangan jantung, gangguan pernapasan, gangguan asam-basa"]
    print("High ECG, IBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, SPO2, NIBP Terlalu tinggi 8
elif (60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Penyakit paru obstruktif kronis (PPOK), hipoksia, hipertensi"]
    print("High Respiration, SpO2, and NIBP detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, SPO2, Temperature	Terlalu tinggi 9
elif (60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Takipnea, hiperventilasi, demam, infeksi"]
    print("Respiration, SpO2, and Temperature detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, SPO2, IBP	Terlalu tinggi 10
elif (60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        (( ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Gangguan sistem pernapasan, hiperventilasi, hipertensi"]
    print("Respiration, SpO2, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, SPO2, ETCO2	Terlalu tinggi 11
elif (60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Hiperventilasi, hipoksia, hiperkapnia"]
    print("High Respiration, SPO2, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, NIBP, Temperature	Terlalu tinggi 12
elif (60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or ( nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Infeksi saluran pernapasan, sepsis, hipertiroidisme,  aritmia"]
    print("High ECG, NIBP, and Temperature detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, NIBP, IBP Terlalu tinggi 13
elif (60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or ( nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or ( ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Penyakit paru obstruktif kronik (PPOK),  penyakit katup jantung, asidosis, penyakit ginjal, hipotiroidisme"]
    print("High Respiration, NIBP, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, NIBP, ETCO2	Terlalu tinggi 14
elif (60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or ( nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
         etco2 > 45):
    conditions = ["Takipnea,  pneumonia, emboli paru, hipoksia, penyakit jantung, aneurisma, hipoventilasi, penyakit ginjal"]
    print("High Respiration, NIBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, Temperature, IBP	Terlalu tinggi 15
elif (60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Kegagalan jantung, bronkitis, asma, sepsis, arthritis reumatoid, jantung koroner, ginjal polikistik, aterosklerosis"]
    print("High Respiration, Temperature, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, Temperature, ETCO2	Terlalu tinggi 16
elif (60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Gangguan paru obstruktif kronis (COPD), gangguan tiroid, flu, radang tenggorokan, hipoventilasi, pneumonia, asma "]
    print("High Respiration, Temperature, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, IBP, ETCO2	Terlalu tinggi 17
elif (60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or ( ibpd > 80)) and
        etco2 > 45):
    conditions = ["Kelelahan, asma, emboli paru, stroke, gangguan neuromuskular"]
    print("High Respiration, IBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)


#SPO2, NIBP, Temperature	Terlalu tinggi 18
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Gangguan pernapasan, penyakit jantung, gagal ginjal,  infeksi saluran kemih, sepsis"]
    print("High SpO2, NIBP, and Temperature detected! Probabilities for possible conditions:")
    print(conditions)

#SPO2, NIBP, IBP	Terlalu tinggi	19
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or ( nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or ( ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipoksia, pneumonia, emboli paru, stres, hipertensi maligna, gagal jantung, gagal ginjal "]
    print("High SpO2, NIBP, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#SPO2, NIBP, ETCO2	Terlalu tinggi	20
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        (( nibps > 120) or ( nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Hiperventilasi, penyakit jantung, stroke, gangguan pernapasan, gagal napas"]
    print("High SpO2, NIBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#SPO2, Temperature, IBP	Terlalu tinggi
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        (( ibps > 120) or ( ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Penyakit paru obstruktif kronis (PPOK), pneumonia, infeksi saluran kemih, inflamasi, jantung koroner, stroke"]
    print("High SpO2, Temperature, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#SPO2, Temperature, ETCO2	Terlalu tinggi
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Polisitemia vera, influenza,  penyakit paru-obstruktif kronis (PPOK), infeksi saluran kemih, kelelahan, hiperkapnia"]
    print("High SpO2, Temperature , and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#SPO2, IBP, ETCO2	Terlalu tinggi
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or ( ibpd > 80)) and
        etco2 > 45):
    conditions = ["Penyakit jantung, stroke, penyakit ginjal, masalah sirkulasi, hipoventilasi, polisitemia vera, hiperkapnia"]
    print("High SpO2, IBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#NIBP, Temperature, IBP	Terlalu tinggi
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        (( nibps > 120) or ( nibpd > 80)) and
        temperature > 37.2 and
        (( ibps > 120) or ( ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Stroke, gagal jantung, infeksi, flu, pilek, hipertensi arteri pulmonalis, sesak napas, nyeri dada"]
    print("High NIBP, Temperature, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#NIBP, Temperature, ETCO2	Terlalu tinggi
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        (( nibps > 120) or ( nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Serangan jantung, stroke, infeksi saluran pernapasan, infeksi saluran kemih,  hiperkapnia, gagal napas"]
    print("High NIBP, Temperature, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#NIBP, IBP, ETCO2	Terlalu tinggi
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        (( nibps > 120) or ( nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        (( ibps > 120) or ( ibpd > 80)) and
        etco2 > 45):
    conditions = ["Hipoventilasi,  penyakit jantung, penyakit pembuluh darah, penyakit yang mempengaruhi sirkulasi darah"]
    print("High NIBP, IBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#Temperature, IBP, ETCO2	Terlalu tinggi
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        (( ibps > 120) or ( ibpd > 80)) and
        etco2 > 45):
    conditions = ["Hiperkapnia, artritis, demam, sepsis, sindrom hipertermi maligna, hipertensi arteri pulmonalis, pneumonia"]
    print("High Temperature, IBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#Low

#ECG, Respiration, SPO2	Terlalu rendah
elif ( ecg < 60  and
        respiration < 12  and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Bradikardia, blok jantung, hipoksia, asma, bronkitis kronis, penyakit paru obstruktif kronik (PPOK), gagal jantung"]
    print("Low ECG, Respiration, and SpO2 detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, Respiration, NIBP	Terlalu rendah
elif ( ecg < 60  and
        respiration < 12  and
        95 <= spo2 <= 100 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotensi, hipotiroidisme, aritmia, penyakit jantung koroner, sesak napas"]
    print("Low ECG, Respiration, and NIBP detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, Respiration, Temperature	Terlalu rendah
elif (  ecg < 60 and
        respiration < 12  and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6  and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Bradikardia, infark miokard, hipokapnia, hipotiroidisme, gangguan kelenjar adrenal, syok"]
    print("Low ECG, Respiration, and Temperature detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, Respiration, IBP	Terlalu rendah
elif ( ecg < 60 and
        respiration < 12  and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        35 <= etco2 <= 45):
    conditions = ["Bradikardia, iskemia miokard, hipoksia, gangguan saraf, keracunan obat, hipotensi"]
    print("Low ECG, Respiration, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, Respiration, ETCO2	Terlalu rendah 	5
elif ( ecg < 60 and
        respiration < 12  and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35  ):
    conditions = ["Bradikardia, gangguan konduksi jantung, gangguan pernapasan, gangguan neurologis, gangguan metabolik."]
    print("Low ECG, Respiration, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, SPO2, NIBP	Terlalu rendah	6
elif ( ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotensi, gagal jantung, aritmia,  hipovolemia, asma, pneumonia, hipotiroidisme, efek samping obat"]
    print("Low ECG, SpO2, and NIBP detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, SPO2, Temperature	Terlalu rendah	7
elif ( ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95  and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6  and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotermia,  syok, gagal jantung, pneumonia, aritmia, hipoksia	"]
    print("Low ECG, SpO2, dan Temperature detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, SPO2, IBP	Terlalu rendah	 8
elif ( ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        35 <= etco2 <= 45):
    conditions = ["Bradikardia, masalah pernapasan, penyakit paru-paru, gangguan sirkulasi, anafilaksis, infeksi sistemik"]
    print("Low ECG, SpO2, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, SPO2, ETCO2	Terlalu rendah	9
elif ( ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35 ):
    conditions = ["Aritmia, gagal jantung, penyakit paru obstruktif kronis (PPOK), hipovolemia, syok, emboli, atau perdarahan"]
    print("Low ECG, SpO2, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, NIBP, Temperature	Terlalu rendah 10
elif ( ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        temperature < 36.6  and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Dehidrasi,  pendarahan internal, sepsis, hipotermia, gagal jantung, hipotensi"]
    print("Low ECG, NIBP, and Temperature detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, NIBP, IBP	Terlalu rendah	11
elif ( ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        35 <= etco2 <= 45):
    conditions = ["gagal jantung, bradikardia, dehidrasi, efek samping obat-obatan tertentu, syok, infeksi berat"]
    print("Low ECG, NIBP, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, NIBP, ETCO2	Terlalu rendah	12
elif ( ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
         etco2 < 35 ):
    conditions = ["Hipovolemia, aritmia, atau infark miokard, stroke, anafilaksis, sepsis, efek samping obat"]
    print("Low ECG, NIBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, Temperature, IBP	Terlalu rendah	13
elif ( ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        35 <= etco2 <= 45):
    conditions = ["Bradikardia, blok jantung, hipotermia, dehidrasi, perdarahan, infeksi berat, gagal jantung, masalah dengan sistem vaskular"]
    print("Low ECG, Temperature, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, Temperature, ETCO2	14
elif ( ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35 ):
    conditions = ["Terlalu rendah	Hipovolemik, syok kardiogenik, syok septik, hipotermia, obstruksi saluran napas, asma, atau gagal napas"]
    print("Low ECG, Temperature, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, IBP, ETCO2	Terlalu rendah 	15
elif (ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        etco2 < 35 ):
    conditions = ["Aritmia, bradikardia, syok, gagal jantung, perdarahan internal, emboli paru, gangguan sirkulasi, hipoperfusi sistemik"]
    print("Low ECG, IBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, SPO2, NIBP 16
elif (60 <= ecg <= 99 and
        respiration < 12  and
        spo2 < 95 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Pneumonia, emboli paru, penyakit paru obstruktif kronis (PPOK), gagal jantung, syok, anemia, perdarahan yang signifikan"]
    print("Low Respiration, SpO2, and NIBP detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, SPO2, Temperature	Terlalu rendah	17
elif (60 <= ecg <= 99 and
        respiration < 12  and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6  and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipoksia, pneumonia, gagal jantung, syok,  hipotermia,  asma, bronkitis kronis"]
    print("Low Respration, SpO2, and Temperature detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, SPO2, IBP	Terlalu rendah 	18
elif (60 <= ecg <= 99 and
        respiration < 12  and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        35 <= etco2 <= 45):
    conditions = ["Hipotensi, dehidrasi, infeksi berat, syok, kegagalan organ, hipoksia, edema paru, emboli paru, masalah kardiovaskular"]
    print("Low Respiration, SpO2, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, SPO2, ETCO2	Terlalu rendah	19
elif (60 <= ecg <= 99 and
        respiration < 12  and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35  ):
    conditions = ["Asma, bronkitis kronis, hipoksia, pneumonia, gagal jantung, gagal ginjal, atau sepsis dystrofi otot, miastenia gravis, poliomielitis sleep apnea"]
    print("Low Respiration, SpO2, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, NIBP, Temperature	Terlalu rendah	20
elif (60 <= ecg <= 99 and
        respiration < 12  and
        95 <= spo2 <= 100 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        temperature < 36.6  and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotermia, gagal pernapasan, obstruksi saluran napas, syok, asma, hipotensi, anafilaksis, infeksi yang parah"]
    print("Low Respiration, NIBP, and Temperature detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, NIBP, IBP	Terlalu rendah	21
elif (60 <= ecg <= 99 and
        respiration < 12  and
        95 <= spo2 <= 100 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        35 <= etco2 <= 45):
    conditions = ["Syok, perdarahan berat, sepsis, hipotensi ortostatik, dehidrasi, gangguan sistem saraf otonom, asma, bronkitis kronis"]
    print("Low Respiration, NIBP, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, NIBP, ETCO2	Terlalu rendah	22
elif (60 <= ecg <= 99 and
        respiration < 12  and
        95 <= spo2 <= 100 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35  ):
    conditions = ["Hipotensi, perdarahan, kerusakan organ, hipoksemia, pneumonia, emboli paru, atau penyakit paru obstruktif kronik (PPOK), hiperkapnia"]
    print("Low Respiration, NIBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, Temperature, IBP	Terlalu rendah	23
elif (60 <= ecg <= 99 and
        respiration < 12  and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6  and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        35 <= etco2 <= 45):
    conditions = ["Pneumonia, edema paru, pneumotoraks, apnea sleep, hipotermia, hipotiroidisme, gagal jantung, syok, hipoglikemia"]
    print("Low Respiration, Temperature , and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, Temperature, ETCO2	Terlalu rendah	24
elif (60 <= ecg <= 99 and
        respiration < 12  and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
         temperature < 36.6  and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35  ):
    conditions = ["Hipotiroidisme, hipoglikemia, syok, keracunan, gangguan metabolisme asam-basa, gangguan ginjal, obstruksi saluran napas, hipotiroidisme, gagal napas"]
    print("Low Respiration, Temperature, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#Respiration, IBP, ETCO2	Terlalu rendah 	25
elif (60 <= ecg <= 99 and
        respiration < 12  and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        etco2 < 35  ):
    conditions = ["Syok, hipovolemia, pendarahan berat, dehidrasi yang parah, gagal napas, obstruksi saluran napas, atau hiperventilasi"]
    print("Low Respiration, IBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#SPO2, NIBP, Temperature	Terlalu rendah	 26
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        temperature < 36.6  and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipoksia, gangguan pernapasan, anemia, hipotensi, dehidrasi, perdarahan, infeksi sistemik, hipotermia, hipotiroidisme"]
    print("Low SpO2, NIBP, and Temperature detected! Probabilities for possible conditions:")
    print(conditions)

#SPO2, NIBP, IBP	Terlalu rendah 	27
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        35 <= etco2 <= 45):
    conditions = ["Pneumonia, penyakit paru obstruktif kronik (PPOK), asma, hipovolemia, infeksi septikemia, aritmia, efek samping obat, hipotensi"]
    print("Low SpO2, NIBP, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#SPO2, NIBP, ETCO2	Terlalu rendah	28
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35  ):
    conditions = ["Hipotensi, kegagalan jantung, perdarahan, syok, atau dehidrasi berat, hiperventilasi, gagal ginjal, gagal hati, sepsis, anemia, keracunan karbon monoksida"]
    print("Low SpO2, NIBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#SPO2, Temperature, IBP	Terlalu rendah	29
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6  and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        35 <= etco2 <= 45):
    conditions = ["Hipoksia, pneumonia, penyakit paru obstruktif kronik (PPOK), emboli paru, aritmia, anemia berat, hipotermia, hipotiroidisme, stroke, hipotensi"]
    print("Low SpO2, Temperature, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#SPO2, IBP, ETCO2	31
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6  and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        etco2 < 35  ):
    conditions = ["Terlalu rendah	Hipoksia, anemia, hipotensi, dehidrasi, perdarahan, kegagalan jantung, syok, hiperventilasi, hipoperfusi"]
    print("Low SpO2, IBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#NIBP, Temperature, IBP	Terlalu rendah	32
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        temperature < 36.6  and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        35 <= etco2 <= 45):
    conditions = ["Hipotens, dehidrasi, pendarahan internal, infeksi berat, alergi, gangguan hormonal, hipotermia, gagal jantung, syok, emboli, atau kerusakan pada pembuluh darah"]
    print("Low NIBP, Temperature, and IBP detected! Probabilities for possible conditions:")
    print(conditions)

#NIBP, Temperature, ETCO2	Terlalu rendah	33
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35  ):
    conditions = ["Hipotensi, dehidrasi, perdarahan, kegagalan jantung, hipotermia, hiperventilasi, stres, asma,  gangguan panik"]
    print("Low NIBP, Temperature, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#NIBP, IBP, ETCO2	Terlalu rendah	34
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90 ) or ( nibpd < 60 )) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        etco2 < 35  ):
    conditions = ["Hipotensi, dehidrasi, perdarahan internal, infeksi, gagal jantung, efek samping obat, syok, hiperventilasi, stres, asma, penyakit paru obstruktif kronis (PPOK)"]
    print("Low NIBP, IBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#Temperature, IBP, ETCO2	Terlalu rendah 	35
elif (60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6  and
        ((ibps < 90 ) or ( ibpd < 60 )) and
        etco2 < 35  ):
    conditions = ["Hipotermia, infeksi, hipoglikemia hipotensi, dehidrasi, perdarahan, gangguan jantung, infeksi, anafilaksis, hipotiroidisme, edema paru, emboli paru, hipovolemia"]
    print("Low Temperature, IBP, and EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)

#ECG, Respiration, SPO2, NIBP	Terlalu tinggi	36
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((nibps > 120) or ( nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi, aritmia, asma, pneumonia,  gagal jantung, hipoksia"]
    print("Low ECG, Respiration, SpO2, and NIBP detected! Probabilities for possible conditions:")
    print(conditions)
#Hasan Akhir
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Takikardia sinus, Aritmia atrial, Aritmis ventrikel"]
    print("High ECG detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Kecemasan dan stres, Gangguan kecemasa, Gangguan pernapasan, Gangguan metabolik, Kondisi neurologis"]
    print("High Respiration detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Penyakit paru-paru, Gangguan sirkulasi, Kondisi kongenital"]
    print("High SpO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Stres, Faktor genetik, Faktor hormon"]
    print("High Non-Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Infeksi, Inflamasi, Reaksi obat, Penyakit autoimun, Gangguan tiroid, Kanker"]
    print("High Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Faktor gaya hidup tidak sehat, Faktor genetik, Usia, Faktor hormon, Stres"]
    print("High Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Gangguan pernapasan, Gangguan neurologis, Gangguan otot pernapasan, Overdosis obat atau alkohol, Gangguan fungsi tiroid"]
    print("High EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Bradikardia, Iskemia jantung, Gangguan elektrolit"]
    print("Low ECG detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Penyakit pernapasan, Gangguan neurologis, Gangguan metabolik, Gangguan jantung"]
    print("Low Respiration detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Gangguan pernapasan, Gangguan sirkulasi, Hiperventilasi, Gangguan pada aliran darah ke paru-paru, Anemia"]
    print("Low SpO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Dehidrasi, Pendarahan, Gangguan jantung, Gangguan endokrin, Infeksi, Vasodilatasi"]
    print("Low Non-Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Kondisi medis, Pengaruh obat-obatan"]
    print("Low Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Dehidrasi, Pendarahan, Gangguan jantung, Gangguan endokrin, Infeksi, Vasodilatasi"]
    print("Low Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Hiperventilasi, Gangguan pernapasan, Gangguan sirkulasi, Hipotermia, Kehilangan darah berat, Penggunaan obat tertentu"]
    print("Low EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Ansietas atau stres, Hipertirodisme, Pneumonia atau infeksi paru-paru, Gangguan jantung, Gangguan metabolik, Efek obat atau stimulan"]
    print("High ECG, Respiration detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hiperventilasi, Kompensasi respirator, Kondisi jantung yang meningkatkan suplai oksigen, Efek samping obat"]
    print("High ECG, SpO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi, Stres atau kecemasan, Efek samping obat, Gangguan hormonal, Gangguan ginjal"]
    print("High ECG, Non-Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Demam, Infeksi, Gangguan inflamasi, Efek samping obat, Gangguan endokrin"]
    print("High ECG, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi, Stres atau kecemasan, Gangguan hormonal, Gangguan ginjal, Penyakit pembuluh darah"]
    print("High ECG, Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Hiperventilasi, Gangguan pernapasan, Metabolisme yang meningkat, Gangguan jantung, Gangguan metabolisme asam-basa"]
    print("High ECG, EtO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Stres, Gangguan metabolik, Kondisi kardiovaskular, Kondisi paru-paru"]
    print("High Respiration, SpO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Stres, Hipertensi, Gangguan tiroid, Adrenaline surge, Efek samping obat"]
    print("High Respiration, Non-Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Demam, Infeksi sistemik, Gangguan metabolik, Penyakit inflamasi, Gangguan pernapasan"]
    print("High Respiration, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Kegagalan jantung kongestif, Hipertensi, Kondisi inflamasi, Gangguan tiroid, Gangguan neurologis"]
    print("High Respiration, Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Kelebihan karbondioksida, Asidosis respiratorik, Gangguan metabolik, Gangguan sistem saraf pusat, Stres"]
    print("High Respiration, EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi, Hipoksia, Gangguan pernapasan, Gangguan sistem saraf pusat, Stres"]
    print("High SpO2, Non-Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Infeksi, Gangguan inflamasi, Overdosis obat, Gangguan sistem saraf pusat, Gangguan endokrin"]
    print("High SpO2, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi, Gangguan pernapasan, Gangguan kardiovaskular, Stres, Gangguan endokrin"]
    print("High SpO2, Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Hiperventilasi, Kelebihan oksigen, Gangguan pernapasan"]
    print("High SpO2, EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi, Demam, Hipertiroidisme, Gangguan hormonal"]
    print("High Non-Invasive Blood Pressure, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi"]
    print("High Non-Invasive Blood Pressure, Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Gangguan pernapasan, Gangguan kardiovaskuler, Hipertiroidisme, Stres"]
    print("High Non-Invasive Blood Pressure, EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Infeksi, Gangguan kardiovaskular, Heartstroke, Sindrom serotonin"]
    print("High Temperature, Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Demam, Gangguan pernapasan, Gangguan metabolisme, Overdosis obat atau gangguan natrkotika, Gangguan kaardiovaskuler"]
    print("High Temperature, EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Hipertensi, Gangguan pernapasan, Gangguan kardiovaskular, Gangguan hormonal"]
    print("High Invasive Blood Pressure, EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotensi, Gangguan pernapasan, Depresi pernapasan, Gangguan metabolik, Gangguan jantung, Gangguan neuromuskuler"]
    print("Low ECG, Respiration detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipoksia, Gangguan pernapasan, Gangguan sirkulasi, Gangguan jantung, Hipotensi"]
    print("Low ECG, SpO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotensi, Gangguan jantung, Gangguan hormonal, Dehidradi, Efek samping obat, Gangguan neurologis"]
    print("Low ECG, Non-Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotermia, Gangguan hormon tiroid, Infeksi berat, Gangguan sirkulasi, Racun atau efek samping obat"]
    print("Low ECG, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotensi, Gangguan jantung, Gangguan hormonal, Efek samping obat, Gangguan neurologis"]
    print("Low ECG, Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Hipoperfusi, Gangguan pernapasan, Gangguan ventilasi, Hipotermia"]
    print("Low ECG, EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Gangguan pernapasan, Gangguan ventilasi, Gangguan metabolik, Gangguan hematologi, Gangguan sirkulasi"]
    print("Low Respiration, SpO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipovolemia, Syok, Gagal jantung, Gangguan pernapasan, Kondisi neurologis"]
    print("Low Respiration, Non-Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotermia, Gangguan pernapasan, Kerusakan sistem saraf pusat, Gangguan hormonal, Kondisi kardiovaskular"]
    print("Low Respiration, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Syok, Hipovolemia, Gagal jantung, Gangguan pernapasan, Gangguan neurologis"]
    print("Low Respiration, Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Hipokapnia, Hiperventilasi, Gangguan sistem saraf pusat, Gangguan metabolik, Penurunan aliran darah ke paru-paru"]
    print("Low Respiration, EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipovolemia, Syok, Gangguan pernapasan, Gangguan jantung, Gangguan sirkulasi perifer"]
    print("Low SpO2, Non-Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotermia, Gangguan pernapasan, Gangguan sirkulasi, Gangguan hormonal, Overdosis obat atau keracunan"]
    print("Low SpO2, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Hipovolemia, Syok, Gangguan pernapasan, Gangguan jantung, Kegagalan organ sistemik"]
    print("Low SpO2, Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Hipoksia, Gangguan pernapasan, Gangguan sirkulasi, Gangguan metabolik"]
    print("Low SpO2, EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotensi, Hipotermia, Syok, Gangguan hormonal"]
    print("Low Non-Invasive Blood Pressure, temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Dehidrasi, Pendarahan, Gangguan jantung, Infeksi berat, Efek samping anestesi"]
    print("Low Non-Invasive Blood Pressure, Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Hipovolemia, Gangguan pernapasan, Gangguan kardiovaskular, Hipotermia, Gangguan metabolisme"]
    print("Low Non-Invasive Blood Pressure, EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotermia, Syok, Gangguan sirkulasi, Gangguan endokrin, Penyakit sistematik"]
    print("Low Temperature, Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Hipotermia, Gangguan pernapasan, Gangguan sirkulasi, Overdosis obat atau racun, Gangguan metabolisme"]
    print("Low Temperature, EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Hipotensi, Gangguan pernapasan, Gangguan sirkulasi, Gangguan metabolik, Efek samping obat"]
    print("Low Invasive Blood Pressure, EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Stres, Hiperventilasi, Penyakit paru obstruktifkronik (PPOK), Penyakit jantung, Hipertiroidisme"]
    print("High ECG, Respiration, SpO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi, Stres, Penyakit kardiovaskular, Gangguan pernapasan, Efek samping obat"]
    print("High ECG, Respiration, Non-Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Demam, Infeksi, Heartstroke, Gangguan tiroid, Kondisi inflamasi"]
    print("High ECG, Respiration, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi, Gangguan kardiovaskular, Gangguan pernapasan, Gangguan tiroid, Stres"]
    print("High ECG, Respiration, Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Peningkatan kebutuhan oksigen, Gangguan pernapasan, Gangguan kardiovaskular, Metabolik asidosis, Kegagaglan pernapasan"]
    print("High ECG, Respiration, EtCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi, Gangguan kardiovaskular, Gangguan pernapasan, Gangguan sistemik, Stres"]
    print("High ECG, SpO2, Non Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Demam, Infeksi sistemik, Gangguan inflamasi, Kegagalan organ, Efek samping obat"]
    print("High ECG, SpO2, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi, Gangguan kardiovaskular, Sindrom stres tak terkontrol, Gangguan tiroid, Keracunan obat atau overdosis"]
    print("High ECG, SpO2, Invasive Blood Pressure detected! Probabilities for possible conditions:")
    print(conditions)
#Jaki mulai
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Dehidrasi, Pneumonia, aritmia, hipertiroid, ketoasidosis, sepsis, diabetes melitus, hipertensi, gangguan neurologis"]
    print("High ECG, Respiration, SPO2, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Sepsis, Keracunan, Reaksi alergi serius"]
    print("High ECG, Respiration, SPO2, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Gangguan kegawatan, Sepsis, Gagal multiorgan, Sindrom Takutsubo, Hipoksia, Asidosis Respiratorik"]
    print("High ECG, Respiration, SPO2, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Infeksi Sistemik/pernapasan, Heatstroke, Gangguan sistemik"]
    print("High ECG, Respiration, NIBP, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Gangguan ginjal, Keracunan/Overdosis Substansi, Gangguan kardiovaskular, Hipertensi darurat"]
    print("High ECG, Respiration, NIBP, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Gangguan neuromuskuler, Gangguan Pernapasan, Asidosis metabolik"]
    print("High ECG, Respiration, NIBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Infeksi sistemik, Sepsis, Hipertiroid, Gangguan kardiovaskular, Gangguan pernapasan"]
    print("High ECG, Respiration, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Sepsis, Overdosis substansi, Gangguan Jantung, Hipertermia"]
    print("High ECG, Respiration, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Stress/Kritis, Hipertensi, PPOK, Emboli Paru, Asidosis Metabolik, Ketoasidosis,  Gangguan metabolik"]
    print("High ECG, Respiration, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Infeksi multiorgan, Gangguan kardiovaskular, Inflamasi organ pernapasan"]
    print("High ECG, SPO2, NIBP, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Efek samping obat, Gangguan pernapasan (PPOK dan Lainnya), Jantung Koroner, Stress, Hipertensi"]
    print("High ECG, SPO2, NIBP, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Efek samping obat, Kegagalan dan penyakit paru, stress/kecemasan"]
    print("High ECG, SPO2, NIBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Infeksi sistemik berat, Kerusakan organ, Krisis hipertensi, Sindrom metabolik"]
    print("High ECG, SPO2, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Infeksi organ, Hipertiroidisme, Gangguan pernapasan, Reaksi pada obat"]
    print("High ECG, SPO2, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Infeksi serius, Hipertiroidisme, Reaksi terhadap obat, Gangguan Kardiovaskular"]
    print("High ECG, SPO2, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Kerusakan organ, Infeksi sistemik, Sindrom metabolik. Gangguan ritme jantung"]
    print("High ECG, NIBP, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Infeksi serius, Hipertiroidisme, Reaksi terhadap obat, Gangguan Kardiovaskular"]
    print("High ECG, NIBP, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Metabolisme asam-basa terganggu, gangguan kardiovaskular, infeksi organ, gangguan sistemik"]
    print("High ECG, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Efek samping obat, Gangguan pernapasan (PPOK dan Lainnya), Jantung Koroner, Stress, Hipertensi"]
    print("High ECG, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Efek samping obat, Kegagalan dan penyakit paru, stress/kecemasan"]
    print("High Respiration, SPO2, NIBP, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Infeksi sistemik berat, Kerusakan organ, Krisis hipertensi, Sindrom metabolik"]
    print("High Respiration, SPO2, NIBP, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        95 > spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Infeksi organ, Hipertiroidisme, Gangguan pernapasan, Reaksi pada obat"]
    print("High Respiration, SPO2, NIBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Infeksi serius, Hipertiroidisme, Reaksi terhadap obat, Gangguan Kardiovaskular"]
    print("High Respiration, SPO2, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Kerusakan organ, Infeksi sistemik, Sindrom metabolik. Gangguan ritme jantung"]
    print("High Respiration, SPO2, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Infeksi serius, Hipertiroidisme, Reaksi terhadap obat, Gangguan Kardiovaskular"]
    print("High Respiration, SPO2, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Metabolisme asam-basa terganggu, gangguan kardiovaskular, infeksi organ, gangguan sistemik"]
    print("High Respiration, NIBP, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Gangguan kegawatan, Sepsis, Gagal multiorgan, Sindrom Takutsubo, Hipoksia, Asidosis Respiratorik"]
    print("High Respiration, NIBP, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Infeksi Sistemik/pernapasan, Heatstroke, Gangguan sistemik"]
    print("High Respiration, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Gangguan ginjal, Keracunan/Overdosis Substansi,  Gangguan kardiovaskular, Hipertensi darurat"]
    print("High Respiration, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Gangguan neuromuskuler, Gangguan Pernapasan, Asidosis metabolik"]
    print("High SPO2, NIBP, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Kerusakan organ, Infeksi sistemik, Sindrom metabolik. Gangguan ritme jantung"]
    print("High SPO2, NIBP, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Infeksi serius, Hipertiroidisme, Reaksi terhadap obat, Gangguan Kardiovaskular"]
    print("High SPO2, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Metabolisme asam-basa terganggu, gangguan kardiovaskular, infeksi organ, gangguan sistemik"]
    print("High SPO2, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Dehidrasi, Pneumonia, aritmia, hipertiroid, ketoasidosis, sepsis, diabetes melitus, hipertensi, gangguan neurologis"]
    print("High NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 66 and
        respiration < 12 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Gangguan Kardiovaskular, Hipoksia, Hipotensi krisis, Gangguan pernapasan dan sirkulasi"]
    print("Low ECG, Respiration, SPO2, NIBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotiroidisme, Gangguan sirkulasi, Gangguan pernapasan, Hipotermia"]
    print("Low ECG, Respiration, SPO2, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Krisis Syok, Hipoksia, Gangguan pernapasan, Gangguan jantung, Hipotensi"]
    print("Low ECG, Respiration, SPO2, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Kegagalan pernapasan akut, PPOK, Gangguan Jantung"]
    print("Low ECG, Respiration, SPO2, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotermia, Dehidrasi, Alergi, Masalah Kardiovaskular, Efek samping obat-obatan"]
    print("Low ECG, Respiration, NIBP, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Syok, Gagal jantung, Dehidrasi, Sepsis, Efek samping obat"]
    print("Low ECG, Respiration, NIBP, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Syok kardiogenik, Emboli paru, Infeksi organ"]
    print("Low ECG, Respiration, NIBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Syok, Sepsis, Hipotermia, Gangguan jantung"]
    print("Low ECG, Respiration, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Gagal jantung akut, Infeksi gangguan pernapasan, gangguan jantung"]
    print("Low ECG, Respiration, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Syok Hipovolemik, Syok septik, anafilaksis, "]
    print("Low ECG, Respiration, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Gagal jantung kongestif, syok, gangguan kardiovaskular, hipotermia"]
    print("Low ECG, SPO2, NIBP, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Krisis Syok, Hipoksia, Gangguan pernapasan, Gangguan jantung, Hipotensi"]
    print("Low ECG, SPO2, NIBP, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Kegagalan pernapasan akut, PPOK, Gangguan Jantung"]
    print("Low ECG, SPO2, NIBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((ibps <= 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotermia, Dehidrasi, Alergi, Masalah Kardiovaskular, Efek samping obat-obatan"]
    print("Low ECG, SPO2, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Syok, Gagal jantung, Dehidrasi, Sepsis, Efek samping obat"]
    print("Low ECG, SPO2, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Syok kardiogenik, Emboli paru, Infeksi organ"]
    print("Low ECG, SPO2, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Gagal jantung akut, Infeksi gangguan pernapasan, gangguan jantung, Hipotermia"]
    print("Low ECG, NIBP, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Syok, Sepsis, Hipotermia, Gangguan jantung"]
    print("Low ECG, NIBP, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Syok Hipovolemik, Syok septik, anafilaksis"]
    print("Low ECG, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Gagal jantung kongestif, syok, gangguan kardiovaskular"]
    print("Low ECG, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Gangguan Kardiovaskular, Hipoksia, Hipotensi krisis, Gangguan pernapasan dan sirkulasi"]
    print("Low Respiration, SPO2, NIBP, Temperature detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotiroidisme, Gangguan sirkulasi, Gangguan pernapasan, Hipotermia"]
    print("Low Respiration, SPO2, NIBP, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Krisis Syok, Hipoksia, Gangguan pernapasan, Gangguan jantung, Hipotensi"]
    print("Low Respiration, SPO2, NIBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Kegagalan pernapasan akut, PPOK, Gangguan Jantung"]
    print("Low Respiration, SPO2, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Gangguan pernapasan akut, Hipotermia, Gangguan sirkulasi, Syok"]
    print("Low Respiration, SPO2, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Gangguan Pernapasan, Hipotensi, Gangguan sirkulasi"]
    print("Low Respiration, SPO2, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Hipotiroidisme, Gangguan sirkulasi, Gangguan pernapasan, Hipotermia"]
    print("Low Respiration, NIBP, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Krisis Syok, Hipoksia, Gangguan pernapasan, Gangguan jantung, Hipotensi"]
    print("Low Respiration, NIBP, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Kegagalan pernapasan akut, PPOK, Gangguan Jantung"]
    print("Low Respiration, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Gangguan pernapasan akut, Hipotermia, Gangguan sirkulasi, Syok"]
    print("Low Respiration, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
#Jaki selesai disini
#Ann mulai dari sini
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Shock, Infeksi Berat, Dehidrasi, Gangguan Jantung, Efek Samping Obat"]
    print("Low SPO2, Temperature, NIBP, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Emboli Paru, Bronkitis Berat, Gangguan Pernapasan, Gagal Jantung, Pneumonia, Penyakit Paru Obstruktif Kronis (PPOK), Asma, Gangguan Tidur (Sleep Apnea), Shock, Dehidrasi Parah, Pendarahan Internal, Hipotermia, Hiperventilasi"]
    print("Low SPO2, Temperature, NIBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Gangguan Pernapasan, Hipovolemia, Hipotensi"]
    print("Low SPO2, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((  90 <= nibps <= 120) or (  60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["PPOK, Gagal Jantung, Emboli Paru, Pneumonia Berat, Hipotermia, Dehidrasi, Pendarahan, Sepsis, Reaksi Alergi yang Parah, Hipoventilasi, Gangguan Pemompaan Jantung"]
    print("Low SPO2, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((  nibps < 90) or (  nibpd < 60)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Hipotermia, Gangguan Pernapasan, Sepsis"]
    print("Low Temperature, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((  nibps > 120) or ( nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Demam Tinggi, Infeksi Paru-Paru, Sepsis, Gagal Jantung, Aritmia, Serangan Jantung, Hipertermia"]
    print("High ECG, Respiration, SPO2, Temperature, NIBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((  nibps > 120) or ( nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Krisis Hipertensi, Sindrom Takotsubo, Gagal Jantung Kongestif, Emboli Paru-Paru, Diseksi Aorta"]
    print("High ECG, Respiration, SPO2, NIBP, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((  nibps > 120) or ( nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Gangguan Kardiak, Asma, Pneumonia, PPOK, Sepsis, Katoasidosis Diabetik, Keracunan Monoksida, Gangguan Kecemasan atau Stres"]
    print("High ECG, Respiration, SPO2, NIBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Sepsis, Pneumonia, Emboli Paru, Gagal Napas, Hipertensi Krisis, Infeksi Sistemik Berat"]
    print("High ECG, Respiration, SPO2, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Demam Tinggi, Pneumonia, Emboli Paru, Asidosis Respiratorik, Gagal Jantung, Serangan Jantung, Aritmia Jantung"]
    print("High ECG, Respiration, SPO2, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Gagal Jantung, Pneumonia, Edema Paru-Paru, Emboli Paru, Sepsis, Ketoasidosis Diabetik, Asidosis Laktat"]
    print("High ECG, Respiration, SPO2, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((  nibps > 120) or ( nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi, Gagal Jantung, Aritmia, Penyakit Arteri Koroner, Penyakit Katup Jantung, Sepsis, Asma Berat, Pneumonia, Peradangan, Penyakit Autoimun"]
    print("High ECG, Respiration, Temperature, NIBP, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((  nibps > 120) or ( nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Hipertiroidisme, Sepsis, Tirotoksikosis, PPOK, Keracunan Panas, Gagal Jantung Kongestif, Aritmia Jantung"]
    print("High ECG, Respiration, Temperature, NIBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((  nibps > 120) or ( nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Gagal Jantung, Penyakit Arteri Koroner, Aritmia Jantung, Pneumonia Berat, PPOK, Emboli Paru, Tumor Otak, Pendarahan Otak, Edema Otak, Ketoasidosis Diabetik, Gagal Ginjal"]
    print("High ECG, Respiration, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Sepsis, Keracunan Panas, Ketoasidosis Diabetik, Gangguan Elektrolit, Gagal Jantung, Pneumonia Bakteri"]
    print("High ECG, Respiration, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Infark Miokard, Hipertensi, Penyakit Paru-Paru, Demam, Sepsis"]
    print("High ECG, SPO2, NIBP, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Sepsis, Hipertiroidisme, Asma Parah, Bronkitis Kronis, PPOK, Hipertensi, Aritmia, Gagal Jantung"]
    print("High ECG, SPO2, NIBP, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Penyakit Arteri Koroner, Gagal Jantung, Aritmia, Hipertensi Krisis, Hipoksia, Hipoventilasi, Hiperkapnia, PPOK, Hipertiroidisme, Overdosis Obat"]
    print("High ECG, SPO2, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Gagal Jantung, PPOK, Sepsis, Hipertiroidisme, Efek Samping Obat"]
    print("High ECG, SPO2, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Sepsis, Hipertiroidisme, Serangan Jantung, Hipertermia Maligna, Keracunan Obat"]
    print("High ECG, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Hipertensi Krisis, Pneumonia, PPOK, Asma, Gagal Napas, Penyakit Kardiovaskular, Hipertiroidisme"]
    print("High Respiration, SPO2, NIBP, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Demam Tinggi, Infeksi Saluran Pernapasan, Pneumonia, Sepsis, Hipertiroidisme, Overdosis Obat, Asma"]
    print("High Respiration, SPO2, NIBP, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Gagal Jantung, Pneumonia Berat, Emboli Paru, Hipertiroidisme Berat, Sepsis"]
    print("High Respiration, SPO2, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Sepsis, Gagal Jantung Kongestif, Asma, PPOK, Pneumonia Berat, Sindrom Distress Pernapasan Akut"]
    print("High Respiration, SPO2, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["PPOK, Edema Paru, Hipertensi (Penyakit Jantung, Stroke, Gagal Ginjal), Demam (Infeksi Saluran Napas Atas, Infeksi Saluran Kemih)"]
    print("High Respiration, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Kegagalan Multiorgan (Gagal Jantung, Gagal Paru-Paru, Gagal Ginjal, Sepsis), Pneumonia Berat, Asma Akut, Hipertiroidisme, Overdosis Obat"]
    print("High SPO2, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((  nibps < 90) or (  nibpd < 60)) and
        temperature < 36.3 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        35 <= etco2 <= 45):
    conditions = ["Gangguan Sirkulasi, Gangguan Pernapasan, Hipotermia, Gangguan Jantung"]
    print("Low ECG, Respiration, SPO2, Temperature, NIBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((  nibps < 90) or (  nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or ( ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Shock, Gagal Jantung, Pneumonia, Hipovolemia, Dehidrasi, Infark Miokard"]
    print("Low ECG, Respiration, SPO2, NIBP, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((  nibps < 90) or (  nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Gagal Napas, Pneumonia, Hipokalemia, Hipomagnesium, Keracunan, Gangguan Neurologis"]
    print("Low ECG, Respiration, SPO2, NIBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.3 and
        ((ibps < 90) or ( ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Shock Kardiogenik, Gagal Jantung, Shock Septik, Hipotermia, Pendarahan Internal"]
    print("Low ECG, Respiration, SPO2, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.3 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Serangan Jantung, Gangguan Irama Jantung, Masalah Sirkulasi Darah, Hiperventilasi, PPOK, Emboli Paru, Hipotermia"]
    print("Low ECG, Respiration, SPO2, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or ( ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Gangguan Pernapasan, Hipovolemia, Gangguan Elektrolit (Hipokalemia, Hipokalsemia)"]
    print("Low ECG, Respiration, SPO2, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (  nibpd < 60)) and
        temperature < 36.3 and
        ((ibps < 90) or ( ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Shock, Jantung Koroner, Penyakit Katup Jantung, Hipertensi, Hipovolemia, Hipotermia, Sepsis"]
    print("Low ECG, Respiration, Temperature, NIBP, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.3 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Shock, Tiroid, Diabetes, Gagal Jantung, Pneumotoraks, SIDS, Intoksikasi/Overdosis Obat"]
    print("Low ECG, Respiration, Temperature, NIBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or ( ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Gangguan Pernapasan, Hipovolemia, Gangguan Elektrolit (Hipokalemia, Hipokalsemia), Kegagalan Multiorgan(Gagal Ginjal, Gangguan Hati, Disfungsi Paru-Paru)"]
    print("Low ECG, Respiration, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.3 and
        ((ibps < 90) or ( ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Gangguan Pernapasan, Hipotermia, Penurunan Aliran Darah ke Organ Vital"]
    print("Low ECG, Respiration, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.3 and
        ((ibps < 90) or ( ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Shock Kardiogenik, Shock Septik, Pendarahan Hebat, Gagal Jantung, Hipotermia, Gangguan Peredaran Darah (Penyakit Arteri Perifer, Penyumbatan Arteri Koroner)"]
    print("Low ECG, SPO2, NIBP, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.3 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Gangguan Pernapasan, Hipotermia"]
    print("Low ECG, SPO2, NIBP, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or ( ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock Kardiogenik, Gagal Jantung, Gangguan Pernapasan, Hipovolemia, Infeksi Berat"]
    print("Low ECG, SPO2, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.3 and
        ((ibps < 90) or ( ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Hipotermia, Gagal Jantung, Penyakit Paru-Paru, Infeksi Sistemik (Sepsis)"]
    print("Low ECG, SPO2, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.3 and
        ((ibps < 90) or ( ibpd < 60)) and
        etco2 < 35):
    conditions = ["Hipovolemia, Shock, Gagal Jantung, Hipotermia, Gangguan Pernapasan"]
    print("Low ECG, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.3 and
        ((ibps < 90) or ( ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Shock, Gagal Jantung, Infeksi Sistemik Berat, Pneumonia Parah, Hipotermia, Overdosis Obat"]
    print("Low Respiration, SPO2, NIBP, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.3 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Pneumonia, Gangguan Pernapasan Obstruktif (PPOK atau Asma), Hipotermia, Shock, Kegagalan Fungsi Organ"]
    print("Low Respiration, SPO2, NIBP, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or ( ibpd < 60)) and
        etco2 < 35):
    conditions = ["Gangguan Pernapasan, Gagal Jantung, Hipovolemia, Shock, Emboli Paru, Gangguan Neurologis, Overdosis Obat"]
    print("Low Respiration, SPO2, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.3 and
        ((ibps < 90) or ( ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Hipotermia, Gagal Pernapasan, Gagal Jantung, Emboli Paru"]
    print("Low Respiration, SPO2, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.3 and
        ((ibps < 90) or ( ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Gangguan Pernapasan, Hipotermia, Penyakit Jantung, Gangguan Sirkulasi"]
    print("Low Respiration, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.3 and
        ((ibps < 90) or ( ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Hipotermia, Gagal Jantung, Gangguan Pernapasan, H1ipovolemia"]
    print("Low SPO2, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
#high
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        35 <= etco2 <= 45):
    conditions = ["Krisis Hipertensi/Gagal Jantung Akut"]
    print("High ECG, Respiration, SPO2, NIBP, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 > 45):
    conditions = ["Penyakit Jantung Koroner, Gagal Jantung, Aritmia Jantung, Pneumonia, Emboli Paru-Paru, Asma, Gagal Napas, Hipoksia, Hipertensi, Stroke, Demam Tinggi (Infeksi Saluran Kemih, Infeksi Sistemik, Penyakit Autoimun), Gangguan Metabolisme (Asidosis Respiratorik, Gangguan Renal, atau Penyakit Hati)"]
    print("High ECG, Respiration, SPO2, NIBP, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        36.6 <= temperature <= 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Hipertensi Darurat, Asma, Bronkitis, Infeksi Paru-Paru, Gagal Jantung, Penyakit Jantung Koroner, Aritmia Jantung, Ketoasidosis Diabetik, Asidosis Respiratorik"]
    print("High ECG, Respiration, SPO2, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Sepsis, Ketoasidosis Diabetik, Asidosis Laktat, Tirotoksikosis, Stres Akut, Intoksikasi Obat"]
    print("High ECG, Respiration, SPO2, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        respiration > 16 and
        95 <= spo2 <= 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Hipertensi Darurat, Gagal Jantung, Aritmia, Penyakit Arteri Koroner, Emboli Paru, Sepsis, Asma Berat, Edema Paru, Demam Tinggi"]
    print("High ECG, Respiration, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg > 99 and
        12 <= respiration <= 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Hipertensi, Infeksi Saluran Kemih, Infeksi Paru-Paru, Peradangan Organ Tertentu, Hipoventilasi, Hiperventilasi, Gangguan Neuromuskular, Efek Samping Obat, Peningkatan Detak Jantung"]
    print("High ECG, SPO2, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration > 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["PPOK, Asma Parah, Gagal Napas Akut, Gagal Jantung, Penyakit Arteri Koroner, Gagal Ginjal, Sepsis, Infeksi Saluran Kemih yang Parah"]
    print("High Respiration, SPO2, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
#low
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        35 <= etco2 <= 45):
    conditions = ["Shock Kardiogenik, Gagal Jantung, Hipovolemia, Hipotermia, Sepsis"]
    print("Low ECG, Respiration, SPO2, NIBP, Temperature, IBP detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((90 <= ibps <= 120) or (60 <= ibpd <= 80)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Hipotermia, Keracunan Obat Atau Alkohol, Sepsis"]
    print("Low ECG, Respiration, SPO2, NIBP, Temperature, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        36.6 <= temperature <= 37.2 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Pneumonia, Emboli Paru, PPOK, Hipovolemia, Aritmia Jantung, Serangan Jantung, Gagal Katup Jantung"]
    print("Low ECG, Respiration, SPO2, NIBP, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((90 <= nibps <= 120) or (60 <= nibpd <= 80)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Pneumonia, PPOK, Gagal Napas, Hipotermia, Efek Samping Obat, Overdosis"]
    print("Low ECG, Respiration, SPO2, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        95 <= spo2 <= 100 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Hipotermia, Keracunan Obat, Overdosis, Asma Parah, Gagal Napas, Gangguan Pernapasan Obstruktif Kronis (COPD)"]
    print("Low ECG, Respiration, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        12 <= respiration <= 16 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock (Kardiogenik, Distributif, Hipovolemik), Hipotermia, Gangguan Pernapasan Obstruktif/Gangguan Pernapasan Sentral"]
    print("Low ECG, SPO2, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  60 <= ecg <= 99 and
        respiration < 12 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Hipotermia, Hipovolemia, Gagal Napas, Asma Akut, Gangguan Pernapasan Akut Lainnya"]
    print("Low Respiration, SPO2, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
#high and low 2 con
elif (  ecg > 99 and
        respiration > 16 and
        spo2 > 100 and
        ((nibps > 120) or (nibpd > 80)) and
        temperature > 37.2 and
        ((ibps > 120) or (ibpd > 80)) and
        etco2 > 45):
    conditions = ["Gagal Jantung, Infeksi Paru-Paru Parah, Sepsis, Hipertensi Darurat, Hipertiroidisme"]
    print("High ECG, Respiration, SPO2, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
elif (  ecg < 60 and
        respiration < 12 and
        spo2 < 95 and
        ((nibps < 90) or (nibpd < 60)) and
        temperature < 36.6 and
        ((ibps < 90) or (ibpd < 60)) and
        etco2 < 35):
    conditions = ["Shock, Gagal Jantung, Gangguan Pernapasan, Hipotermia, Infeksi Berat"]
    print("Low ECG, Respiration, SPO2, NIBP, Temperature, IBP, ETCO2 detected! Probabilities for possible conditions:")
    print(conditions)
else:
    print("Either there is something wrong with the number you gave me\n or my developer haven't added knowledge for\n an advanced combination")