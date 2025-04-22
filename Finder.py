# This line imports the uuid module, which is a built-in tool in Python that generates UUIDs.
import uuid

# This creates a *UUID* object from a string that represents a specific GUID.
# It's basically a fixed identifier used as a *namespace* for generating UUIDs.
terminalNamespaceGUID = uuid.UUID("{2bde4a90-d05f-401c-9492-e40884ead1d8}")

# This makes a new UUID by using the `terminalNamespaceGUID` from the previous line.
# It also uses the string "Far" by turning it into byte format `UTF-16LE encoding`, and then decodes it back into a normal string using `ASCII`.
# The `uuid5` function uses both the namespace AND the name to create a UUID based on them.
# Replace "Far" with the app's name (Case Sensitive)
profileGUID = uuid.uuid5(terminalNamespaceGUID, "Far".encode("UTF-16LE").decode("ASCII"))

# This outputs the profileGUID (UUID) within curly braces.
print(f"{{{profileGUID}}}")

# WindowsGUIDFinder
# Python 3.13.3
# Credits to: Microsoft
