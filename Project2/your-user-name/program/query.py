from relAlg import select, project, join


def query_a():
    select("Suppliers", "sid", "=", "s23")
    project("Suppliers", ["sname"])


def query_b():
    select("Suppliers", "sid", "=", "s23")
    project("Suppliers", ["sname"])


def query_c():
    join("Suppliers", "sid", "Supply", "sid")
    select("Supply", "pid", "=", "p15")
    project("Suppliers", ["address"])


def query_d():
    join("Suppliers", "sid", "Supply", "sid")
    select("Suppliers", "sname", "=", "Kiddie")
    project("Supply", ["cost"])


def query_e():
    pass


if __name__ == "__main__":
    select("../data/Temporary/rel00.txt", "cost", ">=", 40)
    select("../data/Temporary/rel00.txt", "cost", "=", 30.82)
    project("../data/Temporary/rel00.txt", ["sid", "cost"])
