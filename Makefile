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
	@python3 Chapter2/2.1.py

# Run the 2.2 algorithm.
.PHONY: 2.2
2.2:
	@python3 Chapter2/2.2.py

# Run the 2.3 algorithm.
.PHONY: 2.3
2.3:
	@python3 Chapter2/2.3.py

# Run the 2.4 algorithm.
.PHONY: 2.4
2.4:
	@python3 Chapter2/2.4.py

# Run the 2.5 algorithm.
.PHONY: 2.5
2.5:
	@python3 Chapter2/2.5.py