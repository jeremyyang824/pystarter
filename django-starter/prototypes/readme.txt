# 运行服务器
python prototypes.py runserver

# 生成静态网站
python prototypes.py build

# 运行静态网站
cd _build
python -m http.server 9000