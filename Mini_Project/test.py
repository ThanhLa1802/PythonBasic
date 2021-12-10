
data = {
  "audience_id": "bb6ffdf8-3178-11ec-a8c5-ef701324ca44",
  "audience_brand": "Neutrogena",
  "audience_name": "Thanh1234",
  "duration_days": 40,
  "lookback_days": 30,
  "ttd_account_links": "8jbln2j,youtube.com",
  "created": "2021-10-20T07:38:35",
  "last_modified": "2021-10-20T07:38:35",
  "sql": "SELECT DISTINCT ga_sessions.clientId, \"bb6ffdf8-3178-11ec-a8c5-ef701324ca44\" AS audience_id, \"Thanh1234\" AS audience_name, ttd_id FROM  `jjt-consumerdatalake-bigquery.184383534.ga_sessions_*`  AS ga_sessions\nINNER JOIN `jjt-consumerdatalake-bigquery.ttd_analytics_dev.user_mapping` AS user_mapping ON user_mapping.clientId = ga_sessions.clientId\nLEFT JOIN UNNEST([ga_sessions.totals]) as totals\nLEFT JOIN UNNEST([ga_sessions.trafficSource]) as trafficSource\nLEFT JOIN UNNEST(ga_sessions.hits) as hits\nLEFT JOIN UNNEST([hits.page]) as hits_page\nLEFT JOIN UNNEST(hits.product) as hits_product\nLEFT JOIN `jjt-consumerdatalake-bigquery.eco_ga360_dev.ga360_product_hierarchy`\n     AS ga360_product_hierarchy ON hits_product.productSKU = ga360_product_hierarchy.productSku\nLEFT JOIN UNNEST([hits.eventInfo]) as hits_eventInfo\n WHERE\nTIMESTAMP(user_mapping._PARTITIONTIME) >= ((TIMESTAMP_ADD ( TIMESTAMP_TRUNC ( CURRENT_TIMESTAMP (), DAY, 'UTC' ), INTERVAL - 7 DAY )))\n AND TIMESTAMP(user_mapping._PARTITIONTIME) < CURRENT_TIMESTAMP()\n AND ttd_id NOT IN (SELECT ttd_id FROM `jjt-consumerdatalake-bigquery.ttd_analytics_dev.user_upload`)\nAND  ((( TIMESTAMP(PARSE_DATE('%Y%m%d', REGEXP_EXTRACT(_TABLE_SUFFIX,r'^\\d\\d\\d\\d\\d\\d\\d\\d')))  ) >= ((TIMESTAMP_ADD(TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(), DAY, 'UTC'), INTERVAL -7 DAY))) AND ( TIMESTAMP(PARSE_DATE('%Y%m%d', REGEXP_EXTRACT(_TABLE_SUFFIX,r'^\\d\\d\\d\\d\\d\\d\\d\\d')))  ) < ((TIMESTAMP_ADD(TIMESTAMP_ADD(TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(), DAY, 'UTC'), INTERVAL -7 DAY), INTERVAL 7 DAY))))) AND (ga360_product_hierarchy.dimension61 ) = 'Essential Health' AND (hits_page.hostName like  '%.com' )\n",
  "filter_body": "{\"Brand Site\": \"\", \"New vs Returning Visitor (leave blank to include both)\": \"\", \"Medium (the media channel that brought a user to site)\": \"\", \"Source (Site that brought in traffic)\": \"\", \"Page Path\": \"\", \"Event Category\": \"\", \"Time on Site (in seconds)\": \"\", \"Product GFO (cd61)\": \"Essential Health\", \"Product Sub Brand (cd62)\": \"\", \"Product Need State (cd63)\": \"\", \"Product Sub Category (cd64)\": \"\", \"Product Segment (cd65)\": \"\", \"Product Sub Segment (cd66)\": \"\", \"Existing Audience (OR)\": \"Test US Neutrogena 12, Thanh12\", \"Existing Audience (AND)\": \"\", \"Existing Audience (AND) #2\": \"\", \"Existing Audience (AND) #3\": \"\"}"
}




