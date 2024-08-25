#!/bin/bash

# Bỏ qua lỗi nếu các lệnh không thành công
set -e

# Đảm bảo rằng script đang chạy từ thư mục gốc của dự án
cd "$(dirname "$0")"

# Cài đặt các phụ thuộc
echo "Cài đặt các phụ thuộc từ requirements.txt..."
pip install -r requirements.txt

# Tạo hoặc cập nhật cơ sở dữ liệu
echo "Thực hiện các migrations..."
python manage.py migrate

echo "Hoàn tất build!"
