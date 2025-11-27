# [cite_start]Makefile for Team PHQ Project [cite: 2]

PYTHON = python3

.PHONY: run-server run-client clean help

help:
	@echo "Commands:"
	@echo "  make run-server      : Start the server"
	@echo "  make run-client      : Request index.html"
	@echo "  make run-about       : Request about.html"
	@echo "  make run-txt         : Request test.txt"

run-server:
	@echo "Starting Team PHQ Server..."
	$(PYTHON) server.py

run-client:
	@echo "Fetching index.html..."
	$(PYTHON) client.py index.html

run-about:
	@echo "Fetching about.html..."
	$(PYTHON) client.py about.html

run-txt:
	@echo "Fetching test.txt..."
	$(PYTHON) client.py test.txt