# Movie Recomendation System

## Project Overview

Film adalah salah satu bentuk hiburan yang sangat populer, dengan ratusan ribu judul tersedia secara global di berbagai platform. Dalam dunia yang semakin dipenuhi informasi, pengguna sering kali merasa kewalahan dalam memilih film yang sesuai dengan preferensi mereka. Sebuah sistem rekomendasi film dapat menjadi solusi untuk membantu pengguna menemukan film yang relevan dan menarik, menghemat waktu, dan meningkatkan pengalaman pengguna secara keseluruhan.

Proyek ini bertujuan untuk membangun sebuah sistem rekomendasi menggunakan dataset MovieLens, salah satu dataset populer yang menyediakan data rating film oleh pengguna. Dataset MovieLens dipilih karena kaya akan informasi, termasuk sekitar 20 juta rating yang diberikan oleh pengguna terhadap berbagai film, serta data metadata seperti genre. Dataset ini mendukung berbagai teknik pemodelan sistem rekomendasi, termasuk collaborative filtering dan content-based filtering. Dengan hanya menggunakan dua tabel utama (rating.csv dan movie.csv), proyek ini akan fokus pada pendekatan sederhana namun efektif dalam menyediakan rekomendasi film.

Pentingnya proyek ini didasarkan pada beberapa alasan:

- **Kebutuhan Pengguna Akan Rekomendasi yang Relevan:** Berdasarkan riset, pengguna cenderung lebih senang saat diberikan pilihan yang relevan tanpa harus mencari secara manual. Rekomendasi yang baik tidak hanya meningkatkan waktu yang dihabiskan pengguna pada platform tetapi juga kepuasan mereka secara keseluruhan.

- **Aplikasi Bisnis:** Di industri hiburan dan media streaming, sistem rekomendasi adalah tulang punggung untuk mempertahankan pengguna dan mengurangi churn rate. Platform seperti Netflix dan Amazon Prime mengandalkan sistem rekomendasi untuk memberikan rekomendasi yang dipersonalisasi, meningkatkan kemungkinan pengguna menonton film yang direkomendasikan, yang pada gilirannya meningkatkan pendapatan perusahaan.

- **Keberagaman Data:** Dengan adanya berbagai genre dan preferensi penonton, dataset MovieLens dengan 20 juta baris ini menyediakan data yang memadai untuk melatih model yang mampu menangkap variasi minat pengguna.

