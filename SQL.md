## World DB, MySql

Find top 3 cities for eacy country:

```sql

SELECT
    c.Name AS Country,
    ci.Name AS City,
    ci.Population
FROM
    City ci
JOIN
    Country c ON ci.CountryCode = c.Code
LEFT JOIN
    City ci2 ON ci.CountryCode = ci2.CountryCode AND ci.Population < ci2.Population
GROUP BY
    c.Name, ci.Name, ci.Population
HAVING
    COUNT(ci2.Population) < 3 -- Using < 3 because ci.Population < ci2.Population
ORDER BY
    c.Name, ci.Population DESC;

```

```sql

SELECT
    c.Name AS Country,
    ci.Name AS City,
    ci.Population
FROM
    City ci
JOIN
    Country c ON ci.CountryCode = c.Code
WHERE (
    SELECT
        COUNT(*)
    FROM
        City ci2
    WHERE
        ci2.CountryCode = ci.CountryCode AND ci2.Population >= ci.Population
) <= 3
ORDER BY
    c.Name, ci.Population DESC;

```

```sql

SELECT
    Country,
    City,
    Population
FROM (
    SELECT
        c.Name AS Country,
        ci.Name AS City,
        ci.Population,
        ROW_NUMBER() OVER (PARTITION BY c.Code ORDER BY ci.Population DESC) as rn
    FROM
        City ci
    JOIN
        Country c ON ci.CountryCode = c.Code
) AS ranked_cities
WHERE rn <= 3
ORDER BY Country, Population DESC;

```
