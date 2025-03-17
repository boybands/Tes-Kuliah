import streamlit as st
import random

# Data soal
QUESTIONS = [
    {"question": "Berapakah hasil dari 25 × 4 - 30 ÷ 5?", "options": ["100", "96", "92", "90"], "answer": "96"},
    {"question": "Jika sebuah lingkaran memiliki diameter 14 cm, berapakah kelilingnya? (π = 22/7)", "options": ["44 cm", "66 cm", "88 cm", "100 cm"], "answer": "44 cm"},
    {"question": "Berapa hasil dari √144 + 15?", "options": ["21", "25", "27", "33"], "answer": "27"},
    {"question": "Sebuah kendaraan menempuh 240 km dalam waktu 4 jam. Berapakah kecepatan rata-rata kendaraan tersebut?", "options": ["50 km/jam", "60 km/jam", "70 km/jam", "80 km/jam"], "answer": "60 km/jam"},
    {"question": "Berapa hasil dari 7! (faktorial 7)?", "options": ["5040", "4032", "720", "362880"], "answer": "5040"},
    {"question": "Manakah yang merupakan kalimat efektif?", "options": ["Buku itu telah saya baca.", "Saya sudah buku itu baca.", "Saya buku sudah baca itu.", "Baca saya telah buku itu."], "answer": "Buku itu telah saya baca."},
    {"question": "Apa sinonim dari kata 'cermat'?", "options": ["Teliti", "Kasar", "Cepat", "Santai"], "answer": "Teliti"},
    {"question": "Kalimat berikut yang mengandung majas personifikasi adalah?", "options": ["Pohon itu melambaikan tangannya ke arah kami.", "Ia berlari secepat kilat.", "Kita adalah dua sisi mata uang.", "Kebersihan adalah sebagian dari iman."], "answer": "Pohon itu melambaikan tangannya ke arah kami."},
    {"question": "Manakah pasangan kata yang memiliki hubungan analogi?", "options": ["Ayah - Pekerjaan", "Gurih - Rasa", "Mobil - Sepatu", "Hitam - Lemari"], "answer": "Gurih - Rasa"},
    {"question": "Makna kata 'progresif' adalah?", "options": ["Terus menerus maju", "Berlaku mundur", "Netral", "Menyamping"], "answer": "Terus menerus maju"},
    {"question": "What is the correct past tense of the verb 'go'?", "options": ["Goes", "Gone", "Went", "Going"], "answer": "Went"},
    {"question": "Choose the correct sentence:", "options": ["She don't like apples.", "She doesn't like apples.", "She not like apples.", "She isn't like apples."], "answer": "She doesn't like apples."},
    {"question": "What is the opposite of the word 'ancient'?", "options": ["Modern", "Large", "Old", "Ancestors"], "answer": "Modern"},
    {"question": "Complete the sentence: 'He ________ to the park every morning.'", "options": ["go", "goes", "going", "gone"], "answer": "goes"},
    {"question": "Synonym of 'beautiful' is?", "options": ["Ugly", "Pretty", "Rough", "Heavy"], "answer": "Pretty"},
    {"question": "Jika semua burung bisa terbang, dan elang adalah burung, maka?", "options": ["Elang tidak bisa terbang.", "Elang bisa terbang.", "Elang tidak termasuk burung.", "Elang adalah mamalia."], "answer": "Elang bisa terbang."},
    {"question": "Seorang ayah 4 kali lebih tua dari anaknya. Jika usia anaknya 10 tahun, berapakah usia ayahnya?", "options": ["30 tahun", "35 tahun", "40 tahun", "45 tahun"], "answer": "40 tahun"},
    {"question": "Manakah pasangan pola yang logis dalam seri ini: 2, 4, 8, 16, ...?", "options": ["20", "24", "32", "36"], "answer": "32"},
    {"question": "Jika bunga mawar adalah tanaman dan semua tanaman memiliki daun, maka?", "options": ["Mawar tidak memiliki daun.", "Mawar adalah tanaman tanpa daun.", "Mawar memiliki daun.", "Mawar bukan tanaman."], "answer": "Mawar memiliki daun."},
    {"question": "Manakah pernyataan yang benar mengenai segitiga?", "options": ["Jumlah sudutnya 360°", "Jumlah sudutnya 180°", "Memiliki empat sisi", "Hanya memiliki satu sudut siku-siku"], "answer": "Jumlah sudutnya 180°"},
    {"question": "Jika sebuah kotak memiliki panjang 10 cm, lebar 6 cm, dan tinggi 4 cm, berapakah volumenya?", "options": ["200 cm³", "240 cm³", "260 cm³", "300 cm³"], "answer": "240 cm³"},
    {"question": "Dalam sebuah kelas terdapat 30 siswa. Jika 12 siswa adalah perempuan, berapa persen siswa laki-laki di kelas tersebut?", "options": ["60%", "40%", "50%", "80%"], "answer": "60%"},
    {"question": "Sebuah investasi memberikan bunga majemuk sebesar 10% per tahun. Jika modal awal adalah Rp100 juta, berapakah jumlahnya setelah 2 tahun?", "options": ["Rp110 juta", "Rp121 juta", "Rp120 juta", "Rp130 juta"], "answer": "Rp121 juta"},
    {"question": "Jika nilai rata-rata dari lima bilangan adalah 20, dan empat bilangan adalah 15, 25, 20, dan 30, berapakah bilangan kelima?", "options": ["10", "15", "20", "25"], "answer": "10"},
    {"question": "Berapa hasil dari 15% dari 80?", "options": ["10", "12", "15", "18"], "answer": "12"},
    {"question": "Siapakah tokoh yang memproklamasikan kemerdekaan Indonesia?", "options": ["Soekarno dan Hatta", "Soeharto dan Habibie", "Megawati dan SBY", "BJ Habibie dan Anies"], "answer": "Soekarno dan Hatta"},
    {"question": "Hewan nasional Australia adalah?", "options": ["Koala", "Kanguru", "Platipus", "Wombat"], "answer": "Kanguru"},
    {"question": "Siapakah ilmuwan yang mengemukakan teori evolusi?", "options": ["Isaac Newton", "Albert Einstein", "Charles Darwin", "Stephen Hawking"], "answer": "Charles Darwin"},
    {"question": "Bahan utama dalam pembuatan kertas adalah?", "options": ["Plastik", "Kayu", "Besi", "Kapas"], "answer": "Kayu"},
    {"question": "Manakah negara dengan sistem pemerintahan kerajaan?", "options": ["Jepang", "Italia", "Kanada", "Thailand"], "answer": "Thailand"},
    {"question": "Choose the correct word to complete the sentence: 'She ________ a book every night.'", "options": ["reads", "read", "reading", "to read"], "answer": "reads"},
    {"question": "What is the plural form of 'child'?", "options": ["Childes", "Childs", "Children", "Childrens"], "answer": "Children"},
    {"question": "Find the synonym of 'important':", "options": ["Trivial", "Vital", "Useless", "Ordinary"], "answer": "Vital"},
    {"question": "What does the word 'magnificent' mean?", "options": ["Terrible", "Glorious", "Small", "Quick"], "answer": "Glorious"},
    {"question": "The opposite of 'difficult' is?", "options": ["Complicated", "Easy", "Hard", "Tough"], "answer": "Easy"},
    {"question": "Berapa hasil dari 45 + 15 ÷ 3 × 2?", "options": ["35", "55", "75", "65"], "answer": "55"},
    {"question": "Sebuah balok memiliki panjang 8 cm, lebar 6 cm, dan tinggi 10 cm. Berapakah luas permukaan balok tersebut?", "options": ["240 cm²", "360 cm²", "480 cm²", "600 cm²"], "answer": "360 cm²"},
    {"question": "Jika ada 20 apel dibagi rata kepada 5 orang, berapakah jumlah apel yang diterima setiap orang?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Seorang pekerja menyelesaikan 1/4 bagian pekerjaan dalam 2 jam. Berapa waktu yang dibutuhkan untuk menyelesaikan seluruh pekerjaan?", "options": ["6 jam", "8 jam", "10 jam", "12 jam"], "answer": "8 jam"},
    {"question": "Berapa hasil dari 2⁵ - 3²?", "options": ["28", "29", "31", "32"], "answer": "29"},
    {"question": "Manakah kalimat yang menggunakan ejaan yang benar?", "options": ["Dia tetap semangat, walaupun gagal.", "Dia tetap semangat walau pun gagal.", "Dia tetap semangat walau-pun gagal.", "Dia tetap semangat walaupun gagal"], "answer": "Dia tetap semangat, walaupun gagal."},
    {"question": "Antonim dari kata 'optimis' adalah?", "options": ["Pesimis", "Negatif", "Kritis", "Panik"], "answer": "Pesimis"},
    {"question": "Kalimat berikut yang mengandung konotasi positif adalah?", "options": ["Dia orangnya sangat licik.", "Mereka adalah pekerja keras.", "Pengusaha itu sangat serakah.", "Penulis itu selalu lambat menulis."], "answer": "Mereka adalah pekerja keras."},
    {"question": "Kata yang tepat untuk melengkapi kalimat berikut: 'Kota Jakarta adalah salah satu kota yang paling ______ di Indonesia.'", "options": ["megah", "ramai", "indah", "tenang"], "answer": "ramai"},
    {"question": "Manakah kata baku berikut?", "options": ["Fikir", "Aktivitas", "Obat-obatan", "Praktek"], "answer": "Aktivitas"},
    {"question": "What is the superlative form of 'good'?", "options": ["Better", "Good", "Best", "Most Good"], "answer": "Best"},
    {"question": "Choose the correct word to complete the sentence: 'My friends ______ going to the party tomorrow.'", "options": ["are", "is", "was", "will"], "answer": "are"},
    {"question": "What does 'ecology' mean?", "options": ["Study of animals", "Study of environment", "Study of water", "Study of earth"], "answer": "Study of environment"},
    {"question": "What is the synonym of 'fast'?", "options": ["Quick", "Slow", "Bright", "Short"], "answer": "Quick"},
    {"question": "The correct plural of 'tooth' is?", "options": ["Tooths", "Toothes", "Teeth", "Teeths"], "answer": "Teeth"},
    {"question": "Jika semua kucing adalah mamalia, dan semua mamalia bernapas, maka?", "options": ["Kucing tidak bernapas.", "Kucing adalah mamalia yang tidak bernapas.", "Kucing bernapas.", "Kucing bukan mamalia."], "answer": "Kucing bernapas."},
    {"question": "Jika hari ini adalah Senin, hari apakah 4 hari ke depan?", "options": ["Jumat", "Sabtu", "Kamis", "Rabu"], "answer": "Jumat"},
    {"question": "Manakah urutan angka berikut yang merupakan bilangan prima?", "options": ["1, 2, 3, 4", "2, 3, 5, 7", "1, 4, 6, 8", "2, 4, 6, 9"], "answer": "2, 3, 5, 7"},
    {"question": "Jika setiap siswa membawa 2 buku dan ada 25 siswa, berapa total buku yang dibawa?", "options": ["50", "60", "70", "80"], "answer": "50"},
    {"question": "Manakah di antara pernyataan berikut yang salah?", "options": ["Segitiga memiliki tiga sisi.", "Lingkaran memiliki diameter.", "Kubus memiliki sisi datar.", "Persegi panjang memiliki lima sisi."], "answer": "Persegi panjang memiliki lima sisi."},
    {"question": "Berapa hasil dari 25% dari 200?", "options": ["25", "50", "75", "100"], "answer": "50"},
    {"question": "Jika nilai rata-rata 5 siswa adalah 70 dan salah satu siswa memiliki nilai 60, berapakah total nilai keempat siswa lainnya?", "options": ["240", "280", "300", "320"], "answer": "280"},
    {"question": "Jika dua sudut dalam segitiga masing-masing adalah 50° dan 60°, berapakah besar sudut ketiga?", "options": ["60°", "70°", "80°", "90°"], "answer": "70°"},
    {"question": "Sebuah toko memberikan diskon 10% untuk barang seharga Rp500.000. Berapa harga setelah diskon?", "options": ["Rp450.000", "Rp400.000", "Rp350.000", "Rp550.000"], "answer": "Rp450.000"},
    {"question": "Jika sebuah mesin dapat memproduksi 20 barang dalam 5 menit, berapa banyak barang yang dapat diproduksi dalam 15 menit?", "options": ["40", "60", "80", "100"], "answer": "60"},
    {"question": "Berapa hasil dari (8 × 7) + (9 ÷ 3)?", "options": ["57", "58", "59", "60"], "answer": "59"},
    {"question": "Sebuah segitiga memiliki sisi 6 cm, 8 cm, dan 10 cm. Segitiga ini adalah?", "options": ["Siku-siku", "Sama sisi", "Sama kaki", "Sembarang"], "answer": "Siku-siku"},
    {"question": "Dalam sebuah dadu, berapakah peluang untuk mendapatkan angka genap?", "options": ["1/6", "1/3", "1/2", "2/3"], "answer": "1/2"},
    {"question": "Jika x = 3 dan y = 2, berapa hasil dari 2x² + 3y?", "options": ["21", "23", "25", "27"], "answer": "21"},
    {"question": "Jumlah seluruh sudut dalam segi enam adalah?", "options": ["360°", "540°", "720°", "900°"], "answer": "720°"},
    {"question": "Apakah arti dari kata 'dominasi'?", "options": ["Kepemimpinan", "Penguasaan", "Kekuasaan", "Perbedaan"], "answer": "Penguasaan"},
    {"question": "Manakah kata yang termasuk serapan dari bahasa asing?", "options": ["Eksklusif", "Kuat", "Meriah", "Adil"], "answer": "Eksklusif"},
    {"question": "Manakah kalimat yang mengandung metafora?", "options": ["Waktu adalah uang.", "Ia berlari seperti kilat.", "Hujan turun dengan deras.", "Anak itu bermain di taman."], "answer": "Waktu adalah uang."},
    {"question": "Sinonim dari kata 'kontroversi' adalah?", "options": ["Perselisihan", "Ketentuan", "Kesepakatan", "Penghormatan"], "answer": "Perselisihan"},
    {"question": "Manakah di antara berikut yang merupakan antonim dari 'aktual'?", "options": ["Nyata", "Relevan", "Kuno", "Baru"], "answer": "Kuno"},
    {"question": "What is the antonym of the word 'expand'?", "options": ["Enlarge", "Reduce", "Grow", "Broaden"], "answer": "Reduce"},
    {"question": "Choose the correct sentence:", "options": ["He run fast.", "He runs fast.", "He running fast.", "He ran fastly."], "answer": "He runs fast."},
    {"question": "What is the meaning of 'optimistic'?", "options": ["Hopeful", "Sad", "Uncertain", "Terrified"], "answer": "Hopeful"},
    {"question": "The plural of 'mouse' is?", "options": ["Mouses", "Mice", "Mousees", "Mices"], "answer": "Mice"},
    {"question": "Which word is spelled correctly?", "options": ["Accomodate", "Accommadate", "Accommodate", "Acomodate"], "answer": "Accommodate"},
    {"question": "Jika semua anjing menggonggong dan Bobby adalah anjing, maka?", "options": ["Bobby tidak menggonggong.", "Bobby adalah manusia.", "Bobby menggonggong.", "Bobby tidak termasuk hewan."], "answer": "Bobby menggonggong."},
    {"question": "Manakah pasangan yang termasuk hubungan sebab-akibat?", "options": ["Kertas - Pensil", "Hujan - Banjir", "Buku - Meja", "Kaca - Pintu"], "answer": "Hujan - Banjir"},
    {"question": "Berapakah bilangan genap berikutnya setelah 102?", "options": ["103", "104", "105", "106"], "answer": "104"},
    {"question": "Manakah di antara berikut yang bukan merupakan bentuk persegi panjang?", "options": ["Meja", "Pintu", "Jam dinding bulat", "Layar TV"], "answer": "Jam dinding bulat"},
    {"question": "Jika ada 15 apel dan 5 apel dimakan, berapa apel yang tersisa?", "options": ["5", "10", "15", "20"], "answer": "10"},
    {"question": "Berapa hasil dari 12% dari 150?", "options": ["15", "18", "20", "25"], "answer": "18"},
    {"question": "Jika 2x + 5 = 11, maka nilai x adalah?", "options": ["2", "3", "4", "5"], "answer": "3"},
    {"question": "Sebuah persegi memiliki keliling 40 cm. Berapakah panjang sisinya?", "options": ["5 cm", "8 cm", "10 cm", "12 cm"], "answer": "10 cm"},
    {"question": "Jika sebuah tangki air diisi 20 liter per menit, berapa waktu yang dibutuhkan untuk mengisi tangki hingga penuh jika tangki memiliki kapasitas 100 liter?", "options": ["2 menit", "3 menit", "4 menit", "5 menit"], "answer": "5 menit"},
    {"question": "Berapa hasil dari 80 ÷ 5 + 6?", "options": ["18", "20", "22", "24"], "answer": "22"},
    {"question": "Siapa presiden pertama Amerika Serikat?", "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"], "answer": "George Washington"},
    {"question": "Bulan yang memiliki jumlah hari paling sedikit adalah?", "options": ["Januari", "Februari", "Maret", "April"], "answer": "Februari"},
    {"question": "Negara manakah yang terkenal dengan Menara Eiffel?", "options": ["Italia", "Jerman", "Prancis", "Spanyol"], "answer": "Prancis"},
    {"question": "Siapa penulis buku 'Harry Potter'?", "options": ["J.K. Rowling", "J.R.R. Tolkien", "C.S. Lewis", "Suzanne Collins"], "answer": "J.K. Rowling"},
    {"question": "Planet yang dikenal sebagai 'Planet Merah' adalah?", "options": ["Venus", "Mars", "Jupiter", "Saturnus"], "answer": "Mars"},
    {"question": "Berapa hasil dari (12 × 3) - (5²)?", "options": ["4", "6", "8", "10"], "answer": "4"},
    {"question": "Sebuah lingkaran memiliki jari-jari 7 cm. Berapakah luas lingkarannya? (π = 22/7)", "options": ["154 cm²", "144 cm²", "164 cm²", "134 cm²"], "answer": "154 cm²"},
    {"question": "Kalimat berikut yang merupakan contoh kalimat pasif adalah?", "options": ["Dia mencuci mobil di garasi.", "Mobil itu dicuci oleh dia.", "Dia sedang mencuci mobilnya.", "Kami mencuci bersama-sama."], "answer": "Mobil itu dicuci oleh dia."},
    {"question": "Apa makna dari ungkapan 'buah bibir'?", "options": ["Buah untuk dimakan", "Pusat perhatian", "Hal yang tidak penting", "Perkataan yang menyakitkan"], "answer": "Pusat perhatian"},
    {"question": "The past tense of 'write' is?", "options": ["Write", "Writes", "Wrote", "Written"], "answer": "Wrote"},
    {"question": "What is the synonym of 'quick'?", "options": ["Slow", "Fast", "Lazy", "Tough"], "answer": "Fast"},
    {"question": "Jika ada 300 siswa di sekolah, dan 180 di antaranya adalah perempuan, berapa persentase siswa laki-laki?", "options": ["30%", "40%", "50%", "60%"], "answer": "40%"},
    {"question": "Jika 3x + 7 = 16, maka nilai x adalah?", "options": ["2", "3", "4", "5"], "answer": "3"},
    {"question": "Siapakah penulis novel 'Sang Pemimpi'?", "options": ["Andrea Hirata", "Habiburrahman El Shirazy", "Pramoedya Ananta Toer", "Dee Lestari"], "answer": "Andrea Hirata"},
    {"question": "Gunung berapi tertinggi di Indonesia adalah?", "options": ["Gunung Kerinci", "Gunung Semeru", "Gunung Rinjani", "Gunung Merapi"], "answer": "Gunung Kerinci"},
]

