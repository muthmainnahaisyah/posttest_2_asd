# Nama: Muthmainnah Aisyah
# NIM: 2209116001
# Kelas: SI - A

import os
import time
os.system("cls")

Dataset = ["daiva", "zaki", ["wahyu", "zaki"], "shafa", ["zaki", "aji", "wahyu"], "zaki"]
data_kosong1 = []
data_kosong2 = {}

# QUICKSORT

def partition(l, bwh, atas):
    pivot = l[bwh]
    pos_batas = bwh+1
    for k in range(bwh+1, atas):
        if l[k] < pivot:
            l[pos_batas], l[k] = l[k], l[pos_batas]
            pos_batas += 1
    l[pos_batas-1], l[bwh] = l[bwh], l[pos_batas-1]
    return pos_batas

def quicksort(l, bwh, atas):
    if atas <= bwh:
        return
    p = partition(l, bwh, atas)
    quicksort(l, bwh, p-1)
    quicksort(l, p, atas)
    return l

def sorting():
    print("Sebelum diurutkan:\n", Dataset)
    print("="*80)
    for i in range(len(Dataset)):
        if type (Dataset[i]) != str:
            data_kosong2[i] = Dataset[i]
        else:
            data_kosong1.append(Dataset[i])
            quicksort(data_kosong1, 0, len(data_kosong1))
    for j in data_kosong2:
        quicksort(data_kosong2[j], 0, len(data_kosong2[j]))
        data_kosong1.insert(j, data_kosong2[j])
    print("Setelah diurutkan:\n", data_kosong1)
    print("="*80)

# FIBONACCI SEARCH

def fibonacci(a, x, n):
    fibonacci1 = 0
    fibonacci2 = 1
    fibonacci = fibonacci1 + fibonacci2
    while (fibonacci < n):
        fibonacci1 = fibonacci2
        fibonacci2 = fibonacci
        fibonacci = fibonacci1 + fibonacci2
    offset = -1
    while (fibonacci > 1):
        i = min(offset + fibonacci1, n-1)
        if (a[i] < x):
            fibonacci = fibonacci2
            fibonacci2 = fibonacci1
            fibonacci1 = fibonacci - fibonacci2
            offset = i
        elif (a[i] > x):
            fibonacci = fibonacci1
            fibonacci2 = fibonacci2 - fibonacci1
            fibonacci1 = fibonacci - fibonacci2
        else:
            return i
    if (fibonacci2 and a[n-1] == x):
        return n-1
    return -1
    
def search():
    print("\nHasil dari pencarian", x, "=")
    for z in range(len(data_kosong1)):
        if type(data_kosong1[z]) == list:
            isi = fibonacci(Dataset[z], x, len(Dataset[z]))
            time.sleep(1)
            print(x, "berada di array index ke -",z,"kolom",isi)
        else:
            if data_kosong1[z] == x:
                time.sleep(1)
                print(x, "berada di array index ke -",z)

sorting()
x = "zaki"
search()
print("")
