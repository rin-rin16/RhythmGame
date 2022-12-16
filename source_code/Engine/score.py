from source_code.Classes import classes as CL

counter = CL.NumVariables(0)


def up(counter):
    """ make score counter bigger on 1 point """
    counter.adder(1)
