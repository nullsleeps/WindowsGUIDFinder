# WindowsGUIDFinder

## Jump To:
- [How to Use the Script](https://github.com/nullsleeps/WindowsGUIDFinder#how-to-use-the-script)
- [How it Works](https://github.com/nullsleeps/WindowsGUIDFinder#how-it-works)
- [Extras](https://github.com/nullsleeps/WindowsGUIDFinder#extras)
- [Microsoft's Original Code](https://github.com/nullsleeps/WindowsGUIDFinder#microsofts-original-code)


This short but powerful [**`Python script`**](Finder.py) helps generate `GUID's` for applications to be used in **Windows Terminal Profiles**.
A `GUID` **( Global Unique Identifier )** is used by the **Windows Terminal** to uniquely identify each **Shell** and/or **Profile**.
**( i.e.** ***PowerShell***, ***Command Prompt*** **)**.
*This also applies to* **Third Party Tools** *like:* **(** ***Ubuntu*** ***Far Manager, Cygwin, CMDer, etc*** **)**.


# How to Use the Script

*To generate the `GUID` for an app, Replace* `"Far"` *in the line below with the **exact name** of the app.*
```python
profileGUID = uuid.uuid5(terminalNamespaceGUID, "Far".encode("UTF-16LE").decode("ASCII"))
```
*This allows you to make a unique and constant `GUID` that you can paste into your* **`Windows Terminal's`** ***`settings.json`***

# How it Works:

> *For this guide, I'll be getting the `GUID` for* **`Far Manager`** *as an example*.
```python
import uuid
```
*This imports* **Pythons** *built-in `uuid` module, it provides functions to create `UUID's` and `GUID's`.
```python
terminalNamespaceGUID = uuid.UUID("{2bde4a90-d05f-401c-9492-e40884ead1d8}")
```
*This defines a* ***constant namespace*** `GUID` *used by the* **`Windows Terminal`** *that ensures the generated `GUID's` are always consistent when given the same **`input string`**.*
```python
profileGUID = uuid.uuid5(terminalNamespaceGUID, "Far".encode("UTF-16LE").decode("ASCII"))
```
*This uses `uuid5()` to create a `version 5 UUID`, that is based on the `name (string)` and* **namespace**. *The name for the app I used is `Far`.*
*The string is encoded in `UTF-16LE` and its decoded as `ASCII`, which mimics the way **Windows** encodes strings internally. This makes sure that the output `GUID` matches what the **Windows Terminal** would expect*.
```python
print(f"{{{profileGUID}}}")
```
*This just prints the output `GUID` in the same format that the* **Windows Terminal** *uses*.

### *Examples of Third Party Profiles Include:*
- **`Cygwin`**
- **`Ubuntu`**
- **`Far Manager`**
- **`Cmder`**
- **`Git Bash`**
- **`Multipass`**
- **`Neofetch`**
***And much more!***


# Extras
*`WindowsGUIDFinder`*
*`Version 1.0`*
*`Python 3.13.3`*


# Microsofts Original Code

> [!IMPORTANT]
> This code is originally from [Microsoft's Website](https://learn.microsoft.com/en-us/windows/terminal/json-fragment-extensions) and was simply reuploaded with more instructions and detail on how to use it and how it works.

![Microsoft's Original Code on Their Website](https://i.imgur.com/zniBpR0.png)


## And most importantly, Have Fun :)
