class ParentClass:
    static_member = 0

class ChildClass(ParentClass):
    pass

# 在父类中访问静态成员变量
print(ParentClass.static_member)  # 输出: 0

# 在子类中访问静态成员变量
print(ChildClass.static_member)  # 输出: 0

# 修改父类的静态成员变量
ParentClass.static_member = 10

# 在父类中访问修改后的静态成员变量
print(ParentClass.static_member)  # 输出: 10

# 在子类中访问静态成员变量
print(ChildClass.static_member)  # 输出: 0
