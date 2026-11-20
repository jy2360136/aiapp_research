# `.private` 原始证据迁移记录

- 迁移日期：2026-11-20
- 迁移文件：198 个
- 迁移大小：58361804 bytes
- 迁移原则：原始敏感证据不再集中存放在 `.private/`，而是归入对应产品与版本目录的 `raw/` 子目录。
- 安全要求：`raw/` 中可能包含账号、手机号、验证码、持仓等敏感信息，不得对外分享或移入公开仓库。

## 目标目录汇总

| 目录 | 文件数 | 字节数 |
|---|---:|---:|
| `research/competitors/cjsc-moo/v1.1.6_20261118/` | 18 | 6015498 |
| `research/competitors/eastmoney-innovation/v1.6.0_20261118/` | 36 | 10006348 |
| `research/competitors/galaxy-stock/vunknown_20261117/` | 6 | 2522411 |
| `research/competitors/gtht-lingxiai/v9.30.45_20261118/` | 48 | 18768249 |
| `research/competitors/guotai-dazhihui/vunknown_20261117/` | 3 | 1075914 |
| `research/competitors/hexin-stockassistant/v5.3.1_20261118/` | 21 | 3164180 |
| `research/competitors/htsc-cftlight/v2.0.6_20261118/` | 27 | 9556616 |
| `research/competitors/pingan-smt/vunknown_20261117/` | 3 | 428271 |
| `research/target-dongzheng-ai/logs/v1.0.0_20261118/` | 11 | 814687 |
| `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/` | 13 | 5632727 |
| `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/` | 12 | 376903 |

## 文件清单

