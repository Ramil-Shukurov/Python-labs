import problem_1
import builtins
from random import uniform

input_values = []
print_values = []



def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)

def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)

def get_display_output():
    global print_values
    return print_values
"""
def get_input():
    global input_values_copy
    return input_values_copy
"""
def set_keyboard_input(mocked_inputs):
    global input_values#, input_values_copy
    
    mock_input_output_start()
    input_values = mocked_inputs
    #input_values_copy = mocked_inputs.copy() 
    

def test_2():
    a =  uniform(10, 30)
    b =  uniform(10, 30)
    set_keyboard_input([a,b])
    problem_1.main()

    output = get_display_output()
    assert output[-1] == f"Area: {(a*b):.2f}"
    
    #assert output == ["length:", "width:","Area: 22.40"]

    assert output[-1] == "Area: 22.40"
