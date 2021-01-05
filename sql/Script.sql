1. �������� ������� ����������� � ������ �� ��������
��������� � ������ ������

create or replace function "GetRecords"() returns setof record
language plpgsql
as
$$
declare
temprow varchar;
tempRecord record;

begin
for temprow in select distinct dep from salary_table as dictincted
loop
select * from salary_table where dep = temprow order by salary desc limit 1 offset 1 into tempRecord;
return next tempRecord;
end loop;
end
$$;

select * from "GetRecords"() as x(id int, surname varchar, v_position varchar, dep varchar, salary int)


2. �������� �������, ���������� �������� ������ � ����� ������� � ������������ ������� ����������� ����� �,� � ������ �������	

	
select dep, string_agg(surname, ', ' order by surname) as cat_surname
	from salary_table 
	group by dep ;



3. �������� ���������� �����������, ������� �������� ������ 100000,
� ���������� ����������� ������ 90000 ����� �������� ��� ������������� �����������


select 
	count(case when salary < 90000 then 1 else null end) as less_90000,
	count(case when salary > 100000 then 1 else null end) as more_100000 
		from salary_table
	;
	
	
	

	