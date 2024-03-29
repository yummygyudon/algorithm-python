/*
 * 2022년 1월 판매 기준
 * 저자별 & 카테고리별 매출액 (판매량 * 판매가)
 * 저자ID, 저자명, 카테고리, 매출액
    - 저자ID, 카테고리 내림차
*/
SELECT ab.AUTHOR_ID, ab.AUTHOR_NAME, ab.CATEGORY, SUM(ab.PRICE * s.SALED) AS TOTAL_SALES
FROM(SELECT b.BOOK_ID, b.CATEGORY, b.PRICE,a.AUTHOR_ID, a.AUTHOR_NAME
    FROM BOOK as b LEFT JOIN AUTHOR as a ON b.AUTHOR_ID = a.AUTHOR_ID
    ) as ab 
        LEFT JOIN (
    SELECT BOOK_ID, SUM(SALES) as SALED
    FROM BOOK_SALES
    WHERE SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
    GROUP BY BOOK_ID) as s 
        ON ab.BOOK_ID = s.BOOK_ID
GROUP BY ab.AUTHOR_NAME , ab.CATEGORY
ORDER BY ab.AUTHOR_ID , ab.CATEGORY DESC


