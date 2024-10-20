from pymongo import MongoClient
from datetime import datetime
# Buoc 1: ket noi den mongoDB
client = MongoClient("mongodb://localhost:27017/")
client.drop_database('driveManagement1')
db = client['driveManagement1'] # chon csdl

# Buoc 2: tao cac collections
files_collection = db['files']

# Buoc 3: them du lieu 
file_data = [
    { 'file_id': 1, 'name': "Report.pdf", 'size': 2048, 'owner': "Nguyen Van A", 'created_at': datetime(2024, 1, 10), 'shared': False },
    { 'file_id': 2, 'name': "Presentation.pptx", 'size': 5120, 'owner': "Tran Thi B", 'created_at': datetime(2024, 1, 15), 'shared': True },
    { 'file_id': 3, 'name': "Image.png", 'size': 1024, 'owner': "Le Van C", 'created_at': datetime(2024, 1, 20), 'shared': False },
    { 'file_id': 4, 'name': "Spreadsheet.xlsx", 'size': 3072, 'owner': "Pham Van D", 'created_at': datetime(2024, 1, 25), 'shared': True },
    { 'file_id': 5, 'name': "Notes.txt", 'size': 512, 'owner': "Nguyen Thi E", 'created_at': datetime(2024, 1, 30), 'shared': False }
]
files_collection.insert_many(file_data)

# Xem tất cả tệp trong bộ sưu tập 'files'
print("tất cả tệp trong bộ sưu tập :")
for f in files_collection.find():
    print(f)

# Tìm tệp có kích thước lớn hơn 2000KB
print("tệp có kích thước lớn hơn 2000KB: ")
file_quality = files_collection.find({'size': {'$gt': 5000}})
for t in file_quality:
    print(t)

# Đếm tổng số tệp
print("Tổng số tệp: ")
total_files = files_collection.count_documents({})
print(total_files)

# Tìm tất cả tệp được chia sẻ
print(" tất cả tệp được chia sẻ: ")
share_file = files_collection.find({'shared': True})
for s in share_file:
    print(s)

# Thống kê số lượng tệp theo chủ sở hữu
print("Thống kê số lượng tệp theo chủ sở hữu: ")
file_agg = files_collection.aggregate([
    {
        '$group': {'_id': '$owner', 'total': {'$sum': 1}}
    }
])
for result in file_agg:
    print(result)

#  Cập nhật trạng thái chia sẻ của tệp với file_id = 1 thành true
files_collection.update_one({'file_id': 1}, {'$set': {'shared':True }})
#  Xóa tệp với file_id = 3
files_collection.delete_one({'file_id': 3})

print("\nDữ liệu người dùng sau khi cập nhật:")
for u in files_collection.find():
    print(u)

print("\nDữ liệu video sau khi xóa:")
for d in files_collection.find():
    print(d)

# Tìm tất cả tệp của người dùng có tên là "Nguyen Van A".
print('tất cả tệp của người dùng có tên là "Nguyen Van A": ')
name = files_collection.find({'owner':"Nguyen Van A" })
for owner in name:
    print(owner)

# Tìm tệp lớn nhất trong bộ sưu tập.
print('tệp lớn nhất trong bộ sưu tập: ')
size_file = files_collection.find().sort('size', -1).limit(1)
for y in size_file:
    print(y)

# Tìm số lượng tệp có kích thước nhỏ hơn 1000KB.
print("tệp có kích nhỏ hơn 1000KB: ")
file_quality1 = files_collection.find({'size': {'$lt': 1000}})
for t1 in file_quality1:
    print(t1)
# Tìm tất cả tệp được tạo trong tháng 1 năm 2024.
print("Tìm tất cả tệp được tạo trong tháng 1 năm 2024: ")
date_create = files_collection.find({'created_at': {'$gte': datetime(2024, 1, 1), '$lt': datetime(2024, 2, 1)}})
for create in date_create:
    print(create)

# Cập nhật tên tệp với `file_id` là 4 thành "New Spreadsheet.xlsx"
files_collection.update_one({'file_id': 4}, {'$set': {'name':"New Spreadsheet.xlsx" }})
#  Xóa tất cả tệp có kích thước nhỏ hơn 1000KB.
files_collection.delete_many({'size': {'$lt': 1000}})

for update in files_collection.find():
    print(update)

print("\nDữ liệu video sau khi xóa:")
for delete in files_collection.find():
    print(delete)






