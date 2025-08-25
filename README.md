# 📝 My Unordinary Life Blog

<img width="1899" height="862" alt="Ekran görüntüsü 2025-08-07 214337" src="https://github.com/user-attachments/assets/05e2f9ed-8a23-4e47-9337-97e5b1010c35" />

Kişisel blog projesi — Django ile geliştirilmiş, modüler yapıya sahip, içerik yönetimi ve admin paneli ile desteklenmiş bir web uygulaması.

[Website-linki](https://myunordinarylifeblog.pythonanywhere.com/)

## 🚀 Özellikler

- Blog postları oluşturma ve listeleme  
- Hakkımda ve ana sayfa bölümleri  
- Admin panel üzerinden içerik yönetimi  
- Statik dosya yönetimi (CSS, JS, görseller)  
- Tema desteği: farklı temalar ile özelleştirilebilir yapı

## 🧱 Teknolojiler

- Python   
- Django  
- HTML/CSS/JS    
- SQLite (opsiyonel)
- Django CK Editor 5

## ⚙️ Kurulum

```bash
git clone https://github.com/tutkun00/my_unordinary_life_blog.git
cd my_unordinary_life_blog

# Sanal ortam oluştur
python -m venv env
source env/bin/activate  # Windows için: .\env\Scripts\activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Veritabanı işlemleri
python manage.py migrate

# Sunucuyu başlat
python manage.py runserver
```
