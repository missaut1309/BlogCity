## Blog City
Ứng dụng là hệ thống Blog giúp người dùng có thể chia sẻ thông tin, cảm xúc, hình ảnh, kết bạn

## Cài đặt backend 

```sql
CREATE DATABASE blogcity CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER 'blogcity'@'%' IDENTIFIED BY 'blogcity';
GRANT ALL PRIVILEGES ON blogcity.* TO 'blogcity'@'%';
FLUSH PRIVILEGES;
```

## Database migrations 

```bash
python manage.py makemigrations
python manage.py migrate 
```

## Cài đặt superuser

```bash
python manage.py createsuperuser
```

## Running backend
 
```bash
python manage.py runserver
```

## Truy cập vào hệ thống BlogCity
```bash
http://127.0.0.1:8000/blog/
```
