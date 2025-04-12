# API Security

1. Https
   1. Encrypted connection between client and API server
2. OAuth2 (no share credentials, use temporary access token)
   1. user -> app -> authorization server
   2. authorization server -> user : request permission 
   3. user -> authorization server : request approved 
   4. authorization server -> app : permission granted
   5. app -> authorization server : get access token 
   6. authorization server -> app : give access token 
   7. app -> resource server : request data with access token
   8. resource server -> app : return data 
3. WebAuthn (Web Authentication)
   1. facial recognition, fingerprints, authenticator(?), 
4. Implement Authorization
   1. Role-based access control (RBAC)
5. Leveled API Keys
   1. using a single API key is risky
   2. implement api keys with varing access levels.
   3. rotate keys periodically
   4. expiration time
6. Rate Limiting
   1. Rate: 1000 req/day
   2. factors: IP address, User ID, API key, types of requests, 
   3. security, performance, availability, 
7. API Versioning 
   1. backward compatibility
   2. GET/v1/users/123
8. Allow Listing
   1. allow access depends on IP addresses, User IDs, API Keys, 
   2. deny all, permit some
   3. allow list roles 
9. OWASP Security Risks 
   1. Guide lines 
   2. OWASP top 10 API Security Risks 
10. API Gateway
    1. clients -> API Gateway (a single access point) -> APIs
    2. a centralized layer.
    3. security policy enforcements 
    4. rate limiting, authentication, and other cross-cutting concerns
    5. traffic management 
11. Error Handling
    1. Error, API security, User experience 
    2. not show internal server error, not expose sensitive data 
    3. user friendly error message, generic,  
    4. 200: success, 400: bad request, 500: internal server error
12. Input Validation
    1. request parameter, header, payload
    2. SQL injection, Cross-site scripting, 
    3. client side, server side validations
 13. 