drop table if exists employee;
create table employee (
	employee_id varchar(9)
	, first_name varchar(15)
	, mid_name varchar(15)
	, last_name varchar(15)
	, dob varchar(10)
	, address varchar(30)
	, gender varchar(3)
	, salary double
	, manager_id varchar(9)
	, department_id integer
	, primary key (employee_id)
	, foreign key (manager_id) REFERENCES employee(employee_id)
	, foreign key (department_id) REFERENCES department(department_id)
);

drop table if exists department;
create table department (
	department_id integer
	, department_name varchar(30)
	, manager_id varchar(9)
	, ngaynhanchuc varchar(10)
	, PRIMARY key (department_id)
	, foreign key (manager_id) REFERENCES employee(employee_id)
);

select * from employee