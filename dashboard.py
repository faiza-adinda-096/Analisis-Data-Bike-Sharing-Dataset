import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("all_data.csv")

data = load_data()

# Sidebar

st.sidebar.image("pngtree-bicycle-logo-in-trendy-design-style-png-image_4861446.png")
st.sidebar.header("Filter Data")
season_filter = st.sidebar.selectbox("Pilih Musim:", ["All"] + list(data["season"].unique()))

# Filter berdasarkan musim
if season_filter != "All":
    data = data[data["season"] == season_filter]

# Header
st.title("Dashboard Analisis Penyewaan Sepeda :bike:")
st.write("Analisis dan Visualisasi Data Penyewaan Sepeda Berdasarkan Beberapa Faktor ")

#Visualisasi Penyewaan Sepeda Berdasarkan Hari
st.subheader("Rata-rata Penyewaan Sepeda per Hari")
data["workingday_label"] = data["workingday"].map({0: "Akhir Pekan", 1: "Hari Kerja"})
fig, ax = plt.subplots()
colors = ["#F8F7DD", "#D4CAA3"]
sns.barplot(x=data["workingday_label"], y=data["cnt"], palette=colors, estimator=sum, ax=ax)
ax.set_xlabel("Hari")
ax.set_ylabel("Total Penyewaan")

st.pyplot(fig)

# Visualisasi Penyewaan Sepeda per Musim
st.subheader("Rata-rata Penyewaan Sepeda per Musim")
fig, ax = plt.subplots()
season_colors = ["#F8F7DD", "#F8F7DD", "#D4CAA3", "#F8F7DD"]
sns.barplot(x=data["season"], y=data["cnt"], palette=season_colors, estimator='sum', ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Penyewaan")
st.pyplot(fig)

# Visualisasi Penyewaan Sepeda Berdasarkan Jam
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Jam")
all_data = pd.read_csv("all_data.csv")
fig2, ax2 = plt.subplots()
sns.lineplot(x=all_data["hr"], y=all_data["cnt"], color="#D4CAA3", estimator='sum', ax=ax2)
ax2.set_xlabel("Jam")
ax2.set_ylabel("Total Penyewaan")
st.pyplot(fig2)

st.title("Hasil Analisis")
st.write("Berdasarkan faktor hari terdapat banyak orang yang menyewa sepeda pada hari kerja dibanding hari libur weekend. Berdasarkan faktor musim juga dapat mempengaruhi bisnis penyewaan sepeda, karena dapat dilihat pada gambar visualisasi 2 bahwa orang lebih sering menyewa sepeda pada musim gugur dan pada musim spring orang lebih sedikit menyewa sepeda. Berdasarkan faktor jam yaitu dapat kita ketahui ternyata banyak orang menyewa sepeda pada jam sore, lebih tepatnya pada jam 17.00 atau jam 5 sore.")

st.title("Saran")
st.write("Hasil analisis ini memiliki beberapa rekomendasi kepada bisnis sewa sepeda agar bisnis berjalan dengan baik kedepannya. Dapat dilihat dari gambar visualisasi 1, bahwa sangat banyak orang yang menyewa sepeda pada hari kerja disbanding akhir pekan. Maka dari itu, mungkin pemilik bisnis tersebut dapat memperbanyak sepeda pada saat hari kerja agar tidak ada pelanggan yang kecewa karena tidak dapat menyewa sepeda karena kehabisan sepeda. Begitu juga pada saat musim gugur (dapat dilihat pada gambar visualisasi 2), jam 7-9 pagi, dan 4-6 sore (dapat dilihat pada gambar visualisasi 3) terlihat penyewaan sepeda ramai ")


st.caption('Copyright (c) Faiza Adinda 2025')