# The following views are available

## Do not require auth user
- restaurant/menu: Supports GET and POST methods
- restaurant/menu/\<int:pk>: Supports GET, PUT and DELETE methods
- restaurant/api-token-auth: Supports POST. Response includes auth token
  
## Require auth token
- restaurant/booking/tables: Supports GET and POST.