# WindowsGUIDFinder
This short but powerful **Python** script helps generate `GUID's` for applications to be used in **Windows Terminal Profiles**.
A `GUID` **( Global Unique Identifier )** is used by the **Windows Terminal** to uniquely identify each **Shell** and/or **Profile**.
**( i.e.** ***PowerShell***, ***Command Prompt*** **)**.
*This also applies to* **Third Party Tools** *like:* **(** ***Ubuntu*** ***Far Manager, Cygwin, CMDer, etc*** **)**.

## How it Works:
*For this guide, I'll be getting the `GUID` for* **Far Manager**.
```python
import uuid
```
*This imports* **Pythons** *build-in `uuid` module, it provides functions to create `UUID's` and `GUID's`.
```python
terminalNamespaceGUID = uuid.UUID("{2bde4a90-d05f-401c-9492-e40884ead1d8}")
```
*This defines a* ***constant namespace*** `GUID` *used by the* **Windows Terminal** *that ensures the generated `GUID's` are always consistent when given the same input string.
```python
profileGUID = uuid.uuid5(terminalNamespaceGUID, "Far".encode("UTF-16LE").decode("ASCII"))
```
*This uses `uuid5()` to create a `version 5 UUID`, that is based on the `name (string)` and* **namespace**. *The name for the app I used is `Far`.*
*The string is encoded in `UTF-16LE` and its decoded as `ASCII`, which mimics the way **Windows** encodes strings internally. This makes sure that the output `GUID` matches what the **Windows Terminal** would expect*.
```python
print(f"{{{profileGUID}}}")
```
*This just prints the output `GUID` in the same format that the* **Windows Terminal** *uses*.

# Usage

*To generate the `GUID` for an app, Replace "Far" in the line below with the **exact name** of the app.*
```python
profileGUID = uuid.uuid5(terminalNamespaceGUID, "Far".encode("UTF-16LE").decode("ASCII"))
```
*This allows you to make a unique and constant `GUID` that you can paste into your* **Windows Terminal's** *`settings.json`*

**Examples of Third Party Profiles:**
***(Cygwin, Ubuntu, Far Manager, Cmder, Git Bash, Multipass, Neofetch, etc)***


## But most importantly, Have Fun :)


### WindowsGUIDFinder
### Version 1.0
### Python 3.13.3
### Forked from `Microsoft`
