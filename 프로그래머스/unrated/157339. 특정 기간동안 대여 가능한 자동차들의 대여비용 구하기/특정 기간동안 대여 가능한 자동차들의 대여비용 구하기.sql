/*
 * 자동차 ID, 자동차 종류, 대여금액(FEE)
    - 종류 : "세단" or "SUV"
    - 대여 가능 : 2022-11-01 ~ 2022-11-30
    - 대여 금액 : 50만 원 이상 ~ 200만원 미만
 - 금액 내림차, 자동차 종류 오름차, 자동차 ID 내림차
*/
# SELECT ccr.CAR_ID, ccr.CAR_TYPE, TRUNCATE(ccr.FEE - (ccr.FEE * (ccd.DISCOUNT_RATE / 100)), 0) as FEE
# FROM (
#     SELECT cr.CAR_ID, cc.CAR_TYPE, (cc.DAILY_FEE*30) as FEE
#     FROM  (CAR_RENTAL_COMPANY_CAR as cc RIGHT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY as cr ON cc.CAR_ID = cr.CAR_ID)
#     WHERE START_DATE < '2022-11-01' AND END_DATE >= '2022-11-30' AND (cc.DAILY_FEE*30) < 2000000 AND (cc.DAILY_FEE*30) >= 500000
#     ) as ccr LEFT JOIN (
#         SELECT CAR_TYPE, DISCOUNT_RATE
#         FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
#         WHERE DURATION_TYPE = '30일 이상'
#     ) as ccd ON ccr.CAR_TYPE = ccd.CAR_TYPE
# ORDER BY FEE DESC, ccr.CAR_TYPE, ccr.CAR_ID DESC

SELECT cc.CAR_ID, 
       cc.CAR_TYPE, 
       ROUND(cc.DAILY_FEE * (1 - (cd.DISCOUNT_RATE/100)) * 30) as FEE
FROM CAR_RENTAL_COMPANY_CAR as cc 
    INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN as cd ON cc.CAR_TYPE = cd.CAR_TYPE
WHERE cc.CAR_ID NOT IN (SELECT CAR_ID
                     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                     WHERE (CAR_ID, END_DATE) IN (SELECT CAR_ID, MAX(END_DATE)
                                                  FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                                                  GROUP BY CAR_ID)
                             # AND START_DATE >= '2022-11-01' AND END_DATE <= '2022-11-30')
                             AND (START_DATE between '2022-11-01' and '2022-11-30' OR
                                  END_DATE between '2022-11-01' and '2022-11-30' OR
                                  (START_DATE < '2022-11-01' and END_DATE >'2022-11-30')))
    AND cc.CAR_TYPE IN ("세단", "SUV")
    AND cd.DURATION_TYPE = "30일 이상"
    # AND ( (cc.DAILY_FEE - (cc.DAILY_FEE * (cd.DISCOUNT_RATE/100))) * 30 ) BETWEEN 500000 AND 1999999
    AND  (cc.DAILY_FEE * (1 - (cd.DISCOUNT_RATE/100)) * 30)  BETWEEN 500000 AND 1999999
ORDER BY FEE DESC, cc.CAR_TYPE, cc.CAR_ID DESC
