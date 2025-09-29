class parent():
    def __init__(self,id,name) -> None:
        self.id=id
        self.name=name
    def parent_method():
        print("this is thr parent method")
    def parent_Method_2(self):
        print('thi is the method 2 i am calling')
        super().parent_method()
        return self.id
obj=parent(8902,"conquror")
parent.parent_method()
print(obj.id)
print("thi sis te t")