from tud_test import set_keyboard_input, get_display_output
#import problem_1

def test_1():
    set_keyboard_input([5, 4])
    problem_1.main()
    output = get_display_output()
    
    assert output[-1] == "Area: 20.00"

def test_2():
    set_keyboard_input([5.6, 4.0])
    problem_1.main()

    output = get_display_output()
    assert output[-1] == "Area: 22.40"
    
    #assert output == ["length:", "width:","Area: 22.40"]

def test_3():
    set_keyboard_input([5.1, 4.0])
    problem_1.main()

    output = get_display_output()
    
    assert output == ["length:", "width:","Area: 20.40"]

def test_4():
    set_keyboard_input([5, 4.7])
    problem_1.main()

    output = get_display_output()
    
    assert output == ["length:", "width:","Area: 23.50"]

def test_5():
    set_keyboard_input([4.7, 5])
    problem_1.main()

    output = get_display_output()
    
    assert output == ["length:", "width:","Area: 23.50"]

def test_6():
    set_keyboard_input([-5.6, 4.0])
    problem_1.main()

    output = get_display_output()
    assert output[-1] == "Area: 22.40"

def test_7():
    set_keyboard_input([5.6, -4.0])
    problem_1.main()

    output = get_display_output()
    assert float(output[-1][-6:]) == 22.40
