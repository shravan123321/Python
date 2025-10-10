'''
#generators
def serve_chai() :
    yield "Cup 1: masala chai"
    yield "Cup 2: Ginger chai"
    yield "Cup 3: Elaichi chai"
    yield "Cup 4: Coffi chai"

stall = serve_chai()
for chai in stall :
    print(chai) 

# lets create the normal function 
def get_chai_list() :
    return ["Cup 1","Cup 2","Cup 3","Cup 4"]

cup_list=get_chai_list()
for cup in cup_list :
    print(cup)

'''
#generator  Function 
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai_list = get_chai_gen()
# for cup in chai_list :
#     print(cup) 
print(next(chai_list))
print(next(chai_list))
print(next(chai_list))
# print(next(chai_list)) #gives error (StopIteration)