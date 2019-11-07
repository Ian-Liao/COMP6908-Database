from relAlg import select, project, join


def query_a():
    tmp_result = select("../data/Temporary/rel10.txt", "sid", "=", "s23")
    query_result = project(tmp_result, ["sname"])
    print(query_result)


def query_b():
    tmp_result = select("../data/Temporary/rel10.txt", "sid", "=", "s23")
    query_result = project(tmp_result, ["sname"])
    print(query_result)


def query_c():
    select("Supply", "pid", "=", "p15")
    join("Suppliers", "sid", "Supply", "sid")
    project("Suppliers", ["address"])


def query_d():
    select("Suppliers", "sname", "=", "Kiddie")
    join("Suppliers", "sid", "Supply", "sid")
    project("Supply", ["cost"])


def query_e():
    select("Supply", "cost", ">=", 47.00)
    join("Supply", "pid", "Products", "pid")
    join("Supply", "sid", "Suppliers", "sid")
    project("tmp.txt", ["sname", "pname", "cost"])


if __name__ == "__main__":
    query_a()

