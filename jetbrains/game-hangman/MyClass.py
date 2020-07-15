class MyClass:
    
    class_attr = "class"

    def __init__(self):
        self.inst_attr = "instance-init"
        self.output()
    
    def my_function(self):
        func_attr = "function"
        print("func_attr")

    def output(self):
        print("MyClass.class_attr", MyClass.class_attr)
        print("self.inst_attr", self.inst_attr)
        self.my_function()
        
my_class = MyClass()