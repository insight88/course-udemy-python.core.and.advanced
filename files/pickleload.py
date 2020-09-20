import pickle

f = open("student.dat", "rb")
obj = pickle.load(f)
# ! pickle.load(file)로 불러올 수 있는 file은 pickle.dump()로 쓰인 binary 파일이어야 한다
obj.display()
f.close()
