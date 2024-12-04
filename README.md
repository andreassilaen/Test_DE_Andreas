# Test_DE_Andreas

## 1. Setup Data di Database Lokal PostgreSQL

Pertama siapkan data ke database lokal PostgreSQL dengan data yang diinginkan.


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
