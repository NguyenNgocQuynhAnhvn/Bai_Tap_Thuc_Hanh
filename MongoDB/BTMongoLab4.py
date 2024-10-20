from pymongo import MongoClient
from datetime import datetime
# Buoc 1: ket noi den mongoDB
client = MongoClient("mongodb://localhost:27017/")
client.drop_database('facebookData1')
db = client['facebookData1'] # chon csdl

# Buoc 2: tao cac collections
users_collection = db['users']
posts_collection = db['posts']
comments_collection = db['comments']

# Buoc 3: them du lieu nguoi dung
users_data = [
    { 'user_id': 1, 'name': "Nguyen Van A", 'email': "a@gmail.com", 'age': 25 },
    { 'user_id': 2, 'name': "Tran Thi B", 'email': "b@gmail.com", 'age': 30 },
    { 'user_id': 3, 'name': "Le Van C", 'email': "c@gmail.com", 'age': 22 }
]
users_collection.insert_many(users_data)

posts_data = [
    { 'post_id': 1, 'user_id': 1, 'content': "Hôm nay thật đẹp trời!", 'created_at': datetime(2024, 10, 1) },
    { 'post_id': 2, 'user_id': 2, 'content': "Mình vừa xem một bộ phim hay!", 'created_at': datetime(2024, 10, 2) },
    { 'post_id': 3, 'user_id': 1, 'content': "Chúc mọi người một ngày tốt lành!", 'created_at': datetime(2024, 10, 3) }
]
posts_collection.insert_many(posts_data)

comments_data = [
    { 'comment_id': 1, 'post_id': 1, 'user_id': 2, 'content': "Thật tuyệt vời!", 'created_at': datetime(2024, 10, 1) },
    { 'comment_id': 2, 'post_id': 2, 'user_id': 3, 'content': "Mình cũng muốn xem bộ phim này!", 'created_at': datetime(2024, 10, 2) },
    { 'comment_id': 3, 'post_id': 3, 'user_id': 1, 'content': "Cảm ơn bạn!", 'created_at': datetime(2024, 10, 3) }
]
comments_collection.insert_many(comments_data)

# xem tat ca nguoi dung
print("Tat ca nguoi dung:")
for user in users_collection.find():
    print(user)

# Xem tất cả bài đăng của người dùng với user_id = 1
print("tat ca bai dang cua user_id 1: ")
user_post = posts_collection.find({'user_id': 1})
for user in user_post:
    print(user)

# Xem tất cả bình luận cho bài đăng với post_id = 1
print("tat ca binh luan cua user_id 1: ")
user_comment = comments_collection.find({'post_id': 1})
for user in user_comment:
    print(user)

# Truy vấn người dùng có độ tuổi trên 25
print("người dùng có độ tuổi trên 25: ")
user_age = users_collection.find({'age': {'$gt': 25}})
for user in user_age:
    print(user)

#Truy vấn tất cả bài đăng được tạo trong tháng 10
print("Tất cả bài đăng được tạo trong tháng 10: ")
date_post = posts_collection.find({'created_at': {'$gte': datetime(2024, 10, 1), '$lt': datetime(2024, 11, 1)}})
for post in date_post:
    print(post)

# Cập Nhật và Xóa Dữ Liệu
# Cập nhật nội dung bài đăng của người dùng với post_id = 1
posts_collection.update_one({'post_id': 1}, {'$set': {'content':"Hôm nay thời tiết thật đẹp!"  }})

# Xóa bình luận với comment_id = 2
comments_collection.delete_one({'comment_id': 2})

#  Xem lại dữ liệu sau khi cập nhật và xóa
print("\nDữ liệu người dùng sau khi cập nhật:")
for post in posts_collection.find():
    print(post)

print("\nDữ liệu video sau khi xóa:")
for comment in comments_collection.find():
    print(comment)


