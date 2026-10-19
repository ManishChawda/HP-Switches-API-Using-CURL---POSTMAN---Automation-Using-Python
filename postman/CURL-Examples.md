# cURL Examples for HP Switches

These examples demonstrate how to send HTTP requests from the command line.

## Before You Begin

- Confirm that your switch model and firmware support the API endpoint.
- Replace all placeholders with your own device details.
- Use only authorized lab devices.
- Do not put real passwords or tokens directly in commands that may be saved in shell history.

## Example: Basic HTTP Request

```bash
curl --request GET \
  --url "https://<SWITCH_IP>/<API_ENDPOINT>" \
  --user "<USERNAME>"
```

Replace `<SWITCH_IP>`, `<API_ENDPOINT>`, and `<USERNAME>` with your lab values. cURL will prompt for the password.

## Important

The exact endpoint, HTTP method, authentication method, headers, and request body depend on the switch model and firmware. Verify these details in the relevant device documentation before running a request.

Use trusted TLS certificates wherever possible. Do not disable TLS verification in production.
