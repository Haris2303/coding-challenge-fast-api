# Penjelasan API

API ini adalah Restful api sederhana untuk mengelola data users menggunakan FastAPI dan FireBase Firestore sebagai database. API ini menyediakan fitur CRUD untuk data users. API ini digunakan sebagai jembatan untuk penghubung antara backend dan frontend

# Endpoint
- Metode POST `/users` yaitu endpoint untuk menambahkan data user.
- Metode GET `/users` yaitu endpoint untuk mendapatkan semua data users
- Metode GET `/users/{user_id}` yaitu endpoint untuk mendapatkan data user berdasarkan id user
- Metode PUT `/users/{user_id}` yaitu endpoint untuk mengubah data user berdasarkan id user
- Metode DELETE `/users/{user_id` yaitu endpoint untuk menghapus data user berdasarkan id user

# Request yang diberikan
```json
{
    "name": "Andri",
    "email": "andri@gmail.com",
    "age": 25
}
```
