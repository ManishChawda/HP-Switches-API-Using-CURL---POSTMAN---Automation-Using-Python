## cURL and Postman API Examples

The `postman/` directory contains a sanitized Postman collection for the supported switch API examples.

### Postman

1. Open Postman and select **Import**.
2. Import `postman/HP-Switches-API.postman_collection.json`.
3. Configure the required device URLs and credentials locally.
4. Execute requests only against switches you are authorized to administer.

### cURL

cURL examples demonstrate how to send HTTP requests from the command line. Use the API endpoint, authentication method, headers, and request body appropriate to your switch model and firmware.

**Important:** The cURL examples are templates and have not been verified against every supported switch model or firmware version. Before execution, confirm the API endpoint, HTTP method, authentication method, headers, and request body against the documentation for your specific device. Test requests in an authorized lab environment first.

### Security

- Never commit real passwords, authentication tokens, session IDs, or private device details.
- Use trusted TLS certificates wherever possible.
- Any instructions for bypassing TLS verification are for isolated labs only, not production environments.
