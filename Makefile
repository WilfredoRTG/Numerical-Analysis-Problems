.DEFAULT_GOAL := help

# See all the available commands.
.PHONY: help
help: 
	@echo "Commands for use: "
	@echo "-- make 2.1"
	@echo "-- make 2.2"

# Run the 2.1 algorithm.
.PHONY: 2.1
2.1:
	@cd .\Chapter2 && python .\2.1.py

# Run the 2.2 algorithm.
.PHONY: 2.2
2.2:
	@cd .\Chapter2 && python .\2.2.py