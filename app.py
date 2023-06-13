import streamlit as st
import math

st.sidebar.title("Hitung Luas dan Volume Bangun")
selected = st.sidebar.selectbox("Pilih bangun yang ingin dihitung:", 
                                ("Hitung Luas Persegi Panjang", "Hitung Luas Segitiga", "Hitung Luas Trapesium", "Hitung Luas Jajar Genjang", "Hitung Luas Kubus", "Hitung Luas Balok", "Hitung Volume Kubus", "Hitung Volume Balok", "Hitung Luas Kerucut", "Hitung Volume Kerucut","Hitung Luas Limas Segitiga", "Hitung Volume Limas Segitiga","Hitung Luas Prisma Segitiga", "Hitung Volume Prisma Segitiga"))

if selected == "Hitung Luas Persegi Panjang":
    st.title("Hitung Luas Persegi Panjang")

    panjang = st.number_input("Masukkan Nilai Panjang", min_value=0.0)
    lebar = st.number_input("Masukkan Nilai Lebar", min_value=0.0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = panjang * lebar
        st.success(f"Luas Persegi Panjang adalah {luas}")

elif selected == "Hitung Luas Segitiga":
    st.title("Hitung Luas Segitiga")

    alas = st.number_input("Masukkan Nilai Alas", min_value=0.0)
    tinggi = st.number_input("Masukkan Nilai Tinggi", min_value=0.0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = 0.5 * alas * tinggi
        st.success(f"Luas Segitiga adalah {luas}")

elif selected == "Hitung Luas Trapesium":
    st.title("Hitung Luas Trapesium")

    sisi_a = st.number_input("Masukkan Nilai sisi atas", min_value=0.0)
    sisi_b = st.number_input("Masukkan Nilai Sisi bawah", min_value=0.0)
    tinggi = st.number_input("Masukkan Nilai Tinggi", min_value=0.0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = 0.5 * (sisi_a + sisi_b) * tinggi
        st.success(f"Luas Trapesium adalah {luas}")

elif selected == "Hitung Luas Jajar Genjang":
    st.title("Hitung Luas Jajar Genjang")

    alas = st.number_input("Masukkan Nilai Alas", min_value=0.0)
    tinggi = st.number_input("Masukkan Nilai Tinggi", min_value=0.0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = alas * tinggi
        st.success(f"Luas Jajar Genjang adalah {luas}")

elif selected == "Hitung Luas Kubus":
    st.title("Hitung Luas Kubus")

    sisi = st.number_input("Masukkan Nilai Sisi", min_value=0.0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = 6 * sisi * sisi
        st.success(f"Luas Kubus adalah {luas}")

elif selected == "Hitung Volume Kubus":
    st.title("Hitung Volume Kubus")

    sisi = st.number_input("Masukkan Nilai Sisi", min_value=0.0)
    hitung = st.button("Hitung Volume")

    if hitung:
        volume = sisi ** 3
        st.success(f"Volume Kubus adalah {volume}")



elif selected == "Hitung Luas Balok":
    st.title("Hitung Luas Balok")

    panjang = st.number_input("Masukkan Nilai Panjang", min_value=0.0)
    lebar = st.number_input("Masukkan Nilai Lebar", min_value=0.0)
    tinggi = st.number_input("Masukkan Nilai Tinggi", min_value=0.0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        st.success(f"Luas Balok adalah {luas}")


elif selected == "Hitung Volume Balok":
    st.title("Hitung Volume Balok")

    panjang = st.number_input("Masukkan Nilai Panjang", min_value=0.0)
    lebar = st.number_input("Masukkan Nilai Lebar", min_value=0.0)
    tinggi = st.number_input("Masukkan Nilai Tinggi", min_value=0.0)
    hitung = st.button("Hitung Volume")

    if hitung:
        volume = panjang * lebar * tinggi
        st.success(f"Volume Balok adalah {volume}")

if selected == "Hitung Luas Kerucut":
    st.title("Hitung Luas Kerucut")

    jari_jari = st.number_input("Masukkan Nilai Jari-jari", min_value=0.0)
    tinggi = st.number_input("Masukkan Nilai Tinggi", min_value=0.0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari**2 + tinggi**2))
        st.success(f"Luas Kerucut adalah {luas}")

elif selected == "Hitung Volume Kerucut":
    st.title("Hitung Volume Kerucut")

    jari_jari = st.number_input("Masukkan Nilai Jari-jari", min_value=0.0)
    tinggi = st.number_input("Masukkan Nilai Tinggi", min_value=0.0)
    hitung = st.button("Hitung Volume")

    if hitung:
        volume = (1/3) * math.pi * jari_jari**2 * tinggi
        st.success(f"Volume Kerucut adalah {volume}")
elif selected == "Hitung Luas Limas Segitiga":
    st.title("Hitung Luas Limas Segitiga")

    sisi_a = st.number_input("Masukkan Nilai Sisi A", min_value=0.0)
    sisi_b = st.number_input("Masukkan Nilai Sisi B", min_value=0.0)
    sisi_c = st.number_input("Masukkan Nilai Sisi C", min_value=0.0)
    tinggi = st.number_input("Masukkan Nilai Tinggi", min_value=0.0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = (0.5 * sisi_a * tinggi) + (0.5 * sisi_b * tinggi) + (0.5 * sisi_c * tinggi)
        st.success(f"Luas Limas Segitiga adalah {luas}")

elif selected == "Hitung Volume Limas Segitiga":
    st.title("Hitung Volume Limas Segitiga")

    sisi_a = st.number_input("Masukkan Nilai Sisi A", min_value=0.0)
    sisi_b = st.number_input("Masukkan Nilai Sisi B", min_value=0.0)
    sisi_c = st.number_input("Masukkan Nilai Sisi C", min_value=0.0)
    tinggi = st.number_input("Masukkan Nilai Tinggi", min_value=0.0)
    hitung = st.button("Hitung Volume")

    if hitung:
        volume = (1/6) * tinggi * math.sqrt((sisi_a**2 * sisi_b**2) + (sisi_b**2 * sisi_c**2) + (sisi_c**2 * sisi_a**2))
        st.success(f"Volume Limas Segitiga adalah {volume}")

elif selected == "Hitung Luas Prisma Segitiga":
    st.title("Hitung Luas Prisma Segitiga")

    alas = st.number_input("Masukkan Nilai Alas Segitiga", min_value=0.0)
    tinggi_segitiga = st.number_input("Masukkan Nilai Tinggi Segitiga", min_value=0.0)
    tinggi_prisma = st.number_input("Masukkan Nilai Tinggi Prisma", min_value=0.0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas_segitiga = (0.5 * alas * tinggi_segitiga)
        luas_prisma = 2 * luas_segitiga + (alas * tinggi_prisma)
        st.success(f"Luas Prisma Segitiga adalah {luas_prisma}")

elif selected == "Hitung Volume Prisma Segitiga":
    st.title("Hitung Volume Prisma Segitiga")

    alas = st.number_input("Masukkan Nilai Alas Segitiga", min_value=0.0)
    tinggi_segitiga = st.number_input("Masukkan Nilai Tinggi Segitiga", min_value=0.0)
    tinggi_prisma = st.number_input("Masukkan Nilai Tinggi Prisma", min_value=0.0)
    hitung = st.button("Hitung Volume")

    if hitung:
        luas_segitiga = (0.5 * alas * tinggi_segitiga)
        volume_prisma = luas_segitiga * tinggi_prisma
        st.success(f"Volume Prisma Segitiga adalah {volume_prisma}")