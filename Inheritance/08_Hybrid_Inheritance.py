# Hybrid Inheritance
class grend_parent:
    def __init__(self, name):
        self.name = name
    def work(self):
        print("Business Men")

class child1(grend_parent):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
    def work(self):
        print("Student For graduation: final year BCA")

class child2(grend_parent):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
    def work(self):
        print("Working for Company Role: Software Engineer")

# child_hod inherits from both child1 and child2 (Hybrid inheritance)
class child_hod(child1, child2):
    def __init__(self, name, type, home1):
        child1.__init__(self, name, type)
        child2.__init__(self, name, type)
        self.home1 = home1
    def work(self):
        print("Business Analyst")

obj=child_hod("shravan yadav","BCA","Jaipur")
obj.work()