Proyek ini juga merujuk pada penelitian di bidang sistem rekomendasi yang menunjukkan bahwa metode collaborative filtering, terutama matrix factorization, telah berhasil digunakan di berbagai platform skala besar. Selain itu, pendekatan content-based filtering dapat memperkaya hasil rekomendasi dengan mempertimbangkan fitur genre, sehingga rekomendasi tidak hanya berdasarkan kesamaan pengguna, tetapi juga preferensi konten film itu sendiri.
- Referensi [Consumer-side fairness in recommender systems: a systematic survey of methods and evaluation](https://link.springer.com/article/10.1007/s10462-023-10663-5) 

## Business Understanding
Platform streaming film memiliki ribuan hingga jutaan judul film, yang sering kali membuat pengguna merasa kewalahan dalam memilih film yang sesuai dengan preferensi mereka. Tanpa sistem rekomendasi yang tepat, pengguna cenderung menghabiskan waktu yang lama untuk mencari film yang diminati, yang dapat menyebabkan pengalaman pengguna yang kurang memuaskan dan meningkatkan risiko berpindahnya pengguna ke platform lain. Oleh karena itu, penting bagi platform streaming untuk menyediakan sistem rekomendasi yang dapat memprediksi preferensi pengguna dengan akurat berdasarkan pola rating dan minat genre.

### Problem Statements
- **Bagaimana menyediakan rekomendasi film yang relevan dan sesuai dengan minat pengguna?**
Dengan ribuan hingga jutaan pilihan film yang tersedia, pengguna sering kali kesulitan memilih film yang sesuai dengan minat mereka. Jika sistem rekomendasi tidak bisa memberikan pilihan yang relevan, pengguna bisa merasa frustrasi dan akhirnya meninggalkan platform tersebut. 
- **Bagaimana cara memanfaatkan data rating dan metadata film yang tersedia untuk menghasilkan rekomendasi yang akurat?**
Data rating dan metadata film, seperti genre, memberikan informasi yang berharga tentang pola dan preferensi pengguna. Mengoptimalkan penggunaan data ini dalam menghasilkan rekomendasi adalah tantangan utama dalam membangun sistem rekomendasi yang efektif. 

### Goals
- **Membangun sistem rekomendasi film yang mampu menyarankan film-film yang relevan kepada pengguna, baik berdasarkan kesamaan konten maupun kesamaan preferensi dengan pengguna lain.**
Rekomendasi yang relevan adalah kunci untuk menarik perhatian pengguna dan membuat mereka merasa dimengerti oleh sistem. Dengan mampu mengidentifikasi film yang sesuai minat mereka, baik dari sisi kesamaan genre (konten) atau preferensi rating (kesamaan dengan pengguna lain), sistem ini dapat memberikan pengalaman personalisasi yang lebih mendalam.
- **Meningkatkan pengalaman pengguna dalam menemukan film yang menarik, sehingga pengguna lebih mungkin menggunakan platform lebih lama dan puas dengan pilihan yang disarankan.**
Pengalaman pengguna yang baik sangat penting untuk keberhasilan platform streaming atau layanan media. Ketika pengguna merasa direkomendasikan film yang menarik tanpa harus mencarinya sendiri, mereka lebih mungkin merasa nyaman dan kembali ke platform tersebut. Dengan demikian, tujuan ini bukan hanya untuk meningkatkan keterikatan pengguna pada layanan tetapi juga untuk mendorong loyalitas dan retensi pengguna, yang berdampak langsung pada keberlanjutan platform.

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

### Solution statements
- **Content-Based Filtering**
Pendekatan ini menggunakan genre sebagai fitur utama dalam menghitung kesamaan antar film. Dengan metode ini, sistem dapat memberikan rekomendasi berdasarkan film yang serupa dalam hal genre, menggunakan teknik cosine similarity pada data genre yang telah diolah dengan tfidf vectorizer.
- **Collaborative Filtering**
Pendekatan ini menggunakan collaborative filtering menggunakan teknik embdedding dan root mean squared error (rmse) sebagai metrik evaluasi. Sistem ini mengidentifikasi kesamaan antar film berdasarkan pola rating pengguna, sehingga rekomendasi diberikan berdasarkan film-film yang memiliki pola rating serupa dengan film yang telah dinilai tinggi oleh pengguna.
    
    

## Data Understanding
Dataset yang saya gunakan adalah dataset MovieLens yang saya dapatkan dari kaggle.Dalam penelitian saya, saya hanya menggunakan 2 table yaitu rating.csv dan movie.csv
Table rating memiliki kolom userId, movieId, rating, timestamp. Dengan jumlah baris 20000263 (20 juta lebih). Saat melakukan proses data cleaning, tidak ditemukan nilai null atau duplicate dalam table tersebut.
Table movie memiliki kolom movieId, title, dan genre. Dengan jumlah baris 27278. Saat melakukan proses data cleaning, tidak ditemukan nilai null atau duplicate dalam table tersebut.
[MovieLens](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset/data?).

Variabel-variabel pada table rating adalah sebagai berikut:
- userId : Id dari user yang sudah menonton film tertentu.
- movieId : Id dari movie yang sudah ditonton oleh user tertentu.
- rating : rating yang diberikan user pada sebuah movie.
- timestamp: waktu data tersebut dicatat

Variabel-variabel pada table movie adalah sebagai berikut:
- movieId : Id dari movie yang sudah ditonton oleh user tertentu.
- title : judul dari sebuah movie.
- genre: genre dari sebuah movie

## Data Preparation
Setelah melakukan data understanding, sekarang kita masuk ke tahap data preparation. Hal" yang dilakukan di tahap data preparation:
- Merge table rating & movie
- Membuang record yang memiliki value (no genre list) pada kolom genres
- Mengganti pemisah genre "|" dengan "," pada kolom genre

Setelah itu tahap data preparation dilanjutkan pada kasus content based filtering dan collaborative filtering yang tentu saja memiliki proses preparation yang berbeda-beda
- **Content based filtering**
Pada kasus content-based, dikarenakan pemrosesan 20 juta baris terlalu berat, maka kita hanya mengambil sample 30 ribu record yang ada dalam merged_df. Setelah itu kita memisahkan dan menggabungkan genre.Genre awalnya berbentuk string yang dipisahkan oleh koma, seperti "Action,Adventure". Di sini, genre diubah menjadi daftar dengan str.split(','). Daftar genre kemudian digabungkan menjadi satu string per baris dengan spasi sebagai pemisah. Hal ini memungkinkan TF-IDF untuk menganggap genre sebagai “kata-kata” dalam representasi teks
Setelah itu kita menerapkan tfidf vectorizer. Teknik ini mengubah data teks menjadi representasi numerik dengan menghitung bobot Term Frequency-Inverse Document Frequency (TF-IDF), sehingga setiap genre dapat diukur berdasarkan kemunculan relatifnya dibandingkan dengan genre lain di dataset. Hasil dari TF-IDF adalah vektor berbobot yang menunjukkan hubungan antar genre dan digunakan dalam perhitungan kesamaan antar film. Sedangkan disisi lain
- **Collaborative filtering**
Pada kasus collaborative filtering, dikarenakan pemrosesan 20 juta baris terlalu berat, maka kita hanya mengambil sample 1 juta record yang ada dalam merged_df lalu mengacaknya. Hal ini diharapkan untuk mengurangi resiko overfitting pada model.
Untuk kasus collaborative filtering tidak ada teknik data preparation khusus. Dalam kasus ini hanya mendapatkan rating terkecil dan rating terbesar untuk masuk ke pemrosesan splitting data pada data target (rating) dan kolom userId dan movieId sebagai data input. Variabel y berisi rating yang telah dinormalisasi menggunakan skala (x - min_rating) / (max_rating - min_rating). Normalisasi ini berguna agar rating berada dalam rentang antara 0 dan 1, yang memudahkan model dalam proses pembelajaran (terutama untuk model dengan aktivasi sigmoid). Splitting data yang digunakan memiliki ratio 80 training : 20 validation

## Modeling
Sistem rekomendasi yang saya buat dibangun menggunakan dua pendekatan utama: Content-Based Filtering dan Collaborative Filtering.Pada content-based tidak ada algoritma khusus yang digunakan, sedangkan collaborative menggunakan teknik embedding.
**Content-Based Filtering**
Pendekatan content-based filtering memberikan rekomendasi film berdasarkan kesamaan konten, dalam hal ini genre, dengan film yang telah ditonton atau dinilai tinggi oleh pengguna. Setelah teknik tfidf selesai dilakukan, maka selanjutnya kita menerapkan cosine similarity pada matrix tfidf untuk menghitung kemiripan antara setiap film dalam bentuk matriks cosine similarity, dengan nilai antara 0 hingga 1. Matriks ini menunjukkan seberapa mirip setiap film satu sama lain berdasarkan genre.
Matriks ini kemudian dikonversi menjadi DataFrame untuk memudahkan pengindeksan.
Setelah proses tersebut selesai, kita membuat function recommend_movies_by_title untuk mencari rekomendasi film berdasarkan judul film yang diberikan (movie_title). Fungsi ini pertama-tama menemukan indeks film (movie_idx) dalam merged_df_sample yang sesuai dengan movie_title.
Kemudian, skor kesamaan dihitung untuk film tersebut terhadap semua film lainnya dalam cosine_sim_df.
Top film teratas diambil berdasarkan skor kemiripan tertinggi (nlargest(top_n + 1)), melewatkan film itu sendiri (iloc[1:]. Dengan parameter 5 rekomendasi film, berikut adalah outputnya:
Pengujian ditest pada film berjudul jumanji (1995)

**Top 5 recommendation:**

| movieId | title                                             |
|---------|---------------------------------------------------|
| 768     | NeverEnding Story II: The Next Chapter, The (1... |
| 1959    | Indian in the Cupboard, The (1995)                |
| 875     | NeverEnding Story, The (1984)                     |
| 2292    | Chronicles of Narnia: The Lion, the Witch and ... |
| 2545    | Bridge to Terabithia (2007)                       |

**Collaborative filtering**
Pendekatan collaborative filtering memberikan rekomendasi berdasarkan pola kesamaan rating antar film. Teknik ini menggunakan teknik embedding dengan metrik RMSE untuk mengidentifikasi film-film yang memiliki pola rating serupa dengan film yang disukai pengguna. Proses modeling pada kasus collaborative filtering dimulai dengan membuat class recommenderNet yang akan digunakan untuk membangun arsitektur model rekomendasi yang terdiri dari lapisan embedding untuk pengguna dan film. Dalam class tersebut mendefinisikan dua jenis embedding:
Embedding Pengguna (user_embedding): Mewakili setiap pengguna dalam vektor berdimensi embedding_size.
Embedding Film (movie_embedding): Mewakili setiap film dalam vektor berdimensi embedding_size.
embeddings_initializer='he_normal' digunakan untuk menginisialisasi nilai embedding secara acak dengan distribusi normal He.
Regularisasi L2 ditambahkan untuk mencegah overfitting. Selain embedding, setiap pengguna dan film juga diberi lapisan bias (user_bias dan movie_bias) untuk memodelkan kecenderungan peringkat spesifik bagi pengguna atau film. Didalam class tersebut terdapat function call, yang mendefinisikan bagaimana model melakukan prediksi.
inputs[:, 0] adalah ID pengguna, yang digunakan untuk mengambil embedding pengguna (user_vector) dan bias pengguna (user_bias).
inputs[:, 1] adalah ID film, yang digunakan untuk mengambil embedding film (movie_vector) dan bias film (movie_bias).
Model menghitung dot product antara user_vector dan movie_vector, yang mengukur kesamaan antara embedding pengguna dan film.
Nilai ini ditambahkan dengan user_bias dan movie_bias untuk mengakomodasi preferensi pengguna dan popularitas film.
Hasil akhirnya adalah prediksi rating yang dinormalisasi ke rentang (0, 1) menggunakan fungsi aktivasi sigmoid 
Pada kasus collaborative filtering, setelah melakukan pelatihan dengan epoch 5, batch size 64, dan learning rate 0.001, menggunakan optimizer adam dan function loss BinaryCrossentropy menghasilkan hasil yang cukup baik dengan RMSE di angka **0.2730**
Berikut adalah output dari collaborative filtering
Showing recommendations for user: 126797

**Movies with high ratings from user**
| movieId | title                                                     |
|---------|-----------------------------------------------------------|
| 319     | Shallow Grave (1994)                                      |
| 41      | Richard III (1995)                                        |
| 4993    | Lord of the Rings: The Fellowship of the Ring, The (2001) |
| 5008    | Witness for the Prosecution (1957)                        |
| 5225    | And Your Mother Too (Y tu mamá también) (2001)            |

**Top 10 movie recommendations**
| movieId | Title                                         |
|---------|-----------------------------------------------|
| 912     | Casablanca (1942)                             |
| 50      | Usual Suspects, The (1995)                    |
| 1203    | 12 Angry Men (1957)                           |
| 904     | Rear Window (1954)                            |
| 1221    | Godfather: Part II, The (1974)                |
| 7502    | Band of Brothers (2001)                       |
| 5618    | Spirited Away (Sen to Chihiro no kamikakushi) (2001) |
| 3429    | Creature Comforts (1989)                      |
| 6016    | City of God (Cidade de Deus) (2002)           |
| 1945    | On the Waterfront (1954)                      |



## Evaluation
Pada projek ini metrik evaluasi yang digunakan adalah cosine similarity untuk content based filtering dan RMSE untuk collaborative filtering.
Pada kasus content based filtering, hasil yang didapatkan adalah 
| Title                                                        | Cosine Similarity |
|--------------------------------------------------------------|--------------------|
| NeverEnding Story II: The Next Chapter, The (1990)           | 1.0               |
| NeverEnding Story, The (1984)                                | 1.0               |
| Indian in the Cupboard, The (1995)                           | 1.0               |
| Chronicles of Narnia: The Lion, the Witch and Wardrobe (2005)| 1.0               |
| Bridge to Terabithia (2007)                                  | 1.0               |


Bisa dilihat hasil dari cosine similarity pada top recomendation menghasilkan output 1.0. Hal ini dikarenakan film-film yang direkomendasikan juga dari genre yang sama persis dengan film jumanji 1995.
Pada kasus collaborative filtering, setelah melakukan pelatihan dengan epoch 5, batch size 64, dan learning rate 0.001, menggunakan optimizer adam dan function loss BinaryCrossentropy menghasilkan hasil yang cukup baik dengan RMSE di angka **0.2730**
Namun teknik collaborative filtering memiliki keunggulan daripada content based yaitu:
- **Mengenali Pola Preferensi yang Kompleks**: Collaborative Filtering mampu mengenali pola preferensi dari perilaku pengguna lainnya. Dalam contoh rekomendasi di atas, item yang sering diberi rating tinggi oleh pengguna yang memiliki preferensi serupa dihitung kesamaannya berdasarkan skor korelasi. Metode ini memungkinkan sistem untuk menangkap kesamaan preferensi yang kompleks antar pengguna yang mungkin tidak dapat ditangkap dengan data genre atau atribut film lain yang terbatas.

- **Lebih Personal dan Dinamis**: Karena metode ini menganalisis pola rating pengguna untuk mengidentifikasi item yang serupa, sistem akan merekomendasikan film yang kemungkinan besar disukai pengguna berdasarkan kecenderungan pengguna dengan pola rating yang sama. Pendekatan ini lebih responsif terhadap perubahan perilaku pengguna karena bergantung pada data rating yang terus berkembang.

- **Mengatasi Keterbatasan Metadata**: Content-Based Filtering biasanya terbatas pada atribut konten yang ada (seperti genre atau deskripsi), yang seringkali tidak mencakup banyak aspek penting dari pengalaman menonton. Sementara, Collaborative Filtering hanya membutuhkan data rating sehingga dapat bekerja dengan baik bahkan ketika informasi genre atau detail film tidak terlalu spesifik.
