class Student(object):
    def __init__(self,first='',last='',id=0):
        #print 'In the _init_ method'
        self.first_name_str=first
        self.last_name_str=last
        self.id_int=id
    def update(self,first='',last='',id=0):
        if first:
            self.first_name_str=first
        if last:
            self.last_name_str=last
        if id:
            self.id_int=id
    
    def _str_(self):
        #print 'In _str_method'
        return "{} {}, ID:{}".format(self.first_name_str,self.last_name_str,self.id_int)

s1=Student()
print(s1.last_name_str)
s2=Student(last='chuen', first='ch',id='A19MJ0024')
print(s2.last_name_str,s2.id_int)