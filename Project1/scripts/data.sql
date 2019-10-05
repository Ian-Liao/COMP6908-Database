use SupplyDB;

INSERT INTO Suppliers (sid, sname, address)
VALUES (111,	'John Smith',	'1 Elizabeth Ave');

INSERT INTO Suppliers (sid, sname, address)
VALUES (222,	'Linda Wang',	'20 Main Street');

INSERT INTO Suppliers (sid, sname, address)
VALUES (333,	'Paul Justin',	'150 Water Street');

INSERT INTO Suppliers (sid, sname, address)
VALUES (444,	'Andy Brown',	'1 Elizabeth Ave');

INSERT INTO Suppliers (sid, sname, address)
VALUES (555,	'Bob Lee',	'10 Governor Road');

INSERT INTO Suppliers (sid, sname, address)
VALUES (666,	'Lisa Reed',	'10 Governor Road');


INSERT INTO Parts (pid, pname, color)
VALUES ('P1',	'Mother board',	'Grey');

INSERT INTO Parts (pid, pname, color)
VALUES ('P2',	'CPU-AMD',	'White');

INSERT INTO Parts (pid, pname, color)
VALUES ('P3',	'Case',	'Grey');

INSERT INTO Parts (pid, pname, color)
VALUES ('P4',	'Monitor',	'White');

INSERT INTO Parts (pid, pname, color)
VALUES ('P5',	'Cable',	'Red');



INSERT INTO Catalog (sid, pid, cost)
VALUES (111, 'P1',	300);

INSERT INTO Catalog (sid, pid, cost)
VALUES (111,	 'P3',	50);

INSERT INTO Catalog (sid, pid, cost)
VALUES (111,	 'P4',	500);

INSERT INTO Catalog (sid, pid, cost)
VALUES (222,	 'P1',	350);

INSERT INTO Catalog (sid, pid, cost)
VALUES (222,	 'P2',	200);

INSERT INTO Catalog (sid, pid, cost)
VALUES (222,	 'P3',	70);

INSERT INTO Catalog (sid, pid, cost)
VALUES (222,	 'P5',	30);

INSERT INTO Catalog (sid, pid, cost)
VALUES (333,	 'P2',	210);

INSERT INTO Catalog (sid, pid, cost)
VALUES (333,	 'P3',	56);

INSERT INTO Catalog (sid, pid, cost)
VALUES (444,	 'P1',	350);

INSERT INTO Catalog (sid, pid, cost)
VALUES (444,	 'P2',	300);

INSERT INTO Catalog (sid, pid, cost)
VALUES (444,	 'P3',	48);

INSERT INTO Catalog (sid, pid, cost)
VALUES (444,	 'P4',	550);

INSERT INTO Catalog (sid, pid, cost)
VALUES (444,	 'P5',	29);

INSERT INTO Catalog (sid, pid, cost)
VALUES (555,	 'P3',	65);

INSERT INTO Catalog (sid, pid, cost)
VALUES (555,	 'P4',	600);
