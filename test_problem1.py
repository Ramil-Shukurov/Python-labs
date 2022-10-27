from tuf_tests import *

set_keyboard_input([5])
main()
output = get_display_output()

assert ouput == [
                "Output: 5",
                ]


# make python print 5
