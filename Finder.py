import uuid

terminalNamespaceGUID = uuid.UUID("{2bde4a90-d05f-401c-9492-e40884ead1d8}")

# Replace "Far" with the app's name (Case Sensitive)
profileGUID = uuid.uuid5(terminalNamespaceGUID, "Far".encode("UTF-16LE").decode("ASCII"))

print(f"{{{profileGUID}}}")
