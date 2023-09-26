import streamlit as st
from babel.numbers import format_currency

def format_rupiah(angka):
    return format_currency(angka, 'IDR', locale='id_ID','rb')

def tronton():
    st.title("PROGRAM PARKIR PANEL Tronton")
    st.write("-" * 40)
    mbl = st.number_input("Masukan Jumlah Mobil:", min_value=0, step=1)
    orang = st.number_input("Masukan Jumlah Orang:", min_value=0, step=1)
    ppn = 35000 * mbl
    kas = 10000 * mbl
    masuk = 90000 * mbl

    if orang != 0:
        proses = (masuk - kas - ppn) / orang

        st.write('\n')
        st.markdown("<style>div.stButton > button:first-child {background-color: green;}</style>", unsafe_allow_html=True)
        st.markdown(f'<div style="background-color: #C8F7C5; padding: 10px; border-radius: 5px; color: black;"><b>Jatah Satpam:</b> {format_rupiah(ppn)}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="background-color: #C8F7C5; padding: 10px; border-radius: 5px; color: black;"><b>Kas Mushola:</b> {format_rupiah(kas)}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="background-color: #C8F7C5; padding: 10px; border-radius: 5px; color: black;"><b>Jatah Per orang:</b> {format_rupiah(proses)}</div>', unsafe_allow_html=True)
    else:
        st.warning("Jumlah orang tidak boleh 0. Silakan masukkan jumlah orang yang valid.")

def engkel():
    st.title("PROGRAM PARKIR PANEL Engkel")
    st.write("-" * 40)
    mbl = st.number_input("Masukan Jumlah Mobil:", min_value=0, step=1)
    orang = st.number_input("Masukan Jumlah Orang:", min_value=0, step=1)
    ppn = 25000 * mbl
    kas = 10000 * mbl
    masuk = 60000 * mbl

    if orang != 0:
        proses = (masuk - kas - ppn) / orang

        st.write('\n')
        st.markdown("<style>div.stButton > button:first-child {background-color: green;}</style>", unsafe_allow_html=True)
        st.markdown(f'<div style="background-color: #C8F7C5; padding: 10px; border-radius: 5px; color: black;"><b>Jatah Satpam:</b> {format_rupiah(ppn)}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="background-color: #C8F7C5; padding: 10px; border-radius: 5px; color: black;"><b>Kas Mushola:</b> {format_rupiah(kas)}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="background-color: #C8F7C5; padding: 10px; border-radius: 5px; color: black;"><b>Jatah Per orang:</b> {format_rupiah(proses)}</div>', unsafe_allow_html=True)
    else:
        st.warning("Jumlah orang tidak boleh 0. Silakan masukkan jumlah orang yang valid.")

def gabungan():
    st.title("PROGRAM PARKIR PANEL Gabungan")
    st.write("-" * 40)
    mbl_tronton = st.number_input("Masukan Jumlah Mobil Tronton:", min_value=0, step=1)
    mbl_engkel = st.number_input("Masukan Jumlah Mobil Engkel:", min_value=0, step=1)
    mbl_colt = st.number_input("Masukan Jumlah Mobil Coldesel:",min_value=0, step=1)
    orang = st.number_input("Masukan Jumlah Orang:", min_value=0, step=1)

    ppn_tronton = 35000 * mbl_tronton
    kas_tronton = 10000 * mbl_tronton
    masuk_tronton = 90000 * mbl_tronton

    ppn_engkel = 25000 * mbl_engkel
    kas_engkel = 10000 * mbl_engkel
    masuk_engkel = 60000 * mbl_engkel
    
    ppn_colt = 20000 * mbl_colt
    kas_colt = 10000 * mbl_colt
    masuk_colt = 50000 * mbl_colt

    if orang != 0:
        proses_tronton = (masuk_tronton - kas_tronton - ppn_tronton)
        proses_engkel = (masuk_engkel - kas_engkel - ppn_engkel)
        proses_colt = (masuk_colt - kas_colt - ppn_colt)
        ppn_total = ppn_tronton + ppn_engkel + ppn_colt
        kas_total = kas_tronton + kas_engkel + kas_colt
        proses_total = (proses_tronton + proses_engkel + proses_colt) / orang

        st.write('\n')
        st.markdown("<style>div.stButton > button:first-child {background-color: green;}</style>", unsafe_allow_html=True)
        st.markdown(f'<div style="background-color: #C8F7C5; padding: 10px; border-radius: 5px; color: black;"><b>Jatah Satpam:</b> {format_rupiah(ppn_total)}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="background-color: #C8F7C5; padding: 10px; border-radius: 5px; color: black;"><b>Kas Mushola:</b> {format_rupiah(kas_total)}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="background-color: #C8F7C5; padding: 10px; border-radius: 5px; color: black;"><b>Jatah Per orang:</b> {format_rupiah(proses_total)}</div>', unsafe_allow_html=True)
    else:
        st.warning("Jumlah orang tidak boleh 0. Silakan masukkan jumlah orang yang valid.")

# Main program

st.markdown("<style>body {background-color: #1F2227; color: white;}</style>", unsafe_allow_html=True)
st.title("PROGRAM PARKIR PANEL")
st.write("-" * 35)

menu = ["Tronton", "Engkel", "Gabungan"]
pilih = st.selectbox("Pilih Menu di bawah:", menu)

if pilih == "Tronton":
    tronton()
elif pilih == "Engkel":
    engkel()
elif pilih == "Gabungan":
    gabungan()
