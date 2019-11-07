from relAlg import select, project, join

SUPPLY_FILE = "../data/Temporary/rel00.txt"
PRODUCTS_FILE = "../data/Temporary/rel01.txt"
SUPPLIERS_FILE = "../data/Temporary/rel02.txt"


def query_a():
    tmp_result = select(SUPPLIERS_FILE, "sid", "=", "s23")
    query_result = project(tmp_result, ["sname"])
    print(query_result)


def query_b():
    tmp_result = select(SUPPLIERS_FILE, "sid", "=", "s23")
    query_result = project(tmp_result, ["sname"])
    print(query_result)


def query_c():
    tmp_result = select(SUPPLY_FILE, "pid", "=", "p15")
    tmp_result = join(SUPPLIERS_FILE, "sid", tmp_result, "sid")
    project(tmp_result, ["address"])


def query_d():
    tmp_result = select(SUPPLIERS_FILE, "sname", "=", "Kiddie")
    tmp_result = join(tmp_result, "sid", SUPPLY_FILE, "sid")
    tmp_result = select(tmp_result, "pid", "=", "p20")
    project(tmp_result, ["cost"])


def query_e():
    tmp_result = select(SUPPLY_FILE, "cost", ">=", 47.00)
    tmp_result = join(tmp_result, "pid", PRODUCTS_FILE, "pid")
    tmp_result = join(tmp_result, "sid", SUPPLIERS_FILE, "sid")
    project(tmp_result, ["sname", "pname", "cost"])


if __name__ == "__main__":
    query_a()
    query_b()
    query_c()
    query_d()
    query_e()

