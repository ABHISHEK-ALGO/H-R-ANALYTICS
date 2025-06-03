use employee;
SHOW TABLES;
SELECT * FROM hr_enhanced;

-- What was the average satisfaction level of employees who left the company?
SELECT round(AVG(satisfaction_level),2) as avg_satisfaction_left
FROM hr_enhanced
WHERE `LEFT` = 1;

-- Is lack of promotion related to employees leaving the company?
SELECT PROMOTION_LAST_5YEARS,
COUNT(*) AS TOTAL,
SUM(CASE WHEN `LEFT` = 1 THEN 1 ELSE 0 END) AS EMPLOYEE_LEFT,
ROUND(SUM(CASE WHEN `LEFT` = 1 THEN 1 ELSE 0 END)*100/COUNT(*),2) AS ATTRITION_RATE_PERCENTAGE
FROM HR_ENHANCED
GROUP BY PROMOTION_LAST_5YEARS;

-- How balanced is the gender distribution across departments?
SELECT 
    Department,
    Gender,
    COUNT(*) AS count
FROM hr_enhanced
GROUP BY Department, Gender
ORDER BY Department;

-- How many high performers (last evaluation > 0.8) left the company?
SELECT 
    COUNT(CASE WHEN `left` = 1 THEN 1 END) AS high_performers_left,
    COUNT(*) AS total_high_performers,
    ROUND(COUNT(CASE WHEN `left` = 1 THEN 1 END) * 100.0 / COUNT(*), 2) AS attrition_rate_percentage
FROM hr_enhanced
WHERE last_evaluation > 0.8;