| 原路径 | 新路径 | 字节数 |
|---|---|---:|
| `raw/competitors/cjsc-moo/metadata/20261118_103301_home.json` | `research/competitors/cjsc-moo/v1.1.6_20261118/metadata/raw/20261118_103301_home.json` | 807 |
| `raw/competitors/cjsc-moo/metadata/20261118_103503_home_clean.json` | `research/competitors/cjsc-moo/v1.1.6_20261118/metadata/raw/20261118_103503_home_clean.json` | 648 |
| `raw/competitors/cjsc-moo/metadata/20261118_112504_agent_screen.json` | `research/competitors/cjsc-moo/v1.1.6_20261118/metadata/raw/20261118_112504_agent_screen.json` | 654 |
| `raw/competitors/cjsc-moo/metadata/20261118_112546_agent_screen_2.json` | `research/competitors/cjsc-moo/v1.1.6_20261118/metadata/raw/20261118_112546_agent_screen_2.json` | 660 |
| `raw/competitors/cjsc-moo/metadata/20261118_112630_ai_prompt_tapped.json` | `research/competitors/cjsc-moo/v1.1.6_20261118/metadata/raw/20261118_112630_ai_prompt_tapped.json` | 666 |
| `raw/competitors/cjsc-moo/metadata/20261118_112814_ai_answer_26s.json` | `research/competitors/cjsc-moo/v1.1.6_20261118/metadata/raw/20261118_112814_ai_answer_26s.json` | 657 |
| `raw/competitors/cjsc-moo/screenshots/20261118_103301_home.png` | `research/competitors/cjsc-moo/v1.1.6_20261118/screenshots/raw/20261118_103301_home.png` | 2075087 |
| `raw/competitors/cjsc-moo/screenshots/20261118_103503_home_clean.png` | `research/competitors/cjsc-moo/v1.1.6_20261118/screenshots/raw/20261118_103503_home_clean.png` | 1043432 |
| `raw/competitors/cjsc-moo/screenshots/20261118_112504_agent_screen.png` | `research/competitors/cjsc-moo/v1.1.6_20261118/screenshots/raw/20261118_112504_agent_screen.png` | 1026176 |
| `raw/competitors/cjsc-moo/screenshots/20261118_112546_agent_screen_2.png` | `research/competitors/cjsc-moo/v1.1.6_20261118/screenshots/raw/20261118_112546_agent_screen_2.png` | 1042932 |
| `raw/competitors/cjsc-moo/screenshots/20261118_112630_ai_prompt_tapped.png` | `research/competitors/cjsc-moo/v1.1.6_20261118/screenshots/raw/20261118_112630_ai_prompt_tapped.png` | 302043 |
| `raw/competitors/cjsc-moo/screenshots/20261118_112814_ai_answer_26s.png` | `research/competitors/cjsc-moo/v1.1.6_20261118/screenshots/raw/20261118_112814_ai_answer_26s.png` | 428355 |
| `raw/competitors/cjsc-moo/ui-hierarchy/20261118_103301_home.xml` | `research/competitors/cjsc-moo/v1.1.6_20261118/ui-hierarchy/raw/20261118_103301_home.xml` | 3199 |
| `raw/competitors/cjsc-moo/ui-hierarchy/20261118_103503_home_clean.xml` | `research/competitors/cjsc-moo/v1.1.6_20261118/ui-hierarchy/raw/20261118_103503_home_clean.xml` | 24333 |
| `raw/competitors/cjsc-moo/ui-hierarchy/20261118_112504_agent_screen.xml` | `research/competitors/cjsc-moo/v1.1.6_20261118/ui-hierarchy/raw/20261118_112504_agent_screen.xml` | 24364 |
| `raw/competitors/cjsc-moo/ui-hierarchy/20261118_112546_agent_screen_2.xml` | `research/competitors/cjsc-moo/v1.1.6_20261118/ui-hierarchy/raw/20261118_112546_agent_screen_2.xml` | 24353 |
| `raw/competitors/cjsc-moo/ui-hierarchy/20261118_112630_ai_prompt_tapped.xml` | `research/competitors/cjsc-moo/v1.1.6_20261118/ui-hierarchy/raw/20261118_112630_ai_prompt_tapped.xml` | 8745 |
| `raw/competitors/cjsc-moo/ui-hierarchy/20261118_112814_ai_answer_26s.xml` | `research/competitors/cjsc-moo/v1.1.6_20261118/ui-hierarchy/raw/20261118_112814_ai_answer_26s.xml` | 8387 |
| `raw/competitors/eastmoney-innovation/code_request_time.json` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/metadata/raw/code_request_time.json` | 34 |
| `raw/competitors/eastmoney-innovation/code_request_time_2.json` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/metadata/raw/code_request_time_2.json` | 34 |
| `raw/competitors/eastmoney-innovation/metadata/20261117_174814_home.json` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/metadata/raw/20261117_174814_home.json` | 1126 |
| `raw/competitors/eastmoney-innovation/metadata/20261118_134106_v1_6_0_step01_login_page.json` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/metadata/raw/20261118_134106_v1_6_0_step01_login_page.json` | 833 |
| `raw/competitors/eastmoney-innovation/metadata/20261118_135242_v1_6_0_step02_suggestion_running.json` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/metadata/raw/20261118_135242_v1_6_0_step02_suggestion_running.json` | 976 |
| `raw/competitors/eastmoney-innovation/metadata/20261118_135325_v1_6_0_step03_suggestion_answer.json` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/metadata/raw/20261118_135325_v1_6_0_step03_suggestion_answer.json` | 973 |
| `raw/competitors/eastmoney-innovation/screenshots/20261117_174814_home.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261117_174814_home.png` | 332975 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_122146_login_gate.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_122146_login_gate.png` | 548377 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_134106_v1_6_0_step01_login_page.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_134106_v1_6_0_step01_login_page.png` | 1034102 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_135134_v1.6.0_step01_current.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_135134_v1.6.0_step01_current.png` | 225486 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_135242_v1_6_0_step02_suggestion_running.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_135242_v1_6_0_step02_suggestion_running.png` | 545747 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_135325_v1_6_0_step03_suggestion_answer.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_135325_v1_6_0_step03_suggestion_answer.png` | 544489 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_135411_v1.6.0_step04_login_blank.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_135411_v1.6.0_step04_login_blank.png` | 544499 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_135415_v1.6.0_step05_phone_entered_private.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_135415_v1.6.0_step05_phone_entered_private.png` | 168448 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_135632_v1.6.0_step05_phone_entered_private_retry.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_135632_v1.6.0_step05_phone_entered_private_retry.png` | 554783 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_135913_v1.6.0_step06_terms_selected_private.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_135913_v1.6.0_step06_terms_selected_private.png` | 547781 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_135914_v1.6.0_step07_code_requested_private.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_135914_v1.6.0_step07_code_requested_private.png` | 433820 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_141055_v1.6.0_step08_terms_agreed_private.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_141055_v1.6.0_step08_terms_agreed_private.png` | 571310 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_141458_v1.6.0_step09_code_entered_private.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_141458_v1.6.0_step09_code_entered_private.png` | 548358 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_141639_v1.6.0_step10_after_login_private.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_141639_v1.6.0_step10_after_login_private.png` | 451895 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_141841_v1.6.0_debug_after_resend.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_141841_v1.6.0_debug_after_resend.png` | 550435 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_143023_v1.6.0_step12_login_result_private.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_143023_v1.6.0_step12_login_result_private.png` | 451955 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_143759_v1.6.0_step13_fast_login_result_private.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_143759_v1.6.0_step13_fast_login_result_private.png` | 234238 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_143859_v1.6.0_step14_home_after_login.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_143859_v1.6.0_step14_home_after_login.png` | 228442 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_143957_v1.6.0_step15_query_running.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_143957_v1.6.0_step15_query_running.png` | 228317 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_144023_v1.6.0_step16_query_answer.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_144023_v1.6.0_step16_query_answer.png` | 227568 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_144306_v1.6.0_step15_query_running_corrected.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_144306_v1.6.0_step15_query_running_corrected.png` | 187928 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_144332_v1.6.0_step16_query_answer_corrected.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_144332_v1.6.0_step16_query_answer_corrected.png` | 187928 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_144442_v1.6.0_step17_answer_loading.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_144442_v1.6.0_step17_answer_loading.png` | 204866 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_144512_v1.6.0_step18_answer_complete.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_144512_v1.6.0_step18_answer_complete.png` | 371610 |
| `raw/competitors/eastmoney-innovation/screenshots/20261118_144621_v1.6.0_step19_answer_top.png` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_144621_v1.6.0_step19_answer_top.png` | 33176 |
| `raw/competitors/eastmoney-innovation/ui-hierarchy/20261117_174814_home.xml` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/ui-hierarchy/raw/20261117_174814_home.xml` | 6651 |
| `raw/competitors/eastmoney-innovation/ui-hierarchy/20261118_134106_v1_6_0_step01_login_page.xml` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/ui-hierarchy/raw/20261118_134106_v1_6_0_step01_login_page.xml` | 37074 |
| `raw/competitors/eastmoney-innovation/ui-hierarchy/20261118_135242_v1_6_0_step02_suggestion_running.xml` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/ui-hierarchy/raw/20261118_135242_v1_6_0_step02_suggestion_running.xml` | 57 |
| `raw/competitors/eastmoney-innovation/ui-hierarchy/20261118_135325_v1_6_0_step03_suggestion_answer.xml` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/ui-hierarchy/raw/20261118_135325_v1_6_0_step03_suggestion_answer.xml` | 57 |
| `raw/competitors/eastmoney-innovation/ui-hierarchy/20261118_144622_v1.6.0_step19_answer_top.xml` | `research/competitors/eastmoney-innovation/v1.6.0_20261118/ui-hierarchy/raw/20261118_144622_v1.6.0_step19_answer_top.xml` | 0 |
| `raw/competitors/galaxy-stock/metadata/20261117_174911_home.json` | `research/competitors/galaxy-stock/vunknown_20261117/metadata/raw/20261117_174911_home.json` | 914 |
| `raw/competitors/galaxy-stock/metadata/20261117_175304_home_retry.json` | `research/competitors/galaxy-stock/vunknown_20261117/metadata/raw/20261117_175304_home_retry.json` | 933 |
| `raw/competitors/galaxy-stock/screenshots/20261117_174911_home.png` | `research/competitors/galaxy-stock/vunknown_20261117/screenshots/raw/20261117_174911_home.png` | 1205721 |
| `raw/competitors/galaxy-stock/screenshots/20261117_175304_home_retry.png` | `research/competitors/galaxy-stock/vunknown_20261117/screenshots/raw/20261117_175304_home_retry.png` | 1251202 |
| `raw/competitors/galaxy-stock/ui-hierarchy/20261117_174911_home.xml` | `research/competitors/galaxy-stock/vunknown_20261117/ui-hierarchy/raw/20261117_174911_home.xml` | 31841 |
| `raw/competitors/galaxy-stock/ui-hierarchy/20261117_175304_home_retry.xml` | `research/competitors/galaxy-stock/vunknown_20261117/ui-hierarchy/raw/20261117_175304_home_retry.xml` | 31800 |
| `raw/competitors/gtht-lingxiai/metadata/20261117_174924_home.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261117_174924_home.json` | 922 |
| `raw/competitors/gtht-lingxiai/metadata/20261117_175158_home_clean.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261117_175158_home_clean.json` | 928 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_104018_ai_home_2.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_104018_ai_home_2.json` | 937 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_104024_ai_query_typed.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_104024_ai_query_typed.json` | 743 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_104043_ai_answer_15s.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_104043_ai_answer_15s.json` | 740 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_111512_prompt_tapped.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_111512_prompt_tapped.json` | 743 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_111534_prompt_answer_21s.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_111534_prompt_answer_21s.json` | 755 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_111643_home_relaunch.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_111643_home_relaunch.json` | 738 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_111705_prompt_tapped_2.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_111705_prompt_tapped_2.json` | 744 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_111730_prompt_answer_23s_2.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_111730_prompt_answer_23s_2.json` | 756 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_111834_orb_tapped.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_111834_orb_tapped.json` | 729 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_111910_query_typed.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_111910_query_typed.json` | 732 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_111934_query_answer_20s.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_111934_query_answer_20s.json` | 747 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_112028_query_sent.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_112028_query_sent.json` | 729 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_112101_query_answer_24s.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_112101_query_answer_24s.json` | 747 |
| `raw/competitors/gtht-lingxiai/metadata/20261118_112414_query_answer_49s.json` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/metadata/raw/20261118_112414_query_answer_49s.json` | 747 |
| `raw/competitors/gtht-lingxiai/screenshots/20261117_174924_home.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261117_174924_home.png` | 1542298 |
| `raw/competitors/gtht-lingxiai/screenshots/20261117_175158_home_clean.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261117_175158_home_clean.png` | 1584309 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_104018_ai_home_2.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_104018_ai_home_2.png` | 1016040 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_104024_ai_query_typed.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_104024_ai_query_typed.png` | 1617939 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_104043_ai_answer_15s.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_104043_ai_answer_15s.png` | 1617937 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_111512_prompt_tapped.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_111512_prompt_tapped.png` | 90027 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_111534_prompt_answer_21s.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_111534_prompt_answer_21s.png` | 90027 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_111643_home_relaunch.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_111643_home_relaunch.png` | 1020739 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_111705_prompt_tapped_2.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_111705_prompt_tapped_2.png` | 797864 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_111730_prompt_answer_23s_2.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_111730_prompt_answer_23s_2.png` | 806418 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_111834_orb_tapped.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_111834_orb_tapped.png` | 1614835 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_111910_query_typed.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_111910_query_typed.png` | 1120923 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_111934_query_answer_20s.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_111934_query_answer_20s.png` | 1070893 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_112028_query_sent.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_112028_query_sent.png` | 965308 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_112101_query_answer_24s.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_112101_query_answer_24s.png` | 988937 |
| `raw/competitors/gtht-lingxiai/screenshots/20261118_112414_query_answer_49s.png` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/screenshots/raw/20261118_112414_query_answer_49s.png` | 1465204 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261117_174924_home.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261117_174924_home.xml` | 24989 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261117_175158_home_clean.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261117_175158_home_clean.xml` | 24989 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_104018_ai_home_2.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_104018_ai_home_2.xml` | 182693 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_104024_ai_query_typed.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_104024_ai_query_typed.xml` | 24979 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_104043_ai_answer_15s.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_104043_ai_answer_15s.xml` | 24979 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_111512_prompt_tapped.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_111512_prompt_tapped.xml` | 9409 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_111534_prompt_answer_21s.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_111534_prompt_answer_21s.xml` | 9409 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_111643_home_relaunch.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_111643_home_relaunch.xml` | 183837 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_111705_prompt_tapped_2.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_111705_prompt_tapped_2.xml` | 276424 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_111730_prompt_answer_23s_2.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_111730_prompt_answer_23s_2.xml` | 276450 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_111834_orb_tapped.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_111834_orb_tapped.xml` | 24980 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_111910_query_typed.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_111910_query_typed.xml` | 22945 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_111934_query_answer_20s.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_111934_query_answer_20s.xml` | 22950 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_112028_query_sent.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_112028_query_sent.xml` | 34138 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_112101_query_answer_24s.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_112101_query_answer_24s.xml` | 68247 |
| `raw/competitors/gtht-lingxiai/ui-hierarchy/20261118_112414_query_answer_49s.xml` | `research/competitors/gtht-lingxiai/v9.30.45_20261118/ui-hierarchy/raw/20261118_112414_query_answer_49s.xml` | 134696 |
| `raw/competitors/guotai-dazhihui/metadata/20261117_174840_home.json` | `research/competitors/guotai-dazhihui/vunknown_20261117/metadata/raw/20261117_174840_home.json` | 908 |
| `raw/competitors/guotai-dazhihui/screenshots/20261117_174840_home.png` | `research/competitors/guotai-dazhihui/vunknown_20261117/screenshots/raw/20261117_174840_home.png` | 1016839 |
| `raw/competitors/guotai-dazhihui/ui-hierarchy/20261117_174840_home.xml` | `research/competitors/guotai-dazhihui/vunknown_20261117/ui-hierarchy/raw/20261117_174840_home.xml` | 58167 |
| `raw/competitors/hexin-stockassistant/metadata/20261117_174801_home.json` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/metadata/raw/20261117_174801_home.json` | 1038 |
| `raw/competitors/hexin-stockassistant/metadata/20261117_175455_ai_home.json` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/metadata/raw/20261117_175455_ai_home.json` | 1046 |
| `raw/competitors/hexin-stockassistant/metadata/20261117_175601_ai_query_typed.json` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/metadata/raw/20261117_175601_ai_query_typed.json` | 808 |
| `raw/competitors/hexin-stockassistant/metadata/20261118_102736_ai_home_2.json` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/metadata/raw/20261118_102736_ai_home_2.json` | 1053 |
| `raw/competitors/hexin-stockassistant/metadata/20261118_102742_ai_query_typed_2.json` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/metadata/raw/20261118_102742_ai_query_typed_2.json` | 815 |
| `raw/competitors/hexin-stockassistant/metadata/20261118_102809_ai_answer_15s.json` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/metadata/raw/20261118_102809_ai_answer_15s.json` | 806 |
| `raw/competitors/hexin-stockassistant/metadata/20261118_103127_ai_answer_from_suggestion.json` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/metadata/raw/20261118_103127_ai_answer_from_suggestion.json` | 842 |
| `raw/competitors/hexin-stockassistant/screenshots/20261117_174801_home.png` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/screenshots/raw/20261117_174801_home.png` | 306241 |
| `raw/competitors/hexin-stockassistant/screenshots/20261117_175455_ai_home.png` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/screenshots/raw/20261117_175455_ai_home.png` | 303786 |
| `raw/competitors/hexin-stockassistant/screenshots/20261117_175601_ai_query_typed.png` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/screenshots/raw/20261117_175601_ai_query_typed.png` | 359270 |
| `raw/competitors/hexin-stockassistant/screenshots/20261118_102736_ai_home_2.png` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/screenshots/raw/20261118_102736_ai_home_2.png` | 311721 |
| `raw/competitors/hexin-stockassistant/screenshots/20261118_102742_ai_query_typed_2.png` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/screenshots/raw/20261118_102742_ai_query_typed_2.png` | 353917 |
| `raw/competitors/hexin-stockassistant/screenshots/20261118_102809_ai_answer_15s.png` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/screenshots/raw/20261118_102809_ai_answer_15s.png` | 269326 |
| `raw/competitors/hexin-stockassistant/screenshots/20261118_103127_ai_answer_from_suggestion.png` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/screenshots/raw/20261118_103127_ai_answer_from_suggestion.png` | 269604 |
| `raw/competitors/hexin-stockassistant/ui-hierarchy/20261117_174801_home.xml` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/ui-hierarchy/raw/20261117_174801_home.xml` | 93703 |
| `raw/competitors/hexin-stockassistant/ui-hierarchy/20261117_175455_ai_home.xml` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/ui-hierarchy/raw/20261117_175455_ai_home.xml` | 93703 |
| `raw/competitors/hexin-stockassistant/ui-hierarchy/20261117_175601_ai_query_typed.xml` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/ui-hierarchy/raw/20261117_175601_ai_query_typed.xml` | 93422 |
| `raw/competitors/hexin-stockassistant/ui-hierarchy/20261118_102736_ai_home_2.xml` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/ui-hierarchy/raw/20261118_102736_ai_home_2.xml` | 94048 |
| `raw/competitors/hexin-stockassistant/ui-hierarchy/20261118_102742_ai_query_typed_2.xml` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/ui-hierarchy/raw/20261118_102742_ai_query_typed_2.xml` | 93507 |
| `raw/competitors/hexin-stockassistant/ui-hierarchy/20261118_102809_ai_answer_15s.xml` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/ui-hierarchy/raw/20261118_102809_ai_answer_15s.xml` | 258901 |
| `raw/competitors/hexin-stockassistant/ui-hierarchy/20261118_103127_ai_answer_from_suggestion.xml` | `research/competitors/hexin-stockassistant/v5.3.1_20261118/ui-hierarchy/raw/20261118_103127_ai_answer_from_suggestion.xml` | 256623 |
| `raw/competitors/htsc-cftlight/metadata/20261117_174852_home.json` | `research/competitors/htsc-cftlight/v2.0.6_20261118/metadata/raw/20261117_174852_home.json` | 985 |
| `raw/competitors/htsc-cftlight/metadata/20261118_103816_ai_home_2.json` | `research/competitors/htsc-cftlight/v2.0.6_20261118/metadata/raw/20261118_103816_ai_home_2.json` | 1001 |
| `raw/competitors/htsc-cftlight/metadata/20261118_103821_agent_center.json` | `research/competitors/htsc-cftlight/v2.0.6_20261118/metadata/raw/20261118_103821_agent_center.json` | 787 |
| `raw/competitors/htsc-cftlight/metadata/20261118_113000_home_relaunch.json` | `research/competitors/htsc-cftlight/v2.0.6_20261118/metadata/raw/20261118_113000_home_relaunch.json` | 754 |
| `raw/competitors/htsc-cftlight/metadata/20261118_113030_home_cold.json` | `research/competitors/htsc-cftlight/v2.0.6_20261118/metadata/raw/20261118_113030_home_cold.json` | 701 |
| `raw/competitors/htsc-cftlight/metadata/20261118_113148_ai_avatar_tapped.json` | `research/competitors/htsc-cftlight/v2.0.6_20261118/metadata/raw/20261118_113148_ai_avatar_tapped.json` | 735 |
| `raw/competitors/htsc-cftlight/metadata/20261118_120427_ai_query_running.json` | `research/competitors/htsc-cftlight/v2.0.6_20261118/metadata/raw/20261118_120427_ai_query_running.json` | 739 |
| `raw/competitors/htsc-cftlight/metadata/20261118_120456_ai_answer_30s.json` | `research/competitors/htsc-cftlight/v2.0.6_20261118/metadata/raw/20261118_120456_ai_answer_30s.json` | 730 |
| `raw/competitors/htsc-cftlight/metadata/20261118_120727_ai_query_running_2.json` | `research/competitors/htsc-cftlight/v2.0.6_20261118/metadata/raw/20261118_120727_ai_query_running_2.json` | 751 |
| `raw/competitors/htsc-cftlight/screenshots/20261117_174852_home.png` | `research/competitors/htsc-cftlight/v2.0.6_20261118/screenshots/raw/20261117_174852_home.png` | 1009262 |
| `raw/competitors/htsc-cftlight/screenshots/20261118_103816_ai_home_2.png` | `research/competitors/htsc-cftlight/v2.0.6_20261118/screenshots/raw/20261118_103816_ai_home_2.png` | 1041791 |
| `raw/competitors/htsc-cftlight/screenshots/20261118_103821_agent_center.png` | `research/competitors/htsc-cftlight/v2.0.6_20261118/screenshots/raw/20261118_103821_agent_center.png` | 2293232 |
| `raw/competitors/htsc-cftlight/screenshots/20261118_113000_home_relaunch.png` | `research/competitors/htsc-cftlight/v2.0.6_20261118/screenshots/raw/20261118_113000_home_relaunch.png` | 2286923 |
| `raw/competitors/htsc-cftlight/screenshots/20261118_113030_home_cold.png` | `research/competitors/htsc-cftlight/v2.0.6_20261118/screenshots/raw/20261118_113030_home_cold.png` | 837312 |
| `raw/competitors/htsc-cftlight/screenshots/20261118_113148_ai_avatar_tapped.png` | `research/competitors/htsc-cftlight/v2.0.6_20261118/screenshots/raw/20261118_113148_ai_avatar_tapped.png` | 430501 |
| `raw/competitors/htsc-cftlight/screenshots/20261118_120427_ai_query_running.png` | `research/competitors/htsc-cftlight/v2.0.6_20261118/screenshots/raw/20261118_120427_ai_query_running.png` | 338976 |
| `raw/competitors/htsc-cftlight/screenshots/20261118_120456_ai_answer_30s.png` | `research/competitors/htsc-cftlight/v2.0.6_20261118/screenshots/raw/20261118_120456_ai_answer_30s.png` | 340963 |
| `raw/competitors/htsc-cftlight/screenshots/20261118_120727_ai_query_running_2.png` | `research/competitors/htsc-cftlight/v2.0.6_20261118/screenshots/raw/20261118_120727_ai_query_running_2.png` | 648646 |
| `raw/competitors/htsc-cftlight/ui-hierarchy/20261117_174852_home.xml` | `research/competitors/htsc-cftlight/v2.0.6_20261118/ui-hierarchy/raw/20261117_174852_home.xml` | 37214 |
| `raw/competitors/htsc-cftlight/ui-hierarchy/20261118_103816_ai_home_2.xml` | `research/competitors/htsc-cftlight/v2.0.6_20261118/ui-hierarchy/raw/20261118_103816_ai_home_2.xml` | 35660 |
| `raw/competitors/htsc-cftlight/ui-hierarchy/20261118_103821_agent_center.xml` | `research/competitors/htsc-cftlight/v2.0.6_20261118/ui-hierarchy/raw/20261118_103821_agent_center.xml` | 5695 |
| `raw/competitors/htsc-cftlight/ui-hierarchy/20261118_113000_home_relaunch.xml` | `research/competitors/htsc-cftlight/v2.0.6_20261118/ui-hierarchy/raw/20261118_113000_home_relaunch.xml` | 5695 |
| `raw/competitors/htsc-cftlight/ui-hierarchy/20261118_113030_home_cold.xml` | `research/competitors/htsc-cftlight/v2.0.6_20261118/ui-hierarchy/raw/20261118_113030_home_cold.xml` | 31704 |
| `raw/competitors/htsc-cftlight/ui-hierarchy/20261118_113148_ai_avatar_tapped.xml` | `research/competitors/htsc-cftlight/v2.0.6_20261118/ui-hierarchy/raw/20261118_113148_ai_avatar_tapped.xml` | 37127 |
| `raw/competitors/htsc-cftlight/ui-hierarchy/20261118_120427_ai_query_running.xml` | `research/competitors/htsc-cftlight/v2.0.6_20261118/ui-hierarchy/raw/20261118_120427_ai_query_running.xml` | 63042 |
| `raw/competitors/htsc-cftlight/ui-hierarchy/20261118_120456_ai_answer_30s.xml` | `research/competitors/htsc-cftlight/v2.0.6_20261118/ui-hierarchy/raw/20261118_120456_ai_answer_30s.xml` | 63048 |
| `raw/competitors/htsc-cftlight/ui-hierarchy/20261118_120727_ai_query_running_2.xml` | `research/competitors/htsc-cftlight/v2.0.6_20261118/ui-hierarchy/raw/20261118_120727_ai_query_running_2.xml` | 42642 |
| `raw/competitors/pingan-smt/metadata/20261117_174827_home.json` | `research/competitors/pingan-smt/vunknown_20261117/metadata/raw/20261117_174827_home.json` | 884 |
| `raw/competitors/pingan-smt/screenshots/20261117_174827_home.png` | `research/competitors/pingan-smt/vunknown_20261117/screenshots/raw/20261117_174827_home.png` | 413838 |
| `raw/competitors/pingan-smt/ui-hierarchy/20261117_174827_home.xml` | `research/competitors/pingan-smt/vunknown_20261117/ui-hierarchy/raw/20261117_174827_home.xml` | 13549 |
| `raw/target-dongzheng-ai/01-screenshots/20261117_004_side_menu.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/20261117_004_side_menu.png` | 341771 |
| `raw/target-dongzheng-ai/01-screenshots/20261117_005_account_settings.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/20261117_005_account_settings.png` | 153840 |
| `raw/target-dongzheng-ai/01-screenshots/20261117_164222_006_account_settings.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/20261117_164222_006_account_settings.png` | 163149 |
| `raw/target-dongzheng-ai/01-screenshots/20261117_165153_015_trade_settings.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/20261117_165153_015_trade_settings.png` | 114215 |
| `raw/target-dongzheng-ai/01-screenshots/20261117_165330_018_back_to_drawer.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/20261117_165330_018_back_to_drawer.png` | 344736 |
| `raw/target-dongzheng-ai/01-screenshots/20261117_165345_019_home_return.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/20261117_165345_019_home_return.png` | 749243 |
| `raw/target-dongzheng-ai/01-screenshots/20261117_165805_026_back_from_wrong_stock_detail.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/20261117_165805_026_back_from_wrong_stock_detail.png` | 749317 |
| `raw/target-dongzheng-ai/01-screenshots/20261117_170736_040_stock_600519_news_tab.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/20261117_170736_040_stock_600519_news_tab.png` | 408363 |
| `raw/target-dongzheng-ai/01-screenshots/20261117_170743_040b_stock_600519_news_tab_after_4s.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/20261117_170743_040b_stock_600519_news_tab_after_4s.png` | 408385 |
| `raw/target-dongzheng-ai/01-screenshots/20261117_170819_042_stock_600519_fund_holding.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/20261117_170819_042_stock_600519_fund_holding.png` | 427242 |
| `raw/target-dongzheng-ai/01-screenshots/20261117_173803_066_ai_query_600519_after_cold_start.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/20261117_173803_066_ai_query_600519_after_cold_start.png` | 260135 |
| `raw/target-dongzheng-ai/01-screenshots/20261118_095653_074_retest_watchlist.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/20261118_095653_074_retest_watchlist.png` | 809538 |
| `raw/target-dongzheng-ai/01-screenshots/recents_before_swipe.png` | `research/target-dongzheng-ai/screenshots/v1.0.0_20261118/raw/recents_before_swipe.png` | 702793 |
| `raw/target-dongzheng-ai/02-ui-hierarchy/20261117_004_side_menu.xml` | `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/raw/20261117_004_side_menu.xml` | 38147 |
| `raw/target-dongzheng-ai/02-ui-hierarchy/20261117_005_account_settings.xml` | `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/raw/20261117_005_account_settings.xml` | 14648 |
| `raw/target-dongzheng-ai/02-ui-hierarchy/20261117_164222_006_account_settings.xml` | `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/raw/20261117_164222_006_account_settings.xml` | 16107 |
| `raw/target-dongzheng-ai/02-ui-hierarchy/20261117_165153_015_trade_settings.xml` | `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/raw/20261117_165153_015_trade_settings.xml` | 13438 |
| `raw/target-dongzheng-ai/02-ui-hierarchy/20261117_165330_018_back_to_drawer.xml` | `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/raw/20261117_165330_018_back_to_drawer.xml` | 38147 |
| `raw/target-dongzheng-ai/02-ui-hierarchy/20261117_165345_019_home_return.xml` | `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/raw/20261117_165345_019_home_return.xml` | 29322 |
| `raw/target-dongzheng-ai/02-ui-hierarchy/20261117_165805_026_back_from_wrong_stock_detail.xml` | `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/raw/20261117_165805_026_back_from_wrong_stock_detail.xml` | 29322 |
| `raw/target-dongzheng-ai/02-ui-hierarchy/20261117_170736_040_stock_600519_news_tab.xml` | `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/raw/20261117_170736_040_stock_600519_news_tab.xml` | 47446 |
| `raw/target-dongzheng-ai/02-ui-hierarchy/20261117_170743_040b_stock_600519_news_tab_after_4s.xml` | `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/raw/20261117_170743_040b_stock_600519_news_tab_after_4s.xml` | 47446 |
| `raw/target-dongzheng-ai/02-ui-hierarchy/20261117_170819_042_stock_600519_fund_holding.xml` | `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/raw/20261117_170819_042_stock_600519_fund_holding.xml` | 52207 |
| `raw/target-dongzheng-ai/02-ui-hierarchy/20261117_173803_066_ai_query_600519_after_cold_start.xml` | `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/raw/20261117_173803_066_ai_query_600519_after_cold_start.xml` | 19521 |
| `raw/target-dongzheng-ai/02-ui-hierarchy/20261118_095653_074_retest_watchlist.xml` | `research/target-dongzheng-ai/ui-hierarchy/v1.0.0_20261118/raw/20261118_095653_074_retest_watchlist.xml` | 31152 |
| `raw/target-dongzheng-ai/03-logs/20261117_164134_settings_home_current.log` | `research/target-dongzheng-ai/logs/v1.0.0_20261118/raw/20261117_164134_settings_home_current.log` | 548 |
| `raw/target-dongzheng-ai/03-logs/20261117_164510_privacy_policy_webview_wait.log` | `research/target-dongzheng-ai/logs/v1.0.0_20261118/raw/20261117_164510_privacy_policy_webview_wait.log` | 548 |
| `raw/target-dongzheng-ai/app-internal/crash_report_listing.txt` | `research/target-dongzheng-ai/logs/v1.0.0_20261118/app-internal/crash_report_listing.txt` | 77 |
| `raw/target-dongzheng-ai/app-internal/ilog_latest.txt` | `research/target-dongzheng-ai/logs/v1.0.0_20261118/app-internal/ilog_latest.txt` | 1068 |
| `raw/target-dongzheng-ai/app-internal/ilog_records.log` | `research/target-dongzheng-ai/logs/v1.0.0_20261118/app-internal/ilog_records.log` | 15 |
| `raw/target-dongzheng-ai/app-internal/TAFLogin.log` | `research/target-dongzheng-ai/logs/v1.0.0_20261118/app-internal/TAFLogin.log` | 32959 |
| `raw/target-dongzheng-ai/app-internal/TAFNetwork.log` | `research/target-dongzheng-ai/logs/v1.0.0_20261118/app-internal/TAFNetwork.log` | 386520 |
| `raw/target-dongzheng-ai/app-internal/TAFNetwork_after_ai.log` | `research/target-dongzheng-ai/logs/v1.0.0_20261118/app-internal/TAFNetwork_after_ai.log` | 392952 |
| `raw/target-dongzheng-ai/app-internal/webview_error_hits.txt` | `research/target-dongzheng-ai/logs/v1.0.0_20261118/app-internal/webview_error_hits.txt` | 0 |
| `raw/target-dongzheng-ai/app-internal/webview_privacy_hits.txt` | `research/target-dongzheng-ai/logs/v1.0.0_20261118/app-internal/webview_privacy_hits.txt` | 0 |
| `raw/target-dongzheng-ai/app-internal/webview_url_candidates.txt` | `research/target-dongzheng-ai/logs/v1.0.0_20261118/app-internal/webview_url_candidates.txt` | 0 |

## 完整性检查

- 198 个证据文件均已复制到目标目录并完成 SHA-256 校验。
- 所有 JSON 中的 `screenshot`、`ui_xml`、`summary` 引用均已解析到真实文件。
- 原始证据本身有 5 个异常文件，迁移时保持原样，没有伪造或覆盖：
  - `research/target-dongzheng-ai/archive/20261117_flat_screenshots/20261117_171554_048_ai_query_600519_corrected.png`：截断 PNG
  - `research/competitors/eastmoney-innovation/v1.6.0_20261118/screenshots/raw/20261118_144621_v1.6.0_step19_answer_top.png`：截断 PNG
  - `research/competitors/eastmoney-innovation/v1.6.0_20261118/ui-hierarchy/raw/20261118_135242_v1_6_0_step02_suggestion_running.xml`：非 XML 内容
  - `research/competitors/eastmoney-innovation/v1.6.0_20261118/ui-hierarchy/raw/20261118_135325_v1_6_0_step03_suggestion_answer.xml`：非 XML 内容
  - `research/competitors/eastmoney-innovation/v1.6.0_20261118/ui-hierarchy/raw/20261118_144622_v1.6.0_step19_answer_top.xml`：空 XML
