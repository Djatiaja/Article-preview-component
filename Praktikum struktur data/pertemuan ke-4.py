daftar_mahasiswa = {
    "12213":{"Nama":"farhan" , "Kelas":"B1", "Angkatan":2022},
    "121241":{"Nama":"Agus" , "Kelas":"A1", "Angkatan":2021},
    "122214313":{"Nama":"amba" , "Kelas":"A2", "Angkatan":2023},
    "424231":{"Nama":"biba" , "Kelas":"B1", "Angkatan":2021},
    "342313":{"Nama":"tita" , "Kelas":"A1", "Angkatan":2023},
    "23223":{"Nama":"tutu" , "Kelas":"A2", "Angkatan":2022},
    "524":{"Nama":"ati" , "Kelas":"B2", "Angkatan":2021}
}

def search(Kolom, value , angkatan,list1):
    temp=[]
    for mahasiswa in list1:
        if list1[mahasiswa][Kolom]== value and list1[mahasiswa]["Angkatan"] == angkatan:
            temp.append(mahasiswa)
    return temp

value = search("Kelas", "A2", 2022,daftar_mahasiswa)
for val in value:
    print(val,daftar_mahasiswa[val])
