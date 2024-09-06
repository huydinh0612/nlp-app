
## Giới thiệu đồ án
- Demo : D13 - Xây dựng API tóm tắt tóm lược đơn văn bản.
- Giảng viên hướng dẫn :
    - PGS TS. Đinh Điền
    - TS. Nguyễn Hồng Bửu Long
    - TS. Lương An Vinh
- Học viên thực hiện:
    - Đặng Nhì - 23C01035
    - Đinh Gia Huy - 23C01005

## Hướng dẫn cài đặt môi trường

### Môi trường
- Python 3.10.11
- Docker 
### Cài đặt 


1. Clone nội dung code từ github 

```
git clone https://github.com/huydinh0612/nlp-app.git
git checkout DangNhi
```
2. Di chuyển vào thư mục nlp-app
```
cd nlp-app
```
3. Tạo Docker Image 

```
docker build -t nlp_image:prod .
```

## Hướng dẫn sử dụng

1. Chạy docker image vừa được tạo để khởi chạy ứng dụng Demo
- Ứng dụng được đóng gói thành container nlp_app
```
docker container run -it -p 8080:8080 -d --name nlp_app nlp_image:prod
```

