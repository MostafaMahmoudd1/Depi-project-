
-- 1. Top 3 Performers by Subject
WITH RankedScores AS (
    SELECT 
        student_id,
        name,
        subject,
        score,
        ROW_NUMBER() OVER (PARTITION BY subject ORDER BY score DESC) AS rank
    FROM student_performance
)
SELECT 
    student_id,
    name,
    subject,
    score
FROM RankedScores
WHERE rank <= 3
ORDER BY subject, score DESC;

-- 2. Daily Attendance Trends
SELECT 
    date,
    attendance,
    COUNT(*) AS count
FROM student_performance
GROUP BY 
    date,
    attendance
ORDER BY 
    date ASC;

-- 3. Average Scores by Month (SQL Server Format)
SELECT 
    FORMAT(date, 'yyyy-MM') AS month,
    AVG(score) AS average_score
FROM student_performance
GROUP BY 
    FORMAT(date, 'yyyy-MM')
ORDER BY 
    month ASC;
