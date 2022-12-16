from source_code.Classes import classes as cl

counter = cl.NumVariables(0)


def up(count):
    """ make score counter bigger on 1 point """
    count.adder(1)
