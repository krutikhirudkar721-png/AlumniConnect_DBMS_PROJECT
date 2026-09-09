# Test Cases

| ID | Area | Test | Expected |
|---|---|---|---|
| TC01 | Auth | Valid login | Dashboard opens |
| TC02 | Auth | Invalid password | Login rejected |
| TC03 | Auth | Logout | Session cleared |
| TC04 | Auth | Alumni opens admin route | 403 |
| TC05 | Alumni | Add valid record | Record created |
| TC06 | Alumni | Duplicate email | Rejected |
| TC07 | Alumni | Edit own profile | Update succeeds |
| TC08 | Alumni | Admin delete | Dependent rows handled by FK |
| TC09 | Search | Name | Matching results |
| TC10 | Search | Department | Matching results |
| TC11 | Search | Skill | Matching results |
| TC12 | Search | Combined filters | AND semantics |
| TC13 | Search | No result | Empty state |
| TC14 | DB | Invalid FK | Constraint rejection |
| TC15 | DB | Duplicate skill mapping | PK rejection |
| TC16 | DB | Rollback | Uncommitted changes removed |
