from pymongo import MongoClient
from datetime import datetime

# Buoc 1: ket noi den mongoDB
client = MongoClient("mongodb://localhost:27017/")
client.drop_database('tiktok1')
db = client['tiktok1'] # chon csdl

# Buoc 2: tao cac collections
users_collection = db['users']
videos_collection = db['videos']

# Buoc 3: them du lieu nguoi dung
users_data = [
    { 'user_id': 1, 'username': 'user1', 'full_name': 'Nguyen Van A', 'followers': 1500, 'following': 200 },
    { 'user_id': 2, 'username': 'user2', 'full_name': 'Tran Thi B', 'followers': 2000, 'following': 300 },
    { 'user_id': 3, 'username': 'user3', 'full_name': 'Le Van C', 'followers': 500, 'following': 100 }
]
users_collection.insert_many(users_data)

# Bước 4: Thêm dữ liệu video
videos_data = [
    { 'video_id': 1, 'user_id': 1, 'title': 'Video 1', 'views': 10000, 'likes': 500, 'created_at': datetime(2024, 1, 1) },
    { 'video_id': 2, 'user_id': 2, 'title': 'Video 2', 'views': 20000, 'likes': 1500, 'created_at': datetime(2024, 1, 5) },
    { 'video_id': 3, 'user_id': 3, 'title': 'Video 3', 'views': 5000, 'likes': 200, 'created_at': datetime(2024, 1, 10) }
]
videos_collection.insert_many(videos_data)  # Thêm dữ liệu video

# Buoc 5: truy van du lieu
# xem tat ca nguoi dung
print("Tat ca nguoi dung:")
for user in users_collection.find():
    print(user)

# tim video co luot xem nhieu nhat
print("Video co nhieu luot xem nhat:")

mosted_viewed_video = videos_collection.find().sort('views', -1).limit(1)
for user in mosted_viewed_video:    
    print(user)

# tim tat ca video cua nguoi dung co username laf user1
print("tat ca video cua user1: ")
user_videos = videos_collection.find({'user_id': 1})
for video in user_videos:
    print(video)

# cap nhat du lieu
users_collection.update_one({'user_id': 1}, {'$set': {'followers': 2000}})

# xoa video co video_id laf 3
videos_collection.delete_one({'video_id': 3})

#  Xem lại dữ liệu sau khi cập nhật và xóa
print("\nDữ liệu người dùng sau khi cập nhật:")
for user in users_collection.find():
    print(user)

print("\nDữ liệu video sau khi xóa:")
for video in videos_collection.find():
    print(video)







