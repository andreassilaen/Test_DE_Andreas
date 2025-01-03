# Test_DE_Andreas

## 1. Setup Data di Database Lokal PostgreSQL

1. Pertama siapkan data ke database lokal PostgreSQL dengan data yang diinginkan. Butakan tabel terlebih dahulu :
```bash
CREATE TABLE retail_transactions (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    last_status VARCHAR(50),
    pos_origin VARCHAR(100),
    pos_destination VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);
```

2. Isi tabel dengan data dummy:
```bash
INSERT INTO retail_transactions (customer_id, last_status, pos_origin, pos_destination, created_at, updated_at, deleted_at)
VALUES
(1, 'Delivered', 'Jakarta', 'Surabaya', '2024-12-01 08:00:00', '2024-12-01 10:00:00', NULL),
(2, 'In Transit', 'Medan', 'Bandung', '2024-12-02 09:00:00', '2024-12-02 11:30:00', NULL),
(3, 'Pending', 'Bali', 'Yogyakarta', '2024-12-03 10:00:00', '2024-12-03 12:00:00', NULL),
(4, 'Delivered', 'Semarang', 'Jakarta', '2024-12-04 08:00:00', '2024-12-04 10:30:00', NULL),
(5, 'Canceled', 'Surabaya', 'Makassar', '2024-12-05 07:30:00', '2024-12-05 09:00:00', '2024-12-05 09:00:00');
```


## 2. Setup Airflow / docker
1. lanjut ke proses Airflow. file script Dag Airflow dapat dijalankan pada folder yang memiliki docker dan airflow. cara jalankan docker dengan melakukan command  docker-compose down di terminal
```bash
docker-compose down 
```

2. masuk ke dalam ui Airflow dengan url 
```bash 
http://localhost:8080/ 
``` 
dan melakukan login dengan akun airflow default yaitu: 
```bash
username : airflow
password : airflow
```

3. Jika sudah masuk home airflow, carilah Dag dengan judul “extract_load_data_dag”/
Lalu tekan play / aktifkan dag 

4. Maka Dag akan menjalankan task 
```bash 
extract_data >> load_data_toBigquery
```

## 3. Cek BigQuery
 1. Hasil data dapat dilihat dengan cara masuk ke project BigQuery. 

 2. melakukan select query
```bash
SELECT * FROM `sage-outrider-418915.dwh_retail_transactions.raw_retail`
```

------------------------------------

Pastikan Anda berada di folder yang memiliki file `docker-compose.yml`. Jalankan perintah berikut untuk mematikan container yang mungkin sedang berjalan:

```bash
docker-compose down
```
