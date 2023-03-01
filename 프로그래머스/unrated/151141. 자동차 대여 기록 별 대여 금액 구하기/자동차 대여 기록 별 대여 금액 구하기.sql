/*
 - 자동차 종류 : "트럭"인 대여기록
 - 대여 기록별 대여금액 -> 대여 기록ID, 대여 금액
    - 금액 내림차, ID 내림차
*/
# HISTORY 기간 연산
SELECT tot.HISTORY_ID, 
       # tot.PERIOD,
       # p.DISCOUNT_RATE,
       IF( ISNULL(p.DISCOUNT_RATE),  
          (tot.DAILY_FEE * tot.PERIOD),
          TRUNCATE( (tot.DAILY_FEE * tot.PERIOD) * (1-p.DISCOUNT_RATE/100) , 0)) AS FEE
FROM (SELECT h.HISTORY_ID, 
       h.CAR_ID, 
       c.CAR_TYPE, 
       c.DAILY_FEE, 
       h.PERIOD, 
       h.DURATION_TYPE
FROM (
    # (
    SELECT HISTORY_ID, 
        CAR_ID, 
        START_DATE,
        END_DATE,
        DATEDIFF(END_DATE,START_DATE) + 1 AS PERIOD,
        (CASE WHEN DATEDIFF(END_DATE,START_DATE)+1 >= 90 
                THEN '90일 이상'
              WHEN DATEDIFF(END_DATE,START_DATE)+1 >= 30 
                THEN '30일 이상'
              WHEN DATEDIFF(END_DATE,START_DATE)+1 >= 7 
                THEN '7일 이상'
              ELSE
                NULL
        END) as DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    ) as h LEFT JOIN
    (
    SELECT CAR_ID, CAR_TYPE, DAILY_FEE
    FROM CAR_RENTAL_COMPANY_CAR
    ) as c ON h.CAR_ID = c.CAR_ID
     # ) as tot 
    # LEFT JOIN
    # (
    # SELECT DISCOUNT_RATE
    # FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    # ) as p ON tot.CAR_TYPE = p.CAR_TYPE and tot.DURATION_TYPE = p.CAR_TYPE
 ) as tot LEFT JOIN 
 (
    SELECT CAR_TYPE, DURATION_TYPE, DISCOUNT_RATE
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
 ) as p ON (tot.CAR_TYPE, tot.DURATION_TYPE) = (p.CAR_TYPE, p.DURATION_TYPE)
WHERE tot.CAR_TYPE = "트럭"
ORDER BY FEE DESC, tot.HISTORY_ID DESC

# SELECT *
# FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
     