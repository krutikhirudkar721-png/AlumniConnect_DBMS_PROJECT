USE alumniconnect;
-- Basic filters
SELECT * FROM alumni WHERE graduation_year BETWEEN 2020 AND 2024;
SELECT a.alumni_id,CONCAT(a.first_name,' ',a.last_name) name,d.department_name FROM alumni a JOIN departments d ON a.department_id=d.department_id WHERE d.department_name='Computer Science';
SELECT DISTINCT a.alumni_id,CONCAT(a.first_name,' ',a.last_name) name,co.industry FROM alumni a JOIN career_history ch ON a.alumni_id=ch.alumni_id JOIN companies co ON ch.company_id=co.company_id WHERE co.industry='IT' AND ch.is_current=1;
SELECT a.alumni_id,CONCAT(a.first_name,' ',a.last_name) name,co.company_name FROM alumni a JOIN career_history ch ON a.alumni_id=ch.alumni_id JOIN companies co ON ch.company_id=co.company_id WHERE co.company_name='TechNova Solutions';
SELECT * FROM alumni WHERE location LIKE '%Bangalore%';
-- Skill and multi-skill search
SELECT a.alumni_id,CONCAT(a.first_name,' ',a.last_name) name FROM alumni a JOIN alumni_skills x ON a.alumni_id=x.alumni_id JOIN skills s ON x.skill_id=s.skill_id WHERE s.skill_name='Python';
SELECT a.alumni_id,CONCAT(a.first_name,' ',a.last_name) name FROM alumni a JOIN alumni_skills x ON a.alumni_id=x.alumni_id JOIN skills s ON x.skill_id=s.skill_id WHERE s.skill_name IN('Python','SQL') GROUP BY a.alumni_id,name HAVING COUNT(DISTINCT s.skill_name)=2;
-- Experience, mentorship and reports
SELECT a.alumni_id,CONCAT(a.first_name,' ',a.last_name) name,ROUND(SUM(TIMESTAMPDIFF(MONTH,ch.start_date,COALESCE(ch.end_date,CURDATE())))/12,1) years_experience FROM alumni a JOIN career_history ch ON a.alumni_id=ch.alumni_id GROUP BY a.alumni_id,name HAVING years_experience>3;
SELECT a.alumni_id,CONCAT(a.first_name,' ',a.last_name) name,m.domain FROM alumni a JOIN mentorship m ON a.alumni_id=m.alumni_id WHERE m.is_available=1;
SELECT d.department_name,COUNT(a.alumni_id) total FROM departments d LEFT JOIN alumni a ON d.department_id=a.department_id GROUP BY d.department_id ORDER BY total DESC;
SELECT graduation_year,COUNT(*) total FROM alumni GROUP BY graduation_year ORDER BY graduation_year;
SELECT s.skill_name,COUNT(*) total FROM alumni_skills x JOIN skills s ON x.skill_id=s.skill_id GROUP BY s.skill_id ORDER BY total DESC;
SELECT co.company_name,COUNT(DISTINCT ch.alumni_id) total FROM companies co JOIN career_history ch ON co.company_id=ch.company_id WHERE ch.is_current=1 GROUP BY co.company_id ORDER BY total DESC;
SELECT a.alumni_id,CONCAT(a.first_name,' ',a.last_name) name,co.company_name,ch.designation,ch.start_date,ch.end_date FROM alumni a JOIN career_history ch ON a.alumni_id=ch.alumni_id JOIN companies co ON ch.company_id=co.company_id ORDER BY a.alumni_id,ch.start_date DESC;
SELECT a.alumni_id,CONCAT(a.first_name,' ',a.last_name) name FROM alumni a WHERE EXISTS(SELECT 1 FROM mentorship m WHERE m.alumni_id=a.alumni_id);
-- Complex search
SELECT DISTINCT a.alumni_id,CONCAT(a.first_name,' ',a.last_name) name FROM alumni a JOIN departments d ON a.department_id=d.department_id JOIN career_history ch ON a.alumni_id=ch.alumni_id AND ch.is_current=1 JOIN companies co ON ch.company_id=co.company_id WHERE a.graduation_year BETWEEN 2020 AND 2024 AND d.department_name='Computer Science' AND co.industry='IT' AND a.location='Bangalore' AND EXISTS(SELECT 1 FROM alumni_skills x JOIN skills s ON x.skill_id=s.skill_id WHERE x.alumni_id=a.alumni_id AND s.skill_name='Python') AND EXISTS(SELECT 1 FROM mentorship m WHERE m.alumni_id=a.alumni_id AND m.is_available=1);
-- Transaction demonstration
START TRANSACTION; UPDATE alumni SET location='Pune' WHERE alumni_id=1; UPDATE mentorship SET availability_details='Saturday mornings' WHERE alumni_id=1; COMMIT;
START TRANSACTION; UPDATE alumni SET location='Rollback Test' WHERE alumni_id=1; ROLLBACK;
-- DDL demonstrations can be run against a temporary test table: CREATE/ALTER/DROP/TRUNCATE.
