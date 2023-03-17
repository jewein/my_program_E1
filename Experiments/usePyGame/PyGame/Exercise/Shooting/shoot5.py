class CustomClass:
    def __init__(self, id):
        self.id = id
        self.secret = "Super Secret"

    def __class__(self):
        return "CustomClass"

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __setattr__(self, name, value):
        if name == "x":
            self._x = value * 2
        else:
            super().__setattr__(name, value)

    def __eq__(self, other):
        if isinstance(other, CustomClass):
            return self.id == other.id
        return False

    # def __str__(self):
        # return f"Instance of CustomClass with ID: {self.id}"


    def __getattribute__(self, name):
        if name == "secret":
            return "Access Denied"
        return super().__getattribute__(name)


# 创建 CustomClass 实例
obj1 = CustomClass(1)
obj2 = CustomClass(2)

# 调用 __eq__ 方法进行对象相等性比较
print(obj1 == obj2)  # False

# 调用 __str__ 方法获取对象的字符串表示形式
print(str(obj1))  # Instance of CustomClass with ID: 1

# 访问属性并观察 __getattribute__ 方法的行为
print(obj1.secret)  # Access Denied