# Fungsi login
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    valid_users = {"juliana": "123", "yube": "123"}
    
    if st.button("Login"):
        if username in valid_users and valid_users[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["score"] = 0
            st.session_state["current_question"] = 0
            st.session_state["finished"] = False
            st.session_state["questions"] = random.sample(QUESTIONS, len(QUESTIONS))  # Acak soal
            st.session_state["answers"] = []
            st.rerun()
        else:
            st.error("Username atau password salah")

# Fungsi untuk menjalankan kuis
def quiz():
    st.title("Tes Masuk Kuliah")
    total_questions = len(st.session_state["questions"])
    
    if st.session_state["current_question"] < total_questions:
        q = st.session_state["questions"][st.session_state["current_question"]]
        st.subheader(f"Soal {st.session_state['current_question'] + 1}: {q['question']}")
        answer = st.radio("Pilih jawaban:", q['options'], key=f"q{st.session_state['current_question']}")
        
        if st.button("Submit Jawaban"):
            st.session_state["answers"].append({
                "question": q['question'],
                "user_answer": answer,
                "correct_answer": q['answer'],
                "is_correct": answer == q['answer']
            })
            if answer == q['answer']:
                st.session_state["score"] += 1
            st.session_state["current_question"] += 1
            st.rerun()
    else:
        st.session_state["finished"] = True
        st.rerun()

# Fungsi untuk menampilkan hasil kuis
def result():
    st.title("Hasil Tes")
    score = st.session_state.get("score", 0)
    total_questions = len(st.session_state.get("questions", []))
    st.markdown(f"<h2>Skor Anda: {score}/{total_questions}</h2>", unsafe_allow_html=True)
    
    st.subheader("Koreksi Jawaban")
    for answer in st.session_state["answers"]:
        status = "✅ Benar" if answer["is_correct"] else "❌ Salah"
        st.write(f"- {answer['question']}")
        st.write(f"  Jawaban Anda: {answer['user_answer']} {status}")
        if not answer["is_correct"]:
            st.write(f"  Jawaban Benar: {answer['correct_answer']}")
    
    if st.button("Coba Lagi"):
        st.session_state.clear()  # Reset semua data
        st.rerun()

# Alur program
if "logged_in" not in st.session_state:
    login()
elif not st.session_state.get("finished", False):
    quiz()
else:
    result()
