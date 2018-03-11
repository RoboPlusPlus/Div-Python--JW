class BaseOject:
    object_type = ""
    def __init__(self, _object_type):
        self.object_type = str(_object_type)
        self.di_list = []
        self.do_list = []
        self.ai_list = []
        self.ao_list = []

    def get_object_type(self):
        return str(self.object_type)

    def add_di_entry(self, _input):
        self.di_list.append(str(_input))

    def add_do_entry(self, _input):
        self.do_list.append(_input)

    def add_ai_entry(self, _input):
        self.ai_list.append(_input)

    def add_ao_entry(self, _input):
        self.ao_list.append(_input)

    def get_di(self):
        return str(self.di_list)

    def get_do(self):
        return self.do_list

    def get_ai(self):
        return self.ai_list

    def get_ao(self):
        return self.ao_list

def main():
    objectlist = []
    for i in range(5):
        objectlist.append(BaseOject(str(i)))
    hest = BaseOject("Hest")

    a=1
    for o in objectlist:
        o.add_di_entry(str(a))
        a= a+1

    for ob in objectlist:
        print(ob.get_di())
    print(hest.get_di())


if __name__ == '__main__':
    main()