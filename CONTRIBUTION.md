# Team PHQ - Contribution Report

## Team Members
1. **Sourav Md Shariful Islam** - Networking Logic
2. **Ahammed Tanim** - Client UI
3. **Tamim Md** - Request Routing & File Handling
4. **Fahad Md Mainuddin** - Testing + README

## Detailed Contributions

### Sourav Md Shariful Islam
* Implemented the core socket server in `server.py`.
* Added threading support for concurrent client handling.

### Ahammed Tanim
* Built `client.py` and the command-line argument logic.
* Ensured the client can request specific files (`sys.argv`).

### Tamim Md
* Implemented the file handling logic to read from the `public/` directory.
* Wrote the MIME type detection (Text vs HTML).

### Fahad Md Mainuddin
* Created the `public/` directory assets (`index.html`, `about.html`, `test.txt`).
* Wrote `README.md` and verified the Makefile works.