# Blog City
Ứng dụng là hệ thống Blog giúp người dùng có thể chia sẻ thông tin, cảm xúc, hình ảnh, kết bạn

# Cài đặt backend 

CREATE DATABASE blogcity CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER 'blogcity'@'%' IDENTIFIED BY 'blogcity';
GRANT ALL PRIVILEGES ON blogcity.* TO 'blogcity'@'%';
FLUSH PRIVILEGES;

#  database migrations 

python makemigrations
python migrate 

# cài đặt superuser

python manage.py createsuperuser

# running backend
 
python manage.py runserver

# truy cập vào hệ thông blog

http://127.0.0.1:8000/blog/
