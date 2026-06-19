import json
import jsonschema
from urllib.request import urlopen

# Load server.json
with open("server.json", "r", encoding="utf-8") as f:
    server_data = json.load(f)

# Fetch schema from official URL
schema_url = server_data.get("$schema", "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json")
print(f"Fetching schema from: {schema_url}")
with urlopen(schema_url) as response:
    schema = json.load(response)

# Validate
print("Validating server.json...")
try:
    jsonschema.validate(instance=server_data, schema=schema)
    print("[PASS] Validation passed! server.json is valid.")
except jsonschema.ValidationError as e:
    print(f"[FAIL] Validation failed!")
    print(f"   Error: {e.message}")
    print(f"   Path: {' -> '.join(str(p) for p in e.absolute_path)}")
except Exception as e:
    print(f"[ERROR] Error during validation: {e}")
