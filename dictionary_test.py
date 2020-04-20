import types

def test():
    print('1')
# end test

def test2():
    print('2')
# end test2

def main():
    
    _dictionary = {'BIRD': {'string1',  test, 'string2'},
                   'PLANE': {'string3', test2,'string3'}}

    for key, values in _dictionary.items():

        print(key)

        for value in values:
            print(value)
            if(isinstance(value, types.FunctionType)):
                print('it worked')
                value()

# end main

main()
